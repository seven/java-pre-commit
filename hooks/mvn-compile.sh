#!/bin/bash 
echo "----java pre commit check begin----"
mvn compile
if [ $? -ne 0 ]
then
	echo '--------------------------------------------------'
	echo "编译都失败了！请不要commit."
	echo '--------------------------------------------------'
        exit 1
fi
echo "----java pre commit check end ----"
