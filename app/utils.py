import jwt
import datetime
import re
from fastapi import HTTPException
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

def create_jwt_token(payload, secret_key, expiration_time_minutes):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_time_minutes)
    payload['exp'] = expiration_time
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def encrypt_jwt(payload, secret_key):
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def verify_jwt(token, secret_key):
    try:
        decoded = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token not valid")

def verify_regular_expression(params):
    result = False
    for param in params:
        allow_charactors = re.search("^[a-zA-Z0-9_]*$", str(param))
        result = allow_charactors

    return result

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")



