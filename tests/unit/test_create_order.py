from src.application.use_cases.create_order import CreateOrderUseCase


class FakeRepository:
    def save(self, order):
        order.id = 1
        return order


def test_create_order():
    repo = FakeRepository()

    use_case = CreateOrderUseCase(repo)

    result = use_case.execute("Angie", 500)

    assert result.id == 1
    assert result.customer_name == "Angie"
