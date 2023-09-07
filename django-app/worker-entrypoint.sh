#!/bin/sh

work_dir=${DJANGO_WORKDIR}
until cd ${work_dir}
do
    echo "Waiting for ${work_dir}";
    sleep 1;
done
echo "Mounted to ${work_dir}"

exec "$@"