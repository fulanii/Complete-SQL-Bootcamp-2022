

# SECTION 1 SQL Statement and Fundamentals

# SQL Keywords: definition & examples

SQL stands for Structured Query Language lets you access and manipulate databases. SQL keywords are usually capitalize but that’s not require.
SELECT: is used to retrieve data from a table 

```sql
SELECT * FROM film; 
* means all
```

Table 1 

| column_1 | column_2 | column_3 |
| --- | --- | --- |
| a | 1 | 20 |
| b | 2 | 21 |
| c | 3 | 22 |

Table 2

| column_1 | column_2 | column_3 |
| --- | --- | --- |
| d | 4 | 30 |
| e | 5 | 31 |
| f | 6 | 32 |

Above is an example of table in SQL

SELECT column_1 From Table 1 this query will output all the data under column_1 from table 1 which are: a, b, c

To select multiple columns you separate the columns name by a common: SELECT column_1, column_2 From Table 1 ( doesn’t have to be in order EX: SELECT column_1, column_3 From Table 1  )

To select all the element from the table you use the asterisk * symbol EX:  SELECT * From Table 1 (will select everything from the table ) 

Tip: it’s not good practice to use  the asterisk * symbol in SELECT if you don’t need all the columns using it will query everything which increase database traffic and slow down the app

---

DISTINCT: keyword is used with the SELECT keyword to return only distinct values when you have duplicate values

```sql
SELECT DISTINCT column FROM table
```

To clarify which column DISTINCT is being used on you can also use parenthesis for clarity (not require) ex bellow: 

```sql
SELECT DISTINCT (column_1) FROM table
```

EX: bellow we have a table with duplicates we can use the DISTINC

 keyword to only return distinct values

name_age_table

| Name | Age |
| --- | --- |
| Zach | 18 |
| David | 20 |
| Claire | 30 |
| David | 40 |

```sql
SELECT DISTINCT Name FROM name_age_table
```

after running the code above we get this only distinct values without the duplicates

| Name |
| --- |
| Zach |
| David |
| Claire |

---

COUNT:  function return the number of  rows that match a specific condition of a query ex bellow:

name_age_table

| Name | Age |
| --- | --- |
| Zach | 18 |
| David | 20 |
| Claire | 30 |
| David | 40 |

```sql
SELECT COUNT(Name) FROM name_age_table
```

this query will return 4 because there’s 4 names(rows) in the Name column Note: the parenthesis are required for COUNT 

Challenge: count how many distinct name there is in the table bellow

name_age_table

| Name | Age |
| --- | --- |
| Zach | 18 |
| David | 20 |
| Claire | 30 |
| David | 40 |

```sql
SELECT COUNT(DISTINCT Name) FROM name_age_table
// here (DISTINCT Name) will be executed first then COUNT  
```

the query above will return 3 because there’s there’s 3 unique names in the table above 

name_age_table  

| Name | Age |
| --- | --- |
| Zach | 18 |
| David | 20 |
| Claire | 30 |

---

SELECT and WHERE: the WHERE statement allows us to specify conditions on columns for the rows to be returned

Basic syntax example:

SELECT column1, column2 from table WHERE conditions;

WHERE appears immediately after the FROM clause of the SELECT statement 

The conditions are used to filter the rows returned from the SELECT statement

Ex of conditions: is the price greater than $3.00?, is name equal to “Yassine”?

Ex of query: SELECT column1 from table WHERE the price greater than $3.00

Comparison Operators: allows to compare value to something

| operator | Description |
| --- | --- |
| = | Equal |
| >  | Greater Than |
| < | Less Than |
| >= | Greater or Equal to |
| <= | Less or Equal to |
| <> or != | Not Equal to |

Ex using Comparison Operators: 

SELECT Name,Age FROM name_age_table WHERE Name = ‘David’ 

this will output: David 20

(PostgreSQL uses single quotes for strings, remember spelling and case sensitive  ) 

Logical Operators

Allow us to compare multiple comparison operators 

AND

OR

NOT

Ex using Logical Operators: 

SELECT Name,Age FROM name_age_table WHERE Name = ‘David’ and Age = ‘18’

this will output: David 18 

---

ORDER BY:  is used to sort rows based on a column value, in either ascending or depending order. ( alphabetical for string columns or numerical for numeric columns)

