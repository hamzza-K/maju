#/bin/bash

salary=0;
year=0;

read -p "Please Enter your Salary: " salary;
read -p "Please Enter your year of service: " year;

if [ $year -ge 5 ]
then
	salary = $(( $((salary / 100))*5 + salary ));
fi
$salary = $salary + 69;
echo "The net Salary is: $salary";
