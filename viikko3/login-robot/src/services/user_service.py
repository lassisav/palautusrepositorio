from entities.user import User
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)
        
        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        ### Too Short Username
        if len(username) < 3:
            raise UserInputError("Username too short")
        
        ### Username long enough but invalid
        if not re.search("^[a-z]{3,}$", username):
            raise UserInputError("Invalid username")

        ### Password too short
        if len(password) < 8:
            raise UserInputError("Password too short")

        ### Username taken
        user  = self._user_repository.find_by_username(username)
        if user != None:
            raise AuthenticationError("Username already taken")
        
        ### Password only letters
        if re.search("^[a-z]+$", password):
            raise UserInputError("Password cannot contain only letters")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
