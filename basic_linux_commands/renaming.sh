#!/bin/bash

for file in *.HTM; do
	name=$(basename "$file" .HTM)
 	mv "$file" "$name.html"
	#before running it comment out the line above and uncomment the line below
 	#echo mv "$file" "$name.html"


done

