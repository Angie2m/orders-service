from pydantic import BaseModel


class CreateOrderRequest(BaseModel):
    customer_name: str
    total: float


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    total: float


class Token(BaseModel):
    access_token: str
    token_type: str


class UserLogin(BaseModel):
    username: str
    password: str
