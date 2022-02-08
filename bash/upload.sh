#!/bin/bash

cd home/ubuntu/Desktop/projects/

sha=0
previous_sha=0

update_sha()
{
	# getting sha of filesystem
	sha=`ls -lR . | sha1sum`
}

config () {
	## getting instance ip
	echo "--> Monitor $(date +%T): Enter instance ip:"
	read instance_ip
	echo "--> Monitor $(date +%T): OK"
}

upload () {
	## upload commands here
	rsync -avzhe "ssh -i ~/.ssh/git.pem -o "StrictHostKeyChecking=no"" --exclude '.git' --delete ~/Desktop/projects/ ec2-user@$instance_ip:~/projects
	echo "--> Monitor $(date +%T): Files uploaded. OK"
	echo "(Press enter to force update)" 
}

changed () {
	## starting upload procedure
	## rewriting sha state
	echo "--> Monitor $(date +%T): Files changed, uploading..."
	upload
	previous_sha=$sha
}

compare () {
	## updating sha
	## compairing two sha stages
	## if not true - goint to step 'changed' 
    	update_sha
    	if [[ $sha != $previous_sha ]] ; then changed; fi
}

run () {
	while true; do
		compare
		read -s -t 1 && (
		echo "--> Monitor $(date +%T): Forced Upload..."
		upload
		)
	done
}

echo "--> Monitor $(date +%T): Init..."
config
echo "--> Monitor $(date +%T): Monitoring filesystem..."
run
