from employee import Employee
from manager import Manager
from engineer import Engineer

# Creating objects
emp1 = Employee("John Doe", 1001, 20) # Hourly rate $20
mgr1 = Manager("Jane Smith", 2001, 40, "Engineering") # $40 hourly rate
eng1 = Engineer("Alice Johnson", 3001, 30, "Development") # $30 hourly rate

# Defining hours worked
emp1.set_hours_worked(160) # 160 hours worked in the month
mgr1.set_hours_worked(160)
eng1.set_hours_worked(160)

# Using methods
emp1.set_name("John Wick")
print(emp1.get_name())

# Polymorphism and salary calculation
employees = [emp1, mgr1, eng1]
for emp in employees:
     print(f"Salary of {emp.get_name()} ({emp.__class__.__name__}): ${emp.calculate_salary()}")

'''   ########################################################################
from product import Product
from stock import Stock

# Create products
product1 = Product("Shirt", 59.90, "Men's cotton shirt", 10)
product2 = Product("Pants", 79.90, "Men's jeans", 5)

# Create stock
stock = Stock()

# Add products to stock
stock.add_product(product1)
stock.add_product(product2)

# Search product by name
product_searched = stock.search_product("Shirt")
if product_searched:
     print(f"Product found: {product_searched.name}")
else:
     print("Product not found")

# Apply discount to a product
product1.apply_discount(0.10)
print(f"Final price of product {product1.name}: R$ {product1.get_price_final():.2f}")
'''