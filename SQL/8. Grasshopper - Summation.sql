-- https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/sql
/*
 Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
 */
SELECT n,
    n *(n + 1) / 2 as res
FROM kata;

--

SELECT 
  n,
  (SELECT SUM(range) FROM generate_series(1, n) as t(range)) as res
FROM kata;

--

CREATE OR REPLACE FUNCTION summation(num INTEGER)
RETURNS INTEGER AS $$
DECLARE
  i INTEGER := 1;
  total INTEGER := 0;
BEGIN
  WHILE i <= num LOOP
    total := total + i;
    i := i + 1;
  END LOOP;
  RETURN total;
END;
$$ LANGUAGE plpgsql;


select n, summation(n) as res
from kata;