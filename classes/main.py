import csv
import sys
from datetime import date
from pathlib import Path

try:
    from tabulate import tabulate
except ImportError:
    tabulate = None

# Ensure the workspace root is on sys.path, para evitar "ModuleNotFoundError: No module named 'classes'"
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from classes.models import Customer, Employee, Product, InvoiceLine, Invoice

CSV_DIR = Path('data/csv')


def load_customers() -> dict[int, Customer]:
    path = CSV_DIR / 'customers.csv'
    customers = {}
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            c = Customer(
                id=int(row['id']),
                name=row['name'],
                email=row['email'],
                address=row.get('address', '') or ''
            )
            customers[c.id] = c
    return customers


def load_employees() -> dict[int, Employee]:
    path = CSV_DIR / 'employees.csv'
    employees = {}
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            e = Employee(
                id=int(row['id']),
                first_name=row['first_name'],
                last_name=row['last_name'],
                role=row['role'],
                email=row['email']
            )
            employees[e.id] = e
    return employees


def load_invoices(customers: dict[int, Customer], employees: dict[int, Employee]) -> dict[int, Invoice]:
    path = CSV_DIR / 'invoices.csv'
    invoices = {}
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cust = customers[int(row['customer_id'])]
            emp = employees[int(row['employee_id'])]
            inv = Invoice(
                id=int(row['id']),
                customer=cust,
                employee=emp,
                date=date.fromisoformat(row['date']) if row.get('date') else date.today()
            )
            invoices[inv.id] = inv
    return invoices


def load_invoice_lines(invoices: dict[int, Invoice], products: dict[int, Product]) -> None:
    path = CSV_DIR / 'invoices_line.csv'
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            invoice_id = int(row['invoice_id'])
            prod_id = int(row['product_id'])
            line = InvoiceLine(
                product=products[prod_id],
                quantity=int(row['quantity'])
            )
            invoices[invoice_id].add_line(line)


def load_products() -> dict[int, Product]:
    candidate_path = CSV_DIR / 'products.csv'
    if not candidate_path.exists():
        # Si no existe, crea con datos mínimos para el ejemplo
        default_products = {
            1: Product(id=1, name='Lápiz', price=0.5, stock=100),
            2: Product(id=2, name='Cuaderno', price=1.25, stock=50)
        }
        return default_products
    products = {}
    with candidate_path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            p = Product(
                id=int(row['id']),
                name=row['name'],
                price=float(row['price']),
                stock=int(row['stock'])
            )
            products[p.id] = p
    return products


def main() -> None:
    customers = load_customers()
    employees = load_employees()
    products = load_products()
    invoices = load_invoices(customers, employees)

    load_invoice_lines(invoices, products)

    for inv in invoices.values():
        print(f"Invoice {inv.id}")
        table_rows = []
        for line in inv.lines:
            table_rows.append([
                line.product.id,
                line.product.name,
                line.quantity,
                f"{line.product.price:.2f}",
                f"{line.line_total:.2f}"
            ])

        headers = ["Product ID", "Product", "Qty", "Unit Price", "Line Total"]
        if tabulate:
            print(tabulate(table_rows, headers=headers, tablefmt='grid'))
        else:
            print(headers)
            for row in table_rows:
                print(row)

        print(f"Subtotal: {inv.subtotal:.2f}")
        print(f"Tax (12%): {inv.tax:.2f}")
        print(f"Total: {inv.total:.2f}\n")


if __name__ == '__main__':
    main()