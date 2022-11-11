
```sql
SECTION 2 Group By Statement 

GROUP BY:  allows us to aggregate columns per some category.  

(TAKE A LOOK BELLOW FOR MOST COMMON AGGREGATE FUNCTIONS)

Note: whenever your’re using  an aggregate function and a non aggregate function in the SELECT  clause you have to use  GROUP BY or youll get   an error

but when you use just an aggregate functions or a non aggregate functions by themself in the SELECT clause you dont have to use GROUP BY 

Ex: SELECT COUNT(title), AVG(rental_duration) FROM film 

here no need for GROUP BY coz the functions being used in the SELECT clause are both aggregate functions

Ex 2: SELECT customer_id, staff_id FROM payment

here no need for GROUP BY coz we havent used any aggregate function

Ex 3: SELECT store_id, customer_id FROM customer GROUP BY store_id , customer_id

here if i dont use group by it will work just fine But

if i use group by i gotta add both store_id and customer_id or i will get an error 

```sql
SELECT DISTINCT(customer_id) FROM payment

is the same as

SELECT customer_id FROM payment
GROUP BY customer_id

-- theyre both returning the distinct values from customer_id
```

```sql
Aggregation Function: the main idea is to take multiple function and return a single output

Most Common Aggregation Function:

- AVG() - returns average value
- COUNT() - returns number of values
- MAX() - returns max value
- MIN() - returns min value
- SUM() - returns the sum of all values

NOTE: Aggregation Function calls happen only in the SELECT or the HAVING clause.

( haven’t learned the HAVING clause yet)

Special Notes

AVG(): returns a floating point value many decimal places Ex(2.432343) 

You can use  ROUND() to specify precision after the decimal.

COUNT(): simply returns number of rows, so we just use COUNT(*)

Aggregation Function Notes

```sql
SELECT AVG(replacement_cost) FROM film
-- will return the avreage in replacement cost in deciaml point
-- 19.9840000000000000

-- using ROUND() we can round the decimal however we want Ex:
SELECT ROUND(AVG(replacement_cost) ) FROM film

-- this will round 19.9840000000000000 to 20
SELECT ROUND(AVG(replacement_cost), 2) FROM film

-- by adding 2 in the () now we can round with number after the decimal point
```

HAVING: clause allows us to filter after an aggregation has already taken place so after a GROUP BY clause

```sql
-- example

SELECT first_name, last_name, customer_id, address_id FROM customer
WHERE first_name LIKE 'E%'
GROUP BY first_name, last_name, customer_id
HAVING address_id < 500
ORDER BY address_id DESC
LIMIT 1
```

---