syntax: ASC means ascending and DESC means descending  

Ex: SELECT column_1, column_2  From table ORDER BY column_1 ASC/DESC

( above pick either ASC or DESC if left blank ORDER BY uses ASC)

LIMIT: the limit command allows us to limit the number of rows returned for a query.

Syntax: For the LIMIT keyword you use number to tell it how many rows to return if you dont     want all the rows to be returned

Ex: 

```sql
SELECT * FROM payment
ORDER BY payment_date
LIMIT 10;
-- this will return payment_date order by asc order and first 10 rows
```

BETWEEN: operator can be used to match a value against a range of values BETWEEN low and high

```sql
SELECT * FROM payment
WHERE amount BETWEEN 0 and 1
LIMIT 20;
// this will out put all 20 payment where amount is between 0 and 1
```

IN: We can use the IN operator to create a condition that checks to see if a value is
included in a list of multiple options. Note IN (requires parenthesis) 

```sql
SELECT * FROM customer
WHERE first_name IN ('John')
```

LIKE:  operator allows us to perform pattern matching against string data with the use of wildcard characters: ( Case sensitive )

percent % 

Matches any sequence of characters after or before it the size or length doesn't matter 

Ex: WHERE name LIKE  ‘A%’  means all names that begin with an capital ‘A’

Ex: WHERE name LIKE  ‘%a’  means all names that end with an lower ‘a’

Underscore _

Matches any single character basically the _ can be replace by any single character, let’s say we have game 1, game 2, game 10 etc in our db _ can be replace by any single character ex: 1 or maybe 2 etc

Note you can use multiple _ underscores if you want it to be replace with more than 1 single character. 

Ex: WHERE title LIKE ‘Game _’ (single characters) 

Ex: WHERE title LIKE ‘Game _ _’ (multiple characters) 

Complex Matching: matching operators to create more complex patters

Ex:

```sql
-- Cheryl
-- Theresa
-- Sherri

WHERE name LIKE '_her%'

-- Cheryl
-- Theresa
-- Sherri

-- so using the code above the first _ (underderscore) can only be replace  
-- with a 1 single character

-- but the % (percent) can be replace with any number of characters

-- so this is how it will work the single character for the _ underscore 
-- in red (C T and S)

-- and after her any sequence of character for the % percent
-- in green yl, esa and ri

```

ILIKE: is the same as LIKE but not case sensitive but LIKE case sensitive 

---

---

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

---

SECTION 3 JOINS

JOINS: will allow us to combine information from multiple tables together, there’s a couple different join types and the main difference between them is to decide how to deal with information only present in one of them

AS: clause allows us to create an “alias” for a column or results 

Ex: SELECT f_name AS first_name FROM customer

as you can see i selected a column f_name in a table customer and gave it a new name first_name

Ex 2: SELECT SUM(amount) AS total FROM customer

we can use this on fuctions on a column, now SUM(amount) will be total

Note: the AS operator gets executed at the end of a query meaning we can not used it in some query. Can only in the SELECT statment anywhere else will be invalid  

```sql
-- AS code example
--code example
SELECT store_id AS store_identifier FROM customer

The output of the store_id column name will now be store_identifier
```

INNER JOINS: will result with the set of records that match in both tables

Ex: lets imagine we have a registration table (left) and login table (right) the reg_id shows us in what order the register in and the log_id shows us in what ordered the login 

| reg_id | name |
| --- | --- |
| 1 | Andrew |
| 2 | Bob |
| 3 | Charlie |
| 4 | David |

| log_id | name |
| --- | --- |
| 1 | Xavier |
| 2 | Andrew |
| 3 | Yolanda |
| 4 |  Bob |

Now lets say we want to see the people who register and login we can use inner join to do this

```sql
SELECT * FROM registration INNER JOIN login ON registration.name = login.name

-- here were saying where do we have in match 
-- registration(table) in name(column) and login(table) in name(column)

-- Btw registration.name and login.name are basically 
-- the table name dot(.) the column name

```

So this will be the output

| reg_id | name | login_id | name |
| --- | --- | --- | --- |
| 1 | Andrew | 2 | Andrew |
| 2 | Bob | 4 | Bob |

Note: since we said SELECT * in the query above we get duplicated name coz there name in both tables

