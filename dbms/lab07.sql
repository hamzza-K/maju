
-- LAB-07 BY HAMZZA K

--QUESTION #1
------------------------------------------------------------------
create table Employees (
	employeeId bigint unsigned not null auto_increment,
	firstname varchar(30) not null,
	lastname varchar(30) not null,
	birthcity varchar(20) null,
	hiring_date datetime null,
	deptID bigint unsigned,
	jobID varchar(6),
	primary key (employeeId),
	foreign key (deptID) references Departments(deptID),
	foreign key (jobID) references Jobs(jobID)
	on delete cascade
	key firstname (firstname)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;

------------------------------------------------------------------
insert into Employees values (default, "hamza", "khan", "Karachi", "2017-08-01", 1, "ENG126");
insert into Employees values (default, "John", "Doe", "London", "2015-05-07", 6, "ENG123");
insert into Employees values (default, "Star", "Light", "Inslaninity", "2012-02-02", 5, "ENG124");
insert into Employees values (default, "Nighteye", "Dead", "Midtown", "2011-01-10", 4, "ENG128");
insert into Employees values (default, "Lukewarm", "Heart", "Deadstar", "2014-12-12", 3, "MAN125");
insert into Employees values (default, "Night", "Crawler", "Gotham", "2006-06-06", 2, "MAN127");

------------------------------------------------------------------
create table Departments (
	deptID bigint unsigned not null auto_increment,
	deptName varchar(50) not null,
	locationID bigint unsigned,
	primary key (deptID),
	foreign key (locationID) references Locations(locationID)
	on delete cascade,
	key deptName (deptName)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;
------------------------------------------------------------------
insert into Departments values (default, "CS", 4);
insert into Departments values (default, "MS", 5);
insert into Departments values (default, "SE", 6);
insert into Departments values (default, "BBA", 7);
insert into Departments values (default, "PSY", 8);
insert into Departments values (default, "FA", 9);

------------------------------------------------------------------
create table Locations (
	locationID bigint unsigned not null auto_increment,
	city varchar(50) not null default "Islamabad",
	country varchar(50) not null default "Pakistan",
	primary key (locationID),
	key city (city)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;
------------------------------------------------------------------
insert into Locations values (default, default, default);
insert into Locations values (default, "Karachi", default);
insert into Locations values (default, "Florida", "USA");
insert into Locations values (default, "Manchester", "USA");
insert into Locations values (default, "Birmingham", "UK");
insert into Locations values (default, "Multan", default);
------------------------------------------------------------------

create table Jobs (
	jobID varchar(6) not null,
	jobTitle varchar(10) not null default 'N/A',
	salary decimal(10, 2) not null,
	primary key (jobID)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;

------------------------------------------------------------------
insert into Jobs values ("ENG123", "Junior", 20000.00);
insert into Jobs values ("ENG124", "Senior", 40000.00);
insert into Jobs values ("MAN125", "Head", 200000.00);
insert into Jobs values ("ENG126", "Senior", 45000.00);
insert into Jobs values ("MAN127", "Head", 400000.00);
insert into Jobs values ("ENG128", "Junior", 25000.00);
------------------------------------------------------------------


-- QUESTION #2

------------------------------------------------------------------
create table Student (
	studentID bigint unsigned not null auto_increment,
	firstname varchar(30) not null,
	lastname varchar(20) null default 'N/A',
	age int null,
	courseID bigint unsigned,
	primary key (studentID),
	foreign key (courseID) references Course(courseID) on delete cascade,
	key firstname (firstname)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;
------------------------------------------------------------------
insert into Student values (default, "hamzza", "khan", 22, 2);
insert into Student values (default, "Senjougahara", "Chan", 21, 4);
insert into Student values (default, "Mako", "Shita", 19, 1);
insert into Student values (default, "Ararargi", "Kyomi", 25, 3);
------------------------------------------------------------------

create table Marks (
	totalmarks bigint not null,
	studentID bigint unsigned,
	courseID bigint unsigned,
	foreign key	(studentID) references Student(studentID) on delete cascade,
	foreign key (courseID) references Course(courseID) on delete cascade
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;
------------------------------------------------------------------
insert into Marks values (99, 13, 1);
insert into Marks values (80, 16, 2);
insert into Marks values (95, 14, 3);
insert into Marks values (90, 15, 4);
insert into Marks values (75, 14, 7);
------------------------------------------------------------------
create table Course (
	courseID bigint unsigned not null auto_increment,
	coursename varchar(40) not null,
	primary key (courseID),
	key coursename (coursename)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;
------------------------------------------------------------------
insert into Course values (default, "Automata");
insert into Course values (default, "Software Engineering");
insert into Course values (default, "Financial Accounting");
insert into Course values (default, "Linear Algebra");
insert into Course values (default, "Calculus");
insert into Course values (default, "Freshman English");
insert into Course values (default, "Pakistan Studies");
insert into Course values (default, "Data Structures and Algorithms");
------------------------------------------------------------------
create table Employee_details (
	empID bigint unsigned not null auto_increment,
	emp_name varchar(30) not null,
	primary key (empID)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;
------------------------------------------------------------------
insert into Employee_details values (default, "hamzza");
insert into Employee_details values (default, "Sono Tori");
insert into Employee_details values (default, "Tashkani");
------------------------------------------------------------------
create table Salary (
	empID bigint unsigned,
	salary decimal(10, 2) not null,
	foreign key (empID) references Employee_details(empID)
	on delete cascade
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;
------------------------------------------------------------------
insert into Salary values (1, 15000.00);
insert into Salary values (2, 25000.00);	
insert into Salary values (3, 35000.00);
------------------------------------------------------------------