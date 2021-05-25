import json
from functools import wraps
from urllib.request import urlopen

from flask import request, abort
from jose import jwt, exceptions

AUTH0_DOMAIN = 'fish-coffee-shop.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'fish-coffee-shop'


# Auth Header
def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401, 'Authorization header required')

    auth_header = request.headers['Authorization']
    header_parts = auth_header.split(' ')

    if len(header_parts) != 2:
        abort(401, 'Malformed header')
    elif header_parts[0].lower() != 'bearer':
        abort(401, 'Auth token needs to be bearer token')

    return header_parts[1]


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        abort(403, 'Permissions not included in JWT.')

    if permission not in payload['permissions']:
        abort(403, 'Permission not found.')
    return True


def verify_decode_jwt(token):
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN THE HEADER
    try:
        unverified_header = jwt.get_unverified_header(token)
    except exceptions.JWTError:
        abort(400, 'Could not decode JWT token')

    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        abort(401, 'Authorization malformed.')

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    # Finally, verify!!!
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            abort(401, 'Token expired.')

        except jwt.JWTClaimsError:
            abort(401, 'Incorrect claims. Please, check the audience and issuer.')

        except Exception:
            abort(400, 'Unable to parse authentication token')

    abort(403, "Missing permissions")


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
