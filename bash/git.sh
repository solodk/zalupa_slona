#!/bin/bash

## MYREPO_DIR=/home/ec2-user/projects/zalupa_slona/.git ##
CURRENT_DATE=$(date +%d-%b-%Y%t%T)

echo $CURRENT_DATE
cd ~/projects/zalupa_slona/

git add --all
git commit -m "AWS GIT stakeholder commit $CURRENT_DATE"
git push origin main:main
