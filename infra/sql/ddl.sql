CREATE TABLE IF NOT EXISTS datamart_layer.supplies
(
    supply_id UInt32,
    product_id UInt32,
    quantity UInt32,
    supply_date DateTime DEFAULT now(),
    supplier String
) ENGINE = MergeTree()
ORDER BY supply_id;

CREATE TABLE IF NOT EXISTS datamart_layer.payments
(
    payment_id UInt32,
    order_id UInt32,
    payment_date DateTime DEFAULT now(),
    payment_method String,
    payment_amount Float64
) ENGINE = MergeTree()
ORDER BY payment_id;

CREATE TABLE IF NOT EXISTS datamart_layer.orders
(
    order_id UInt32,
    customer_id UInt32,
    order_date DateTime DEFAULT now(),
    total_amount Float64,
    status Enum8('pending' = 1, 'shipped' = 2, 'delivered' = 3, 'canceled' = 4)
) ENGINE = MergeTree()
ORDER BY order_id;

CREATE TABLE IF NOT EXISTS datamart_layer.customers
(
    customer_id UInt32,
    first_name String,
    last_name String,
    email String,
    phone String,
    registration_date DateTime DEFAULT now(),
    country String
) ENGINE = MergeTree()
ORDER BY customer_id;

CREATE TABLE IF NOT EXISTS datamart_layer.products
(
    product_id UInt32,
    product_name String,
    category String,
    price Float64,
    available_stock UInt32,
    created_at DateTime DEFAULT now()
) ENGINE = MergeTree()
ORDER BY product_id;
