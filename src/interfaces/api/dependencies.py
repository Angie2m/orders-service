from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from src.application.use_cases.create_order import CreateOrderUseCase
from src.infrastructure.config import settings
from src.infrastructure.database.db import SessionLocal
from src.infrastructure.repositories.sqlalchemy_order_repository import (
    SQLAlchemyOrderRepository,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_create_order_use_case():
    db = SessionLocal()

    repo = SQLAlchemyOrderRepository(db)

    return CreateOrderUseCase(repo)


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username = payload.get("sub")  # Obtenemos el valor como 'Any' inicialmente
        if username is None or not isinstance(username, str):
            raise credentials_exception  # Si es None o no es string, lanzamos error
        return username
    except JWTError:
        raise credentials_exception
