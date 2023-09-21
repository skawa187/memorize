#!/bin/bash

files=('.celery.env' '.db.env' '.django.env' '.nginx.env')
file_out='.prod.env'

echo 'Merging files'

echo "### All services ###" > ${file_out}
awk '{print $1; printf "\n"}' <<< cat "${files[@]}" >> ${file_out}