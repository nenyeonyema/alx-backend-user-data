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
        if path is None:
            return True

        if not excluded_paths:
            return True

        path_slashed = path if path.endswith('/') else path + '/'

        for each_path in excluded_paths:
            slashed_excluded_paths = each_path if each_path.endswith('/')\
                    else each_path + '/'
            if path_slashed == slashed_excluded_paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Authorizes header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        return None
