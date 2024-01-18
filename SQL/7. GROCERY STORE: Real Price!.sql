-- https://www.codewars.com/kata/5a8f00745084d718940000c5/train/sql
-- Make a SELECT query which will tell the price per kg of the product.

SELECT name,
    weight,
    price,
    ROUND((price * 1000 / weight)::numeric, 2)::float AS "price_per_kg"
FROM pro
ORDER BY price_per_kg,
    name;