import bcrypt
from passlib.context import CryptContext

cripto = CryptContext(schemes=['bcrypt'])

def verify_password(password: str, hash_password) -> bool:
    teste= cripto.verify(password,hash_password)
    return teste

def generate_hash(password: str) -> str:
    return cripto.hash(password)