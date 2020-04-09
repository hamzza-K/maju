create table my_table (
	id bigint unsigned not null auto_increment,
	status tinyint unsigned not null default 2,
	events int unsigned not null default 0,
	latitude decimal(10, 8) null,
	longitude decimal(11, 8) null,
	name varchar(50) not null,
	description varchar(120) not null default 'N/A',
	bio text null,
	birtday date null,
	event_time time null,
	created_at datetime not null,
	primary key (id),
	key status (status),
	key birthday_time (birtday, event_time)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;





create table Employees (
	employeeId bigint unsigned not null auto_increment,
	firstname varchar(30) not null,
	lastname varchar(30) not null,
	birthcity varchar(20) null,
	hiring_date datetime null,
	deptID bigint unsigned,
	jobID bigint unsigned,
	primary key (employeeId),
	foreign key (deptID) references Departments(deptID),
	foreign key (jobID) references Jobs(jobID),
	key firstname (firstname)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;


create table Departments (
	deptID bigint unsigned not null auto_increment,
	deptName varchar(50) not null,
	locationID bigint unsigned,
	primary key (deptID),
	foreign key (locationID) references Locations(locationID),
	key deptName (deptName)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;

create table Locations (
	locationID bigint unsigned not null auto_increment,
	city varchar(50) not null,
	country varchar(50) not null,
	primary key (locationID),
	key city (city)
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;


create table Jobs (
	jobID bigint unsigned not null auto_increment,
	jobTitle varchar(5) not null default 'ENG',
	salary decimal(10, 2) not null,
	constraint pk_job primary key nonclustered ([jobTitle], [jobID])
)engine=innodb
	default charset=utf8
	default collate=utf8_unicode_ci;


