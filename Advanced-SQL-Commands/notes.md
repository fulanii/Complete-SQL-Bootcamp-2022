

``` sql
Timestamps and Extract - Part One: 

- TIME: Contains only time
- DATE: Contains only date
- TIMESTAMP: Contains date and time
- TIMESTAMPTZ: Contains date, time, and timezone
- SHOW ALL: Show all the value of a run-time parameter (idk what it means/do)
- NOW:
- TIMEOFDAY:
- CURRENT_TIME:
- CURRENT_DATE:

```sql
SHOW ALL
-- will show all value of run time parameter

SHOW TIMEZONE
-- will show your computer timezone

SELECT NOW()
-- will give you timestanp with time zone information

SELECT CURRENT_TIME
-- will give you time with timezone

SELECT CURRENT_DATE: will give u date yyyy-mm-dd
```

---

Timestamps and Extract - Part Two: 

EXTRACT(): allows you to extract or obtain a sub-component of a date value  

- year
- month
- day
- week
- quater
- Ex:  EXTRACT(YEAR FROM date_col)

AGE(): Calculates and returns the current age given a timestamp 

- Ex: AGE(date_col)
- Ex of output: 13 years 1mon 5 days 01:03:13.003423

TO_CHAR(): general function to convert data types to text 

- Ex: TO_CHAR(date_col, ‘mm-dd-yyyy’)
- requries to argument 1) expression 2) format for the result in string

```sql
-- Code Examples

SELECT EXTRACT(YEAR FROM payment_date) AS year FROM payment
-- this code will return all the years from a time stamp 
-- ( u can extract year, month and day)

SELECT AGE(payment_date) FROM payment
-- this code will tell u the age since date
-- ex: if the payment_date was 2003 and i did AGE(payment_date) in 2022
-- AGE will be 19

SELECT TO_CHAR(payment_date, 'Month-YYYY') FROM payment
-- this query will take the payment_date which looks like this 
-- 2007-02-15 22:25:46.996577
-- and change it to string: February-2007
-- since i said 'Month-YYYY' i get the month with first letter capitalize
-- then a dash(-) then year 2007
-- Btw there many different way to change data stamp to string 
-- (check postgre docs) 
-- https://www.postgresql.org/docs/current/functions-formatting.html
```

Note: Just learned a new words TRIM() and DOW

TRIM: function is used to remove spaces or set of characters from the leading or trailing or both sides of a strin

```sql
Ex Trailing: SELECT TRIM(TRAILING 'M' FROM 'MADAM')
-- here the 'M' at the end will be remove and output = MADA

Ex Leading: SELECT TRIM(LEADING 'M' FROM 'MADAM')
-- here the 'M' at the begening will be remove and output = ADAM

Ex Both: SELECT TRIM(BOTH 'M' FROM 'MADAM')
-- here the 'M' at the begening and end will be remove and output = ADA

Ex Not specific: SELECT TRIM('M' FROM 'MADAM')
-- this will remove all the 'M' character from the word 'MADAM'
-- and output will be = ADA

Ex: SELECT TRIM('MADAM')
-- this will simply remove white spaces and return character output = MADAM
-- sometimes some fuction returns strings with some spaces u can or cant see
-- so use = so check if the same may not work coz of spaces so u cam trim it :)
```

DOW:  Means day of the week

---

Mathematical Functions and operators:  No need to go trough all of them there’s big and details documentation likn bellow incase you ever need to use them

[https://www.postgresql.org/docs/9.5/functions-math.html](https://www.postgresql.org/docs/9.5/functions-math.html)

---

String Function and Operators:  No need to go trough all of them there’s big and details documentation link bellow incase you ever need to use them but we’ll be taking a look at a couple

[https://www.postgresql.org/docs/9.1/functions-string.html](https://www.postgresql.org/docs/9.1/functions-string.html)

```sql
1 -- how to concatenate strings lets suppose first_name = mike last_name = ju
SELECT first_name || last_name FROM customer
-- and out put will be mikeju 

2 -- notice how theres no space this how you add it 
SELECT first_name || ' ' || last_name FROM customer
-- out put will be mike ju the empty quotes is blank space

3 -- u can upper case a string using the upper() funtion
SELECT UPPER(first_name) FROM customer
-- output = MIKE

4 -- u cam lower case a string usng the lower() function
SELECT LOWER(first_name) FROM customer
-- output = mike

5 -- you can grap a certain number of character from a string using left() function
SELECT LEFT(first_name, 1) from customer
-- the 1 tells us to grap the 1st word/character from the first_name
-- output will be m
```

---

Sub Query: allows you to construct complex queries, essentially performing a query on top of another query 

```sql
/*
-- Tip 
	1 sub query run first

	2 if your sub query returns multiple values you need to use the IN operator

	3 EXIST: operator is a boolean operator that tests for existence 
					 of rows in a subquery. returns (True or False)
*/
-- 1 Ex:
SELECT * FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film)
-- so here the avg rental_rate get returns first 
-- then were selecting everything from film where
-- rental_rate is > than the avg rental_rate

-- 2 Ex:
SELECT first_name FROM customer
WHERE customer_id IN 
(SELECT customer_id FROM rental  
WHERE return_date BETWEEN '2005-01-01' AND '2006-01-01')
-- above we will get a list of customer_id that returned their rental
-- between the dates above so we have to use the IN operator
-- after we get the list then we slect all the customer first_name
-- from the customer table that have their customer-id in that list

-- 3 Ex: 
SELECT * FROM customer
WHERE EXISTS (SELECT customer_id FROM payment )
-- here i will get a list of customer_id returned from the sub query
-- if anything is returned from the sub query even one row then EXISTS is TRUE
-- then SELECT * FROM customer will be executed
-- but if nothing is returned from the sub query EXISTS is false
-- so SELECT * FROM customer will not be executed

```

---

Self-Join: is a query in which a table is joined to itself

```sql
-- self join can viewd as a join of two copies of the same table 
-- The table is not actually copied, but SQL performs the command as it were.

--Syntax
	SELECT tableA.col, tableB.col 
	FROM table AS tableA 
	JOIN table AS tableB 
	ON tableA.some_col = tableB.other_col
```

Self-Join details explanation: 

let’s say we have a table with employee name, emp_id  and report_id which is basically the id of employee other employee  have to report too so emp_id

employee tab

Now lets say instead of repot_id we want the name of the employee and the name of who they have to report to in a table. And since it’s in one table we can do a self join to get that

And how u ask? well since the report_id is basically the emp_id of employee other employee have to report too

Ex: code bellow

```sql
SELECT emp.name, report.name
FROM employee AS emp -- emp is an allias of the employee table to not mix stuff
JOIN employee AS report -- report too is an allias of the employee table to not mix stuff
ON emp.emp_id = report.report_id 
-- above we got the 2 different allias of the same table to get 2 diff columns

-- Btw (allias r require) to organize and not mix shit up
```

This will be the output:
| name | rep (the name who each employee reports too) |
| --- | --- |
| Andrew | Charlie |
| Bob | Charlie |
| Charlie | David |
| David | Andrew |

```