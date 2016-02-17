#!/bin/bash

if [ -z "$1" ]
  then echo You must supply an instance to provision
       echo "Options are commonly: local_dev, test, prod, staging."
  exit;
fi

host=$1

/usr/bin/ansible-playbook provisioners/playbook.yml -i "provisioners/${host}_hosts"
