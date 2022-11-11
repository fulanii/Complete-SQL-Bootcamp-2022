``` sql
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
