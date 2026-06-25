from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from src.infrastructure.config import settings

# Imports de infraestructura y base de datos
from src.infrastructure.database.db import Base, engine

# Imports de la capa de interfaces (API)
from src.interfaces.api.order_controller import router
from src.interfaces.api.schemas import Token

# Inicialización de la base de datos (creación de tablas si no existen) [3]
Base.metadata.create_all(bind=engine)

# Instancia principal de la aplicación [3]
app = FastAPI(
    title="Orders API",
    description="Servicio de gestión de pedidos con Arquitectura Hexagonal y Seguridad JWT",
    version="1.0.0",
)


# --- Endpoint de Autenticación (Módulo de Seguridad) [1] ---
@app.post("/token", response_model=Token, tags=["Security"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para obtener el token de acceso JWT.
    Credenciales de laboratorio: admin / password123
    """
    # Validación simple de credenciales para el proyecto final [1]
    if form_data.username != "admin" or form_data.password != "password123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Generación del Token utilizando la configuración de infraestructura [4]
    access_token = jwt.encode(
        {"sub": form_data.username}, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )

    return {"access_token": access_token, "token_type": "bearer"}


# Inclusión de las rutas de negocio (Orders) [3]
app.include_router(router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "version": "1.0.0"}
