#!/bin/sh
openssl enc -d -nosalt -aes-128-cbc -in $1.enc -out $1
openssl enc -d -nosalt -aes-128-cbc -in $2.enc -out $2

cat $1 $2 > resultat.txt
