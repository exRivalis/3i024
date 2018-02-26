#!/bin/sh
openssl enc -d -nosalt -aes-128-cbc -in $1.enc -out $1
