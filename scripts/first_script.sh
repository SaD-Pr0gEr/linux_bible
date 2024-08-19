#!/bin/bash
# set -x
#kernelName=`uname -s`
#username=`whoami`
#osName=`uname -o`
#processor=`uname -p`
#kernelVersion=`uname -r`
#someCommand=$(pwd)
#BALANCE=200
#echo "a\nb"
#echo "You are using\n OS: $osName $processor\n Kernel: $kernelName $kernelVersion\n You'r logged in as: $username\n Current Directory: $someCommand\n \$Path=$PATH"
#echo '$osName'
#echo "$osName"
#echo "Args: $0 $1 $2\nArgs count: $#\nAll accepted args(without \$0): $@\nArg \$0 always be path to file\nScript exit code: $?"
#read -p "Your args: " arg1 arg2 arg3
#echo "Your args: $arg1 $arg2 $arg3"
#echo "$arg1"
#echo "$arg2"
#echo "$arg3"
#THIS="Example"
#THIS=${THIS:-"Not Set"}
#THAT=${THAT:-"Not Set"}
#echo $THIS
#echo $THAT
#DJANGO_SETTINGS_MODULE=core.settings.dev
#echo $DJANGO_SETTINGS_MODULE
#read -p 'enter your age: ' userAge
#userBirthYear=$[$(date +%Y)-$userAge]
#echo "You are $userAge years old, so you born at $userBirthYear(cause it's $(date +%Y))"
#let bornYear=$(date +%Y)-$userAge
#echo "You are $userAge years old, so you born at $bornYear"
#echo "You are $userAge years old, so you born at $(expr $(date +%Y) - $userAge)"
#echo "You are $userAge years old, so you born at `echo "$(date +%Y) - $userAge" | bc`"
#I=0
#echo "$((++I))"
#echo $I
#echo "$((I++)) and $I"
#echo $I
#if [ $userAge -eq 22 ] ; then
#echo "Good guy $(expr $userAge % 3) $[$userAge + 20] $[($userAge / 10) * 2]"
#elif [ $userAge -lt 18 ] ; then
#echo "Skarlupa"
#fi
#read -p 'enter your name: ' userName
#if [ $userName = 'ozod' ] ; then
#echo 'U r generally good guy'
#else
#echo 'fi, u r skarlupa, boy'
#fi
#let xt="$userAge * 10" 
#echo "$userAge * 10 => $xt"
#echo "$(($userAge + 20))"
#res=$[1 + 2]
#echo "$[$userAge + 20 * 20 / 20 % 5 - 2 ** 2]"
#let userAge="$userAge + 20"
#echo $userAge
#echo $(($userAge + 20))
#echo "$((userAge++))++"
#echo $userAge
#echo "++$((++userAge))"
#echo $userAge
filename="$HOME"
if [ -f "$filename" ] ; then
echo "$filename is a regular file"
elif [ -d "$filename" ] ; then
echo "$filename is a directory"
else
echo "I have no idea what $filename is"
fi
