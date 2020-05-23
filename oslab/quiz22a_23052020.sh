#!/bin/bash

color=$(zenity --entry --text "Enter the Color")
echo "$color"

zenity --info --text="the color is $color"

while true; do
	anotherColor=$(zenity --list --title="Colors" --column="Select a Color" "White" "Black" "Red" "Violet" "Purple" "Pain" "Yellow")
	if (("$anotherColor"=="Black" )); then
		zenity --error --text="You chose $anotherColor; Ending Now"
		break
	fi
	zenity --info --text="You chose $anotherColor"
done





