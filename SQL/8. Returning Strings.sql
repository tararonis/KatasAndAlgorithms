-- https://www.codewars.com/kata/55a70521798b14d4750000a4/train/sql
SELECT
  'Hello, ' || name || ' how are you doing today?' as greeting
FROM
  person


SELECT 
  FORMAT('Hello, %s how are you doing today?', name) as greeting
FROM 
  person