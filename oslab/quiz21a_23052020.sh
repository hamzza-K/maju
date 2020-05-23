#!/bin/bash


echo "Enter your salary: "
read salary
echo "Enter your year of service: "
read year


if ($year >= 5); then
	bonus=$((salary/100))
	bonus=$((bonus*5))
	salary=$((salary+bonus))
fi

echo "Net Salary is: $salary"
