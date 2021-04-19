--https://www.codewars.com/kata/5ad90fb688a0b74111000055/train/sql
SELECT
  (
    INITCAP("firstname") || ' ' || INITCAP("lastname")
  ) AS shortlist
FROM
  elves
WHERE
  firstname ILIKE '%tegil%'
  OR lastname ILIKE '%astar%'
