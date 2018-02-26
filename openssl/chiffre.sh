#!/bin/sh
openssl enc -nosalt -aes-128-cbc -in $1 -out $1.enc
