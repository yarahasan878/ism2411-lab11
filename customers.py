## Customer.py
# Author: Yara Hasan
# Module 11 lab: Customer Dic

# Reflection 1:
# I would use .get() when I am not sure if a key exists.
# I would use brackets when I know the key is there.
# My rule is to use .get() to avoid errors.

# Reflection 2:
# This reminds me of PivotTables in Excel because both
# summarize data by categories. Python is more useful
# for large datasets because it can automate calculations
# and process a lot of data quickly.

print("---Exersice 1---")
customer = {
    "name": "alice",
    "Name": "Name-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("Hello, I'm John.")

print("---Exersice 2---")
customer['Phone'] = '555-5555'
print(customer)
customer['tier'] = 'Platinum'
print(customer)
del customer['Name']
print(customer)

print(customer.get('ytd_spend', 0))



print("---Exersice 3---")
print(customer.get("email", "no email on file"))

#try:
 #   print(customer["email"])
#except KeyError as error:
 #   print("KeyError caught:", error)

print("---Exersice 4---")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(key)


print("---Exersice 5---")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"],0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print("---Exersice 6---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purshas")


print("---Exersice 7---")
catalog= {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")

print("---Exersice 8---")
transaction = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}
for sale in transaction:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
