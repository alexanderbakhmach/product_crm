from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from models import Base, User
from schemas import UserSchema


class AuthenticationService:
    name = "authentication_service"
    db = DatabaseSession(Base)

    @rpc
    def sign_up(self, email, password):
        user = User(email=email, password=password)
        self.db.add(user)
        self.db.commit()

        user = UserSchema().dump(user)

        print(user)

        return user