```sql
SELECT reg_id, login.name, login_id, log_id FROM registration
INNER JOIN LOGINS ON registration.name = login.name

-- i think login.name can be switch around with registration.name 
-- sice the name are all the same 
-- (not sure to look on too)
```

| reg_id | name | login_id |
| --- | --- | --- |
| 1 | Andrew | 2 |
| 2 | Bob | 4 |

## More example of inner join

```sql
SELECT payment_id, payment.customer_id, first_name FROM payment
INNER JOIN customer
ON payment.customer_id = customer.customer_id

/* 
1 selecting payment_id from the payment table 
	(if your refering to a column that can only be found in one the table 
	 you're joining no need to specify sql knows where its coming from)
	 
2 selecting customer_id from the payment table
	(since customer_id can be found in multiple tables we need to specify
	which table customer_id column we want here were getting the one from
	the payment table so we do payment.customer_id)
	
3 selecting first_name from the customer table
	( since first_name is unique to the customer table no need to specify)

4 then i do INNER JOIN the customer table which basically get us matching records 
  from both tables
  	(So the result will give us a new table that joins customer only found in 
	the payment and customer tables)

SO GENERAL SYNTAX 

	SELECT columns 
  FROM table_a 
	INNER JOIN table_b 
	ON table_a.identifying column = table_b.identifying
		
						( = basically means find all the mathing records )
*/

-- NOTE: for inner join the order doesnt really matter 
-- the table(name) after the FROM and table(name) 
-- after INNER JOIN can be switch up (just name shit properly) 
```

Note Tip: just came across this while doing research to learn will be helpful in the future

```sql
SELECT payment_id, first_name FROM payment p
INNER JOIN customer c
ON p.customer_id = c.customer_id

-- so just found out i can use allias like this without using 
AS -- work well with JOINs and some other statment and clause.
```

---

OUTER JOIN: allows to specify on how to deal with values only present in one of the table being join. There’s a couple of different type of outer join its prettry complex so take your time.

FULL OUTER JOIN: is basically the opposite of INNER JOIN, FULL OUTER JOIN returns results that includes unmatched rows in both tables. Where as an  INNER JOIN only returns the matching rows in a tables.

If the rows in the joined table do not match, the full outer join sets NULL values for every column of the table that does not have the matching row.

customer

| customer_id | Name |
| --- | --- |
| 1 | Yassine |
| 2 | Yasser |
| 3 | John |
| 4 | Mike |

payment

| payment_id | Name |
| --- | --- |
| 1 | Yasser |
| 2 | Mike |
| 3 | Yassine |
| 4 | Sam |

So above we have 2 table were using to pratice, the first one is the customer table and the second one is the payment table 

we can do a FULL OUTER JOIN to get all the matching results from both tables 

```sql
SELECT * FROM customer
FULL OUTER JOIN payment
ON customer.name = payment.name
```

and this what the output will be

| customer_id | Name | payment_id | Name |
| --- | --- | --- | --- |
| 1 | Yassine | 3 | Yassine |
| 2 | Yasser | 1 | Yasser |
| 3 | John | null | null |
| 4 | Mike | null | null |
| null | null | 2 | Mike |
| null | null | 4 | Sam |

So above by doing the name full outer join we match all the matching names and whenever the names dont match there’s null to say this name apper in one table put not both tables

ON customer.name = payment.name: is only checking for matching in the name column

