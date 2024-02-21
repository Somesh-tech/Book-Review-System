from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pwd(password):
    if password:
        return pwd_context.hash(password)
    else:
        raise Exception("The password cannot be Empty !")
    
def verify_pwd(provided_pwd, hashed_pwd):
    return pwd_context.verify(provided_pwd,hashed_pwd)