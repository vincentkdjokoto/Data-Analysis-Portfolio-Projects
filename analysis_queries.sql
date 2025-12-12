-- Monthly Sales Analysis
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS unique_customers,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value
FROM orders
WHERE order_status != 'Cancelled'
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month DESC;

-- Top Products by Revenue
SELECT 
    p.product_name,
    p.category,
    COUNT(DISTINCT oi.order_id) AS orders_count,
    SUM(oi.quantity) AS total_units_sold,
    SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY total_revenue DESC
LIMIT 20;

-- Customer Lifetime Value
SELECT 
    c.customer_name,
    c.email,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(o.total_amount) AS lifetime_value,
    AVG(o.total_amount) AS avg_order_value
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_status != 'Cancelled'
GROUP BY c.customer_id, c.customer_name, c.email
ORDER BY lifetime_value DESC;