we could actually do: ON customer.customer_id = payment.payment_id = that would check for matching ids from both ids columns

 by doing SELECT *  we selected all the columns that’s why name was repeated twice, we could’ve done “SELECT [payment.name](http://payment.name), [customer.name](http://customer.name)  FROM customer” doing that would’ve only showed the 2 names columns

The reason why we have the full outer join output table like that is coz postgreSQL took the customer table then the payment table and started matching them then whenever a column doesnt match postgreSQL add null then move on 

so first 2 customer names have a match postgreSQL add them 

then last 2 customer names dont have matches in the payment table names so postgreSQL add null so forth etc..

---

LEFT OUTER JOIN: results in the set of records that are in the left table, if there is no match with the right table, the results are null

```sql
SELECT * FROM tableA LEFT OUTER JOIN tableB
ON tableA.col_match = tableB.col_match

-- so here tableA is the left table 
-- this will return everything from tableA even if its unique to tableA
-- then it will return the mathches tableB has with tableA
-- but will not return anything thats unique to tableB
-- LEFT OUTER JOIN can be shorten to LEFT JOIN

-- btw the order matter coz we have to specify the left table and the left table
-- is the first to come after FROM 

LEFT OUTER JOIN =
-- return everyting exculsive to tableA or can be found in both tableA and 
-- tableB but dont return anything exulsive to tableB

```

so here i have 2 table customer and payment

| customer_id | Name |
| --- | --- |
| 1 | Yassine |
| 2 | Yasser |
| 3 | John |
| 4 | Mike |

| payment_id | Name |
| --- | --- |
| 1 | Yasser |
| 2 | Mike |
| 3 | Yassine |
| 4 | Sam |

```sql
SELECT * FROM customer
LEFT OUTER JOIN payment
ON customer.name = payment.name

-- so here the customer table is the left table aka tableA
-- were grabing everithng from tableA and mathing tableA has with tableB
-- but nothing unique to tableB 
```

This is the output 

| customer_id | Name | payment_id | Name |
| --- | --- | --- | --- |
| 1 | Yassine | 3 | Yassine |
| 2 | Yasser | 1 | Yasser |
| 3 | John | null | null |
| 4 | Mike | null | null |

```sql
SELECT * FROM customer
LEFT OUTER JOIN payment
ON customer.name = payment.name
WHERE payment.name IS null

-- using WHERE payment.name IS null: i can get evrything unique to tableA

-- if payment.name is null
-- in LEFT OUTER JOIN that means 
-- its unique to the other table in this case the left table, tableA 
-- aka customer table
```

This is the output of the code above

| customer_id | Name | payment_id | Name |
| --- | --- | --- | --- |
| 3 | John | null | null |
| 4 | Mike | null | null |

```sql
-- This explains LEFT JOIN VERY WELL

SELECT customer.customer_id, payment.customer_id FROM customer
LEFT OUTER JOIN payment
ON customer.customer_id = payment.customer_id
WHERE payment.customer_id IS null

/*(left table comes first after the FROM clause so the customer table is the left table)

Btw LEFT OUTER JOIN is same as LEFT JOIN

So here i SELECTED customer_id FROM customer table
and customer_id FROM payment table and did a LEFT JOIN

postgreSQL took everything(meaning everything unique to the column or no) 
from the customer_id column within the customer table

Then postgreSQL took only the matching stuff payment.customer_id has
with customer.customer_id and returned it 

so if there anything in the  customer.customer_id(left table) 
that's not in the payment.customer_id(payment table) 

PostgreSQL returns null

So everything we selected from the left table will be shown
if there's maches in the second table it will be shown
but is its unique to the second table it will not be shown

Btw the WHERE clause can be use to father narow out results

*/
Ex: using this: WHERE customer.customer_id IS null

so here using WHERE payment.customer_id IS null postgreSQL will return
everything unique to the customer table since that mean there's no match
for it in the 2nd table(payment table)

	To simplify if its null in the second table its unique to the left table
	meaning it only exist in the left table 
	(keep in mind if it only exist in the second table in a left join it wont 
	( be included anyway 

-- TABLES BELLOW TO HELP U VISUALIZE 

-- For middle table (customer_id is left)
SELECT customer.customer_id, payment.customer_id FROM customer
LEFT OUTER JOIN payment
ON customer.customer_id = payment.customer_id

-- And this for last table
WHERE payment.customer_id IS null
```

| customer_id |
| --- |
| 1 |
| 2 |
| 3 |
| 4 |

| payment_id |
| --- |
| 1 |
| 2 |
| 5 |
| 6 |

| customer_id | payment_id |
| --- | --- |
| 1 | 1 |
| 2 | 2 |
| 3 | null |
| 4 | null |

| customer_id | payment_id |
| --- | --- |
| 3 | null |
| 4 | null |

---

RIGHT JOINS: is literally basically the same as left join but with switch tables smh!!

```sql
SELECT * FROM TableA -- this table is the left table
RIGHT OUTER JOIN TableB -- this table is the right table
ON TableA.col_match = TableB.col_match

-- code above means return back all rows that's unique to TableB 
-- or can be found in TableB and TableA 
-- Bit do not return rows that can only be found in TableA

IN RIGHT OUTER JOIN -- the second table is the right table
```

---

UNION: operator is used to combine the result-set of two or more SELECT statements 

Sales_Q1                                                                         Sales_Q2

| name | amount |
| --- | --- |
| david | 100 |
| claire | 50 |

| name | amount |
| --- | --- |
| david | 200 |
| claire | 100 |

```sql
SELECT * FROM Sales_Q1
UNION
SELECT * FROM Sales_Q2

```

this will be the output of the code above

| name | amount |
| --- | --- |
| david | 100 |
| claire | 50 |
| david | 200 |
| claire | 100 |

---

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

| emp_id | name | report_id (emp_id) |
| --- | --- | --- |
| 1 | Andrew | 3 |
| 2 | Bob | 3 |
| 3 | Charlie | 4 |
| 4 | David | 1 |

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

---

SECTION 8 Creating Databases abd Tables

1. Data types:  are just different types of data in SQL ex: bellow

Most Common Data Types

- Boolean: True or False
- Character: char, varchar, and text
- Numeric: integer and floating-point number
- Temporal: date, time, timestamp, and interval

Not as common Data Types

- UUID: universally unique identifiers
- Array: stores an array of strings, numbers etc ( like a python list )
- JSON:
- Hstore: store key value pair ( like a python dictionanry )
- Special types such as network address and geometric data

When creating databases and tables u should carefully consider which data types should be used for the data to be stored.

Always review documentation to see the data types limitation

[https://www.postgresql.org/docs/current/datatype.html](https://www.postgresql.org/docs/current/datatype.html)

When creating database and table, take your time to plan for long term storage Remember you can always remove historical information you've decided you aren't using, but you can't go back in time to add in information!

1. Primary Keys and Foreign Keys

Primary Keys: is a column or group of columns used to identify a row uniquely in a table

Ex: in the dvdrental database we have a unique, non-null customer_id column as the primary key. Unique mean it has to be distinct for every row and non-null mean there must be an entry and cant be empty.

Foreign Keys: is a field or group of fields in a table that uniquely identifies a row in another table.

A foreign key is defined in a table that references to the primary key of the other table.

The table that contains the foreign key is called referencing table or child table.
The table to which the foreign key references is called referenced table or parent table.
A table can have multiple foreign keys depending on its relationships with other tables.

1. Constraints: are like rules enforced on the data columns on table, these are used to prevent invalid data from being entered into our database. And it ensure accuracy and reliability of the database.

Contraints can be divided into two main categories 

1. Column Contraints
    - contrains the data in a column to adhere to certain conditions
2. Table Constraints
    - applied to the entire table rather than to an individual column

Ex of most common contraints used 

- NOT NULL constraint: ensures that a column cannot have a null value
- UNIQUE contraints: ensures that all values in a column are different/unique
- Primary Key Constrains uniquely identifies each row/record in a database table.
- Foreign Key Constrains data based on columns in other tables.
- Check Contraint ensures that all values in a column satisfy certain conditions
- Exclusion Constraint ( Look up)

---

CREATE TABLE: keyword allows u to creates tables in SQL

```sql
-- Full general syntax
CREATE TABLE table_name (
	column_name TYPE column_constraint,
	column_name TYPE column_constraint,
	table_constraint table_constraint
) INHERITS existing_table_name

-- real syntax example
CREATE TABLE player (
	player_id SERIAL PRIMARY KEY -- see serial def bellow 
	age SMALLINT NOT NULL 
)
```

SERIAL:  in postgreSQL a sequence is a special kind of databse object that generates a sequence of integers and a sequence is often used as the primary key column in a table. 

so serial will create a sequence object and set the next value generated by the sequence as the default value for the column. This is perfect for a primary key because it logs unique entries for you automatically upon insertion

If arow is later removed, the column with the SERIAL data type will not adjust, marking the fact that a row was removed from the sequence, for example 1,2,3,5,6,7
You know row 4 was removed at some point

```sql
-- query used to create account table
CREATE TABLE account(
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR (50) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL,
    email VARCHAR (250) UNIQUE NOT NULL,
    creat_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP
)
-- 
```

---

INSERT: allows you to add in rows to a table 

```sql
-- general syntax
INSERT INTO tableName(column1, column2,...)
VALUES
	(value1, value2,...)
	( value1, value2,...)  

-- real life syntax ex
INSERT INTO account(user_name, password, email, creat_on)
VALUES
('Yassine', 'password', 'yassine@yassine.com', CURRENT_TIMESTAMP)
-- above we where it says account(columns...) we pass in all the columns
-- we want to fill out in that order so the values have to be in order too

-- notice how we didn't add user_id column that's coz it's fill out automaticalyy
-- by postgreSQL since we set it to SERIAL
-- dont forget the commas , its v important

-- table that references multiple tables (intermidiary table)
CREATE TABLE account_job(
	user_id INTEGER REFERENCES account(user_id),
	job_id INTEGER REFERENCES job(job_id),
	hire_date TIMESTAMP
)
-- notice how for user_id we set it to INTEGER and not SERIAL that's coz it's
-- referencing a foreing_key to another table 

-- (only use SERIAL for primary key in its table) 
-- (use INTEGER to refer to the primary key from another table)

-- u cant add a user_id to the account_job table that doesn't exist 
-- in the account table... why u ask?

-- coz the user_id from account_job table is referring to 
-- the user_id from the account table it

-- ^^ same for the job_id 
```

```sql
-- general syntax
INSERT INTO tableName(column1, column2,...)
VALUES
	(value1, value2,...)
	( value1, value2,...)  

-- real life syntax ex
INSERT INTO account(user_name, password, email, creat_on)
VALUES
('Yassine', 'password', 'yassine@yassine.com', CURRENT_TIMESTAMP)
-- above we where it says account(columns...) we pass in all the columns
-- we want to fill out in that order so the values have to be in order too

-- notice how we didn't add user_id column that's coz it's fill out automaticalyy
-- by postgreSQL since we set it to SERIAL
-- dont forget the commas , its v important

-- table that references multiple tables (intermidiary table)
CREATE TABLE account_job(
	user_id INTEGER REFERENCES account(user_id),
	job_id INTEGER REFERENCES job(job_id),
	hire_date TIMESTAMP
)
-- notice how for user_id we set it to INTEGER and not SERIAL that's coz it's
-- referencing a foreing_key to another table 

-- (only use SERIAL for primary key in its table) 
-- (use INTEGER to refer to the primary key from another table)

-- u cant add a user_id to the account_job table that doesn't exist 
-- in the account table... why u ask?

-- coz the user_id from account_job table is referring to 
-- the user_id from the account table it

-- ^^ same for the job_id 
```

---

UPDATE: keyword allows for the changing of the values of the column in a table

```sql
-- general syntax
UPDATE table 
SET column1 = value1
column2 = value2
WHERE condition

-- reset everything without condition
UPDATE account 
SET last_login = CURRENT_TIMESTAMP

-- set based on another column
UPDATE account
SET last_login = created_on

-- using another table values (update join)
UPDATE tableA 
SET original_col = tableB.new_col
FROM tableB
WHERE tableA.id = tableB.id 

-- return rows that were affected
UPDATE account SET last_login = created_on
RETURNING account_id, lasr_login
```

```sql
-- real life symtax ex:

UPDATE account
SET last_login = CURRENT_TIMESTAMP
-- this querry will set the the last login column to the current time date etc

UPDATE account
SET last_login = creat_on 
-- this query will set last_login to what creat_on is to

SET last_login = '2022-01-01'
WHERE last_login IS NULL
-- this query uses a condition to update the last_login column
-- only where last_login is NULL

UPDATE account_job
SET hire_date = account.creat_on
FROM account
-- this is call an update join this query uses a different table to update a 
-- column or using the condition like WHERE to specify a row or rows 
-- to update that matches the condition 

UPDATE account_job
SET hire_date = CURRENT_TIMESTAMP
RETURNING *
-- using the returning keyword u can return specific columns or all of them
-- after updating in 1 query so u dont have to type select again 

-- update multiple rows using CASE 
-- (btw using this will lose every rown in the column being updated that's not 
-- part of the update bellow) 
UPDATE table_test 
SET address = CASE
    when id = 3 then '512 marker dr'
    when id = 2 then '615 thusk rd'
END
```

---

DELETE: We can use the delete clause to remove rows from a table 

```sql
-- general syntax
DELETE FROM tableName
WHERE row_id = 1

-- delete based on other tables
DELETE FROM tableA
USING tableB
WHERE tableA.id = tableB.id

-- delete everything from a table
DELETE FROM tableName

-- u can also add the returning clause to see what got delete

-- this query will delete the job mag row and return everything that got 
-- deleted in that row
DELETE FROM job
WHERE job_name = 'mag'
RETURNING *
```

---

ALTER :  allows to make change to an existing table ex of some bellow:

- Adding, dropping, or renaming columns
- Changing a column's data type
- Set DEFAULT values for a column
- Add CHECK constraints
- Rename table

```sql
-- general syntax
ALTER TABLE tableName action 
-- (replace action with what you wanna change in the table )

-- add column 
ALTER TABLE tableName ADD COLUMN new_colName TYPE
-- this how u add a new column to a table give it a name and data type

-- removing columns 
ALTER TABLE tableName DROP COLUMN colName
-- this query will remove a column from a table

-- u can even alter the constraints
ALTER TABLE tableName ALTER COLUMN colName 
-- list bellow of some contraint u can alter 
SET DEFAULT value
DROP DEFAULT 
SET NOT NULL
DROP NOT NULL
ADD CONSTRAINT constraint_name

-- remaing a table
ALTER TABLE account
RENAME TO k
-- here the account table will be remane to k

-- renaming a colum
ALTER TABLE account
RENAME COLUMN creat_on
TO created_on
-- this query will rename the creat_on column 
-- from the account table to created_on
 

-- https://www.postgresql.org/docs/current/sql-altertable.html
```

---

DROP: allows to complete remove a column in a table 

```sql
-- general syntax
ALTER TABLE table_name
DROP COLUMN columnName

-- if exist
ALTER TABLE table_name
DROP COLUMN IF EXISTS columnName
-- by adding if exists postgresql will only try to drop the column if it exists
-- and it it doesnt exists u wont get an error 

-- Drop multiple table
ALTER TABLE table_name
DROP COLUMN columnName1,
DROP COLUMN columnName2,
DROP COLUMN columnName3,
```

---

CHECK: constraint allows to create more customized constraints that adhere to a certain conditions.

```sql
-- general syntax
CREATE TABLE example(

	  id SERIAL PRIMARY KEY,
    age SMALLINT CHECK(age > 21),
    parent_age SMALLINT CHECK(parent_age > age) 
   
);
-- so how check constraints works is it basically check 
-- whatever u ask it to check before inserting anything in the column
-- with check constraints

-- ex above u can't insert any age bellow 21 coz of the check constraints
-- and u cant insert a parent age that isn't grater than 21 

```

---

CONDITIONAL EXPRESSIONS: 

CASE: we can use the case statment to only execute SQL code when certain conditions are met

```sql
-- general CASE syntax

CASE
	WHEN codition1 THEN result1
	WHEN codition2 THEN result2
	ELSE some_other_results

END
```

Example using the table bellow 

test

| a |
| --- |
| 1 |
| 2 |

```sql
-- general case
SELECT a,
CASE WHEN a = 1 THEN 'one' -- if a == 1 return 'one'
		 WHEN a = 2 THEN 'two' -- if a == 2 return 'two'
ELSE 'other' -- if != 1 or 2 return other 
END FROM test

/*
So above were saying where a = 1 return one and where a = 2 return 2
so since in the a column there's rown 1 and 2
both one and two will be return
and the else is just saying if none of them = to 1 or 2 return other

WHEN are basically like if statments in python
*/

-- Case Expressions: 
-- first evaluates an expression then compares the results with
-- each value in the WHEN clauses sequentially

-- Case Expressions general syntax
CASE expression
	WHEN value1 THEN result1
	WHEN value2 THEN result2
ELSE some_other_result
END 
```

```sql
-- real life case example using dvdrentals db and customer table

SELECT customer_id,
CASE
    WHEN customer_id <= 100 THEN 'Best Customers'
    WHEN (customer_id <= 200) THEN 'Okay Customers'
    ELSE 'Regular Customers'
END AS customer_class
FROM customer

/* 
So here im using general case to check if the customer id is <= 100
if it is i give them a best customer lable in the customer_class column in 
the case table being return

same with 200 

but if their customer_id is not <= to 100 or 200 they get a regular customers 
badge 
so basically everyone else

BTW the () is optional
( query above will return 2 column 
	customer_id and customer_class
) 
*/

-- real life Case Expressions example using dvdrentals db and customer table
SELECT customer_id,
CASE customer_id
    WHEN 1 THEN 'Winner'
    WHEN 2 THEN 'Second Place'
    ELSE 'Losers'
END AS results
FROM customer
ORDER BY customer_id

/*
So case espressions is a bit different it check for equality

it goes tru all the customer id and where the customer id = to 1 it returns 
Winner and when its equal to 2 it returns Second place
and everything else as losers

its basically looping tru a list like in python

*/

-- btw u can pass case tru an agregated function multiple of times like this
SELECT 
SUM(CASE rating
    WHEN'R' THEN 1
    ELSE 0
    END 
    ) AS r,
    
SUM(CASE rating
    WHEN'PG' THEN 1
    ELSE 0
    END 
    ) AS pg,
    
SUM(CASE rating
    WHEN'PG-13' THEN 1
    ELSE 0
    END 
    ) AS pg13 
FROM film
```

---

COALESCE: accepts an unlimited number of arguments. it returns the first argument that is not null if all arguments are null the COALESCE function will return null

```sql
Example 
SELECT COALESCE(1,2)
1 gets return

SELECT COALESCE(NULL,2,3)
2 gets return

-- Keep the COALESCE function in mind in
-- case you encounter a table with null values
-- that you want to perform operations on!
```

---

CAST:  lets u convert from one data type to another. Keep in mind not every instance of a data
type can be CAST to another data type, it must be reasonable to convert the data

for example '5' to an integer will work, 

but 'five' to an integer will not.

```sql
-- syntax for cast funtion
SELECT CAST('5' AS INTEGER)

-- postgreSQL CAST operator :: 
SELECT '5'::INTEGER 
```

---

NULLIF: takes in 2 inputs and returns NULL if both are equal, otherwise it returns the first argument passed 

```sql
--Example 
NULLIF(argument1, argument2) -- general syntax

NULLIF(10, 10)
-- will return NULL since 10 = 10

NULLIF(10, 12)
-- will return 10 since 10 != 12 and 10 was the first argument pass

SELECT(
	SUM(CASE WHEN department='A' THEN 1 ELSE O END)/
	NULLIF(SUM(CASE WHEN department='B'THEN 1 ELSE O END),0)
)AS department_ratio
FROM depts

-- the nullif above return a null if the sum function returns a 0
-- that's why we added a 0 at the end remember if 2 arguments are equal 
-- nullif returns null
```

---

VIEWS:  is like a stored query when u find yourself using a certain query many times instead of writting it all everytime u can create a view that you can use to easily call that query

```sql
-- example 
CREATE VIEW info AS --}.    general syntax
SELECT * FROM customer -- } 

-- real life exaple 
/*
Now let's say we will need a customer first name last name and address for some
reports and everytime we need to creat a complicated table join to get that

instead we can creat a simple/short view to get the table join so we can get our 
data
*/ 

-- let's say bellow is the complicated table join 
SELECT first_name, last_name, address FROM customer
INNER JOIN address 
ON  customer.address_id = address.address_id

--  instead of typing that everytime we can create a view to help us. bellow:
CREATE VIEW customer_info AS
SELECT first_name, last_name, address FROM customer
INNER JOIN address 
ON  customer.address_id = address.address_id

-- so now whenever we need the data we can just call our view instead of 
-- typing that long INNER JOIN like so: 
SELECT * FROM customer_info

-- ^ much easier 

-- u can even change replace or delete a view 
-- now lets say i dont need last names to be query from that view  i can just
CREATE OR REPLACE VIEW customer_info AS
SELECT first_name, address FROM customer
INNER JOIN address 
ON  customer.address_id = address.address_id

-- boom when we query the view after this query we wont get last name
-- btw u can add columns too

-- to drop/delete a view do 
DROP VIEW customer_info

-- to check if a view exists first before dropping so u wont get error
DROP VIEW IF EXISTS customer_info

-- to change a view name
ALTER VIEW customer_info RENAME TO c_info
-- query above will delete customer_info and rename it to  c_info
```

---

IMPORT and EXPORT: 

```sql
-- come back to leacture if u got problem importing/exporting in pgAdmin
```

---

[SQL Challenges, Anwser & Reviews](https://www.notion.so/SQL-Challenges-Anwser-Reviews-fae7a0bfb7464b5fac14a6b62b7665bc)

[PgAdmin & psql Shortcuts](https://www.notion.so/PgAdmin-psql-Shortcuts-e4978dad031543128d69e544fa8743da)