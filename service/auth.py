import datetime as dt
import calendar
import jwt
from flask import abort
from service.user import UserService
from constants import JWT_SECRET, JWT_ALGORITHM


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email: str, password: str | None, is_refresh=False) -> dict:
        user = self.user_service.get_by_email(email)
        if user is None:
            raise abort(404)
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "email": user.email,
            "role": user.role
        }

        min30 = dt.datetime.now() + dt.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        days130 = dt.datetime.now() + dt.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = data['email']
        return self.generate_tokens(email, None, is_refresh=True)
