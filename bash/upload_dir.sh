#!/bin/bash

echo "Type instance ip:"
read instance_ip

rsync -avzhe "ssh -i ~/.ssh/git.pem" --exlude '.git' --delete ~/Desktop/projects/zalupa_slona ec2-user@$instance_ip:~/projects
