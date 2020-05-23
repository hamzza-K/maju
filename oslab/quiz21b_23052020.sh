#!/bin/bash

echo "Enter a Number: "

read num1

echo "Enter another Number: "

read num2

echo "Enter 1 for +, 2 for -, 3 for *, 4 for /: "

read operator

case $operator in
	1) echo $(( num1 + num2 ));;
	2) echo $(( num1 - num2 ));;
	3) echo $(( num1 * num2 ));;
	4) echo $(( num1 / num2 ));;
	*) echo "wrong input"
esac

