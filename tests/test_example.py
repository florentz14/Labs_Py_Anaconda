import pytest

from classes.models import Customer, Employee, Product, InvoiceLine, Invoice


def test_customer_email_validation():
    with pytest.raises(ValueError, match="Invalid email address"):
        Customer(1, "Ana", "anax.com", "Calle 1")


def test_employee_name_validation():
    with pytest.raises(ValueError, match="Employee first_name cannot be empty"):
        Employee(1, "", "Perez", "Ventas", "luis@x.com")


def test_product_validation():
    with pytest.raises(ValueError, match="Product price cannot be negative"):
        Product(1, "Lápiz", -1.0, stock=10)


def test_invoiceline_validation():
    p = Product(1, "Lápiz", 0.5, stock=100)
    with pytest.raises(ValueError, match="InvoiceLine quantity must be positive"):
        InvoiceLine(p, 0)


def test_invoice_workflow():
    c = Customer(1, "Ana", "ana@x.com", "Calle 1")
    e = Employee(1, "Luis", "Perez", "Ventas", "luis@x.com")
    p = Product(1, "Lápiz", 0.5, stock=100)
    inv = Invoice(1, c, e)

    inv.add_line(InvoiceLine(p, 10))

    assert inv.subtotal == 5.0
    assert inv.tax == pytest.approx(0.6)
    assert inv.total == pytest.approx(5.6)
    assert p.stock == 90

