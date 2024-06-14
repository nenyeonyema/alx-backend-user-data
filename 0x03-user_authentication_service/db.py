#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User
from user import Base
from typing import Optional, Dict, Any


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Adds new user

            Parmeters:
                email (str): the users email
                hashed_password (str): The user's hashed password

            Returns:
                User: The new user object
        """

        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    
        return new_user

    def find_user_by(self, **kwargs: Dict[str, Any]) -> User:
        """ Find a user by arbitrary keyword arguments.
        
            Args:
                **kwargs (Dict[str, Any]): Arbitrary keyword arguments to filter the query.
        
            Returns:
                User: The found User object.
        
            Raises:
                NoResultFound: If no user is found matching the query.
                InvalidRequestError: If invalid query arguments are passed.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound("Not found")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid")
