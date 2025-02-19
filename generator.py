import random
import datetime
from faker import Faker
from clickhouse_driver import Client

CLICKHOUSE_HOST = "localhost"
CLICKHOUSE_DB = "datamart_layer"
CLICKHOUSE_USER = "admin"
CLICKHOUSE_PASSWORD = "admin"
NUM_RECORDS = 1000  

client = Client(host=CLICKHOUSE_HOST, database=CLICKHOUSE_DB, user="admin", password="admin")

fake = Faker()

products = [
    (i, fake.word().capitalize(), random.choice(["Electronics", "Home Appliances", "Furniture"]), 
     round(random.uniform(50, 2000), 2), random.randint(10, 200))
    for i in range(1, NUM_RECORDS + 1)
]

customers = [
    (i, fake.first_name(), fake.last_name(), fake.email(), fake.phone_number(), fake.country())
    for i in range(1, NUM_RECORDS + 1)
]

orders = [
    (i, random.randint(1, NUM_RECORDS), fake.date_time_between(start_date="-1y", end_date="now"),
     round(random.uniform(50, 5000), 2), random.choice(["pending", "shipped", "delivered", "canceled"]))
    for i in range(1, NUM_RECORDS + 1)
]

payments = [
    (i, i, fake.date_time_between(start_date="-1y", end_date="now"),
     random.choice(["Credit Card", "PayPal", "Bank Transfer", "Crypto"]),
     round(random.uniform(50, 5000), 2))
    for i in range(1, NUM_RECORDS + 1)
]

supplies = [
    (i, random.randint(1, NUM_RECORDS), random.randint(10, 200),
     fake.date_time_between(start_date="-2y", end_date="now"), fake.company())
    for i in range(1, NUM_RECORDS + 1)
]

def insert_data(table, columns, data):
    query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES"
    client.execute(query, data)

tables = ["supplies", "payments", "orders", "customers", "products"]
for table in tables:
    client.execute(f"TRUNCATE TABLE {table}")

insert_data(f"{CLICKHOUSE_DB}.products", ["product_id", "product_name", "category", "price", "available_stock"], products)
insert_data(f"{CLICKHOUSE_DB}.customers", ["customer_id", "first_name", "last_name", "email", "phone", "country"], customers)
insert_data(f"{CLICKHOUSE_DB}.orders", ["order_id", "customer_id", "order_date", "total_amount", "status"], orders)
insert_data(f"{CLICKHOUSE_DB}.payments", ["payment_id", "order_id", "payment_date", "payment_method", "payment_amount"], payments)
insert_data(f"{CLICKHOUSE_DB}.supplies", ["supply_id", "product_id", "quantity", "supply_date", "supplier"], supplies)

print(f"{NUM_RECORDS} records was downloaded to clickhouse!")