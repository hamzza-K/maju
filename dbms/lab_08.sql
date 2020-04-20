--Q1
 select D.deptName, count(E.employeeId) as total, avg(J.salary) as average 
 from Employees as E, 
 Departments as D, 
 Jobs as J 
 where E.jobID = J.jobID and E.deptID = D.deptID group by D.deptName;
--Q2	
select E.firstname, E.lastname, J.jobtitle, J.salary
from Employees as E
left join Jobs as J
on E.jobID = J.jobID
where J.salary = (select max(salary) from Jobs);
--Q3
select E.firstname, E.lastname, J.jobtitle 
from Employees as E 
left join Jobs as J --Designation == Jobtitle, in my tables
on E.jobID = J.jobID;
--Q4
select L.city, L.country, D.deptName
from Locations as L 
join Departments as D --My structure of the database was different; location had a unique key.
on L.locationID = D.locationID 
where L.country="Pakistan";
--Q5
select L.city, D.deptName 
from Locations as L, 
Departments as D, 
Employees as E 
where L.locationID = D.locationID and E.deptID = D.deptID;
--Q6
select E.firstname, E.lastname, D.deptname 
from Locations as L, 
Departments as D, 
Employees as E 
where L.locationID = D.locationID and E.deptID = D.deptID;
