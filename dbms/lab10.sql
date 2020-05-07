--Q1
select c.ContactName, c.Country, c.Phone, o.OrderDate, o.ShipCity, o.Freight, o.ShipName 
from customers as c, orders as o 
where c.CustomerID in 
	(select CustomerId from orders where ShippedDate
		in (select max(ShippedDate) from orders)) limit 20;
--I was not sure what the statement meant by "most recent",
-- but I applied the query according to the lecture note that you provided.
--In order to make the result clean I only chose a handful of features.
--Q2
select * from products where UnitPrice > (select avg(UnitPrice) from products);
--Q3
select * from customers where CustomerID in (select CustomerID from orders where OrderDate > "1994-05-01");
--There was no date above year 1996 in the database.
--Q4
select * from customers where CustomerID in (select CustomerID from orders where ShipCountry = "UK");
--Q5
select CompanyName from customers where CustomerID in (select CustomerID from orders where Freight in (select max(Freight) from orders));
--Q6
select * from employees where City in (select City from customers) and Country in (select Country from customers);
--I used suppliers in the image since employees table was spewing byte code.