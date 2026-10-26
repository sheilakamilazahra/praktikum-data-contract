from datetime import datetime
from pydantic import ValidationError

from contract import OrderContract


# Data dengan field tambahan yang tidak ada di contract
invalid_order = {
    "order_id": "ORD-888",
    "customer_id": 888,
    "amount": 100000.0,
    "status": "PENDING",
    "transaction_date": datetime(2026, 9, 20, 10, 0),
    "payment_date": None,
    "unexpected_field": "ABC",
}


# Validasi data
try:
    order = OrderContract.model_validate(invalid_order)

    print("VALID")
    print(order)

except ValidationError as exc:
    print("INVALID")
    print(exc)