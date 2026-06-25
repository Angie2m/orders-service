from fastapi import APIRouter, Depends

from src.interfaces.api.dependencies import get_create_order_use_case, get_current_user
from src.interfaces.api.schemas import CreateOrderRequest

router = APIRouter()


@router.post("/orders")
def create_order(
    request: CreateOrderRequest,
    use_case=Depends(get_create_order_use_case),
    current_user: str = Depends(get_current_user),  #
):
    # Solo llega aquí si el token es válido
    return use_case.execute(request.customer_name, request.total)
