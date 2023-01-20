#!/bin/bash
line="-----------------------------------------------------------------"
clear

echo -e "Starting at: $(date)\n" ;echo $line

echo -e  "UPTIME\n"
uptime
echo $line
echo -e "\nFREE"
free
echo $line
echo -e "\nWHO"
who
echo $line
echo -e "\nFinishing at: $(date)\n";echo $line

