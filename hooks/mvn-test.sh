#!/bin/bash 
echo "----java pre commit check begin----"
mvn test
if [ $? -ne 0 ]
then
	echo '--------------------------------------------------'
	echo "Unit Test都失败了！请不要commit."
	echo '--------------------------------------------------'
        exit 1
fi
echo "----java pre commit check end ----"
