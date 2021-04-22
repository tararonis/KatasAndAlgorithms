--https://www.codewars.com/kata/5abcf0f930488ff1a6000b66/sql
SELECT
  *
FROM
  students
WHERE
  (
    (
      quality1 = 'evil'
      AND quality2 = 'cunning'
    )
    OR (
      quality1 = 'cunning'
      AND quality2 = 'evil'
    )
  )
  OR (
    quality1 = 'brave'
    AND quality2 != 'evil'
  )
  OR (
    quality1 = 'studious'
    OR quality2 = 'intelligent'
  )
  OR (
    quality1 = 'hufflepuff'
    OR quality2 = 'hufflepuff'
  )


SELECT * FROM students
WHERE quality1 IN ( 'hufflepuff', 'studious') 
OR quality2 IN ( 'hufflepuff', 'intelligent') 
OR (quality1 = 'evil' AND quality2 = 'cunning')
OR (quality1 = 'brave' AND quality2 != 'evil')