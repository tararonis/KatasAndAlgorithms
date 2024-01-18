-- https://www.codewars.com/kata/6433e30366f6ca752de24600/train/sql

/* 
Return the list of films that have not been rented out at all in the past month, but have been rented at least 10 times in total. Include the film_id, title of the film and in the brackets, its rating, rental count, and the date of the most recent rental. Since the business is in America, please use American date notation (for example, 'April 9, 2023').

Notes:
Sort by count of rented films from higher to lower. If two or more films have the same amount of rentals then sort by last rental date in descending order, if even last rental dates are the same - then by film title alphabetically.
"in the past month" - interval inclusive of 1 month from CURRENT_DATE. We are not taking time part of today into account for this task
"sort by last rental date" means by final text presentation, not the date itself.
Schema
inventory table:
Column       | Type      | Modifiers
------------ +-----------+----------
inventory_id | integer   | not null
film_id      | smallint  | not null
store_id     | smallint  | not null
film table:
Column           | Type     | Modifiers
-----------------+----------+----------
film_id          | integer  | not null
title            | varchar  | not null
description      | text     | not null
rating           | varchar  | not null
rental table:
Column       | Type      | Modifiers
-------------+-----------+----------
rental_id    | integer   | not null
customer_id  | integer   | not null
inventory_id | integer   | not null
rental_date  | timestamp | not null
return_date  | timestamp | 
Desired Output
The desired output should look like this:

film_id | film_title         | rental_count | last_rental_date
--------+----------------+------------------+------------------
   32   | Chinatown (G)      | 23           | January 31, 2023
   14   | The Terminator (R) | 17           | March 01, 2023
...
*/

SELECT 
  film_id,
  title || ' (' || rating || ')' as film_title,
  COUNT(*) as rental_count,
  to_char(max(rental_date), 'FMMonth DD, YYYY') as last_rental_date
FROM
  film
JOIN inventory using(film_id)
JOIN rental using(inventory_id)
GROUP BY film_id
HAVING COUNT(*) >= 10 AND max(rental_date) < current_date - interval '1' month
ORDER BY rental_count desc, last_rental_date desc, title;
