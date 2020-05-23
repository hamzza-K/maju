#!/bin/bash


previousdate=$(zenity --calendar --title="Select a Date" --day=6 --month=6 --year=2006)

pdate=${previousdate:0:2}
pmon=${previousdate:3:5}
pmon=${pmon:0:2}
pyear=${previousdate:6:10}

echo "$pdate $pmon $pyear"

date=$(date '+%d')
mon=$(date '+%m')
year=$(date '+%Y')

echo "$date $mon $year"

age=$((year - pyear - 1))

if (("$pmon" >= "$mon")); then
	age=$((age+1))
elif (( "$pmon" == "$mon")) && (("$pdate" >= "$date")); then
	age=$((age+1))
fi


echo "Your age is: $age"
