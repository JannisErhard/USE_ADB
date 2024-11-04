#!/bin/bash
text=`echo $1 | sed "s/\ /\%s/g"` #replace spaces with code for spaces
adb shell input text $text
adb shell input keyevent 22 # tab to attachment
adb shell input keyevent 22 # tab to send button
adb shell input keyevent 66 # press button
