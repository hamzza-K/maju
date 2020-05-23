#!/bin/bash

TIME=$(zenity --entry --title="Time Counter" --text="Enter the duration: ")
sleep $TIME

zenity --info --title="Time Completed" --text="The time is up. \n\nTotal time: $TIME"
