--https://www.codewars.com/kata/589cf45835f99b2909000115/train/sql
SELECT
  created_at :: date AS date,
  count(*) AS count,
  (
    SUM(count(*)) OVER(
      ORDER BY
        created_at :: date
    )
  ) :: integer AS total
FROM
  posts
GROUP BY
  date
ORDER BY
  date;