
--Q1
create temporary table temp_Employee_info
select concat(E.firstname, " ", E.lastname), S.salary, J.Jobtitle, D.deptName 
from Employees as E, Salary as S, Departments as D, Jobs as J where E.employeeId = S.employeeId and E.deptID = D.deptID and E.jobID = J.jobID;
--Q2
create table cloned_Employees like Employees;
--Q3
alter table cloned_Employees drop column lastname;
--Q4
create or replace view vw_Employees as select firstname, lastname, hiring_date from Employees;
--Q5
insert into Employees values (13, 'nebula', 'distant', 'Deadstar', '2009-04-02', 5, 'ENG456');
--Q6
alter view vw_Employees as select firstname, lastname, hiring_date from Employees where year(hiring_date)=2019;
--Q7
insert into vw_Employees values ('Jeorgo', 'Jovannno', '2019-02-21');
--Q8
insert into vw_Employees values ('It was I', 'Dio', '2012-08-16');

