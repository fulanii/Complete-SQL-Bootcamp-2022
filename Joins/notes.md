SECTION 3 JOINS

```sql
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

Now lets say we want to see the people who register and login we can use inner join to do this

```sql
SELECT * FROM registration INNER JOIN login ON registration.name = login.name

-- here were saying where do we have in match 
-- registration(table) in name(column) and login(table) in name(column)

-- Btw registration.name and login.name are basically 
-- the table name dot(.) the column name

```

So this will be the output

Note: since we said SELECT * in the query above we get duplicated name coz there name in both tables

```sql
SELECT reg_id, login.name, login_id, log_id FROM registration
INNER JOIN LOGINS ON registration.name = login.name

-- i think login.name can be switch around with registration.name 
-- sice the name are all the same 
-- (not sure to look on too)
```

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

```sql
SELECT * FROM customer
LEFT OUTER JOIN payment
ON customer.name = payment.name

-- so here the customer table is the left table aka tableA
-- were grabing everithng from tableA and mathing tableA has with tableB
-- but nothing unique to tableB 
```

This is the output 

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

```sql
SELECT * FROM Sales_Q1
UNION
SELECT * FROM Sales_Q2

``` sql

this will be the output of the code above
| name | amount |
| --- | --- |
| david | 100 |
| claire | 50 |
| david | 200 |
| claire | 100 |