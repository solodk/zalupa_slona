#!/bin/bash

MYREPO_DIR=/home/ec2-user/projects/zalupa_slona/.git
CURRENT_DATE=$(date +%d-%b-%Y%t%T)
echo $CURRENT_DATE

git --git-dir=$MYREPO_DIR add --all
git --git-dir=$MYREPO_DIR commit -m "AWS GIT stakeholder commit $CURRENT_DATE"
git --git-dir=$MYREPO_DIR push
