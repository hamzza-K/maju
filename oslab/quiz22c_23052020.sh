#!/bin/bash

zenity --forms --title="Records" --text="Update the Records" --separator="," --add-entry="First Name" --add-entry="Last Name" --add-entry="Email" --add-entry="Password" --add-entry="DOB" >> records.csv

case $? in
	0) zenity --info --text="Updated Successfully";;
	1) zenity --info --text="Not Updated";;
	-1) zenity --error --text="Error";;
esac

