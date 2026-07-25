#!/bin/bash

for dir in  data reports src secrets
do 
	if [ -d "$dir" ]; then
		echo "confirmed folder: $dir"
	else
		mkdir -p "$dir"
		echo "Created folder: $dir"
	fi
done

if [ ! -f "data/transactions.csv" ]; then
	echo "WARNING !"
	echo "========="
	echo "transactions.csv file is missing."
	echo "Add transactions.csv into data/"
fi
