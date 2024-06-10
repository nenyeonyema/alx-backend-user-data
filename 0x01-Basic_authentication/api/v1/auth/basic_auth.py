#!/usr/bin/env python3
""" Basic Auth
"""
import base64
from typing import TypeVar
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

        Parameters:
        authorization_header (str): The Authorization header string.

        Returns:
        (str): The Base64 encoded part of the header, or None if invalid.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Extract the Base64 part after "Basic "
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string to its UTF-8 string representation.
        Returns None if the input is invalid.

        Parameters:
            base64_authorization_header (str): The Base64 string to decode.

        Returns:
            (str) or None: The decoded UTF-8 string, or None if invalid.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            # Decode the Base64 string to bytes
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # Convert bytes to UTF-8 string
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None
