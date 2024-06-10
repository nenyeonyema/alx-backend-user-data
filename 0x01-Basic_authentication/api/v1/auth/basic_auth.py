#!/usr/bin/env python3
""" Basic Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ 
    BasicAuth class that inherits from Auth.
    Implements Basic Authentication methods.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ 
        Extracts the Base64 part of the Authorization header for Basic Authentication.
        Returns None if the header is invalid or does not start with 'Basic '.

        param: - authorization_header: The Authorization header string.
        return: - The Base64 encoded part of the header, or None if invalid.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Extract the Base64 part after "Basic "
        return authorization_header[6:]
