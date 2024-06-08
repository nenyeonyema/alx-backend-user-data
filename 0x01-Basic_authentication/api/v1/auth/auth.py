#!/usr/bin/env python3
""" API Authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorizes header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        return None
