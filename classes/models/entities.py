from dataclasses import dataclass, field
from datetime import date
from typing import List, ClassVar, Optional

from .validators import validate_email, validate_non_empty


@dataclass
class Customer:
    _id_counter: ClassVar[int] = 1
    id: Optional[int] = None
    name: str = ""
    email: str = ""
    address: str = ""

    def __post_init__(self):
        if self.id is None:
            self.id = Customer._id_counter
            Customer._id_counter += 1

        self.name = validate_non_empty(self.name, "Customer name")
        self.email = validate_email(self.email)
        self.address = self.address.strip()


@dataclass
class Employee:
    _id_counter: ClassVar[int] = 1
    id: Optional[int] = None
    first_name: str = ""
    last_name: str = ""
    role: str = ""
    email: str = ""

    def __post_init__(self):
        if self.id is None:
            self.id = Employee._id_counter
            Employee._id_counter += 1

        self.first_name = validate_non_empty(self.first_name, "Employee first_name")
        self.last_name = validate_non_empty(self.last_name, "Employee last_name")
        self.role = validate_non_empty(self.role, "Employee role")
        self.email = validate_email(self.email)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


@dataclass
class Product:
    _id_counter: ClassVar[int] = 1
    id: Optional[int] = None
    name: str = ""
    price: float = 0.0
    stock: int = 0

    def __post_init__(self):
        if self.id is None:
            self.id = Product._id_counter
            Product._id_counter += 1

        self.name = validate_non_empty(self.name, "Product name")
        if self.price < 0:
            raise ValueError("Product price cannot be negative")
        if self.stock < 0:
            raise ValueError("Product stock cannot be negative")

    def is_available(self) -> bool:
        return self.stock > 0


@dataclass
class InvoiceLine:
    product: Product
    quantity: int

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError("InvoiceLine quantity must be positive")
        if self.product is None:
            raise ValueError("InvoiceLine product cannot be None")

    @property
    def line_total(self) -> float:
        return self.product.price * self.quantity


@dataclass
class Invoice:
    _id_counter: ClassVar[int] = 1
    id: Optional[int] = None
    customer: Optional[Customer] = None
    employee: Optional[Employee] = None
    date: date = field(default_factory=date.today)
    lines: List[InvoiceLine] = field(default_factory=list)

    def __post_init__(self):
        if self.id is None:
            self.id = Invoice._id_counter
            Invoice._id_counter += 1

        if self.customer is None:
            raise ValueError("Invoice customer cannot be None")
        if self.employee is None:
            raise ValueError("Invoice employee cannot be None")

    @property
    def subtotal(self) -> float:
        return sum(line.line_total for line in self.lines)

    @property
    def tax(self) -> float:
        return self.subtotal * 0.12

    @property
    def total(self) -> float:
        return self.subtotal + self.tax

    def add_line(self, line: InvoiceLine):
        if not isinstance(line, InvoiceLine):
            raise TypeError("add_line expects InvoiceLine")
        if not line.product.is_available():
            raise ValueError("Product is not available")
        if line.quantity > line.product.stock:
            raise ValueError("Not enough stock for product")

        self.lines.append(line)
        line.product.stock -= line.quantity

    def remove_line(self, line: InvoiceLine):
        self.lines.remove(line)
        line.product.stock += line.quantity

