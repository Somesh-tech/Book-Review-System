from jose import JWTError, jwt
from datetime import datetime, timedelta
from db_conn import schemas
from fastapi import  Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

# oauth_schema = OAuth2AuthorizationCodeBearer(tokenUrl='login')
# Token has three parts:
# 1) Header -> contains the algo for the token generation.
# 2) Signature -> contains secret key
# 3) Expiration Time.

oauth_scehma = OAuth2PasswordBearer(tokenUrl="login")

# to create random key use "openssl rand -hex 32" in git bash.
Secret_key = "9a865d28620664a7e5799a9b7ff975364151d2621926c69f6422643d84e13294"
exp_time_in_minutes = 1
Algo = "HS256"

def generate_token(data : dict):
    
    data_to_encode = data.copy()

    expiration_time = datetime.utcnow() + timedelta(minutes=exp_time_in_minutes)

    data_to_encode.update({"exp_time" : expiration_time.isoformat()})

    encoded_data = jwt.encode(data_to_encode, Secret_key, algorithm=Algo)

    return encoded_data

def verify_token(token : str, credentials_error):
    try:
        payload = jwt.decode(token, Secret_key, algorithms=[Algo])
        id : str = payload.get("user_id")

        if not id:
            raise credentials_error
        token_data = schemas.TokenData(id= id)
    except JWTError:
            raise credentials_error
    return token_data

def get_current_user(token:str = Depends(oauth_scehma)):
     
    credentials_error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "Invalid Credentials",
                                       headers={"WWW-Authenticate":"Bearer"})
    
    return verify_token(token, credentials_error)
