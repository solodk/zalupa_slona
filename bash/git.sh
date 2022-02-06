#!/bin/bash

## MYREPO_DIR=/home/ec2-user/projects/zalupa_slona/.git ##
CURRENT_DATE=$(date +%d-%b-%Y%t%T)

echo $CURRENT_DATE
cd ~/projects/zalupa_slona/




sha=0
previous_sha=0

update_sha()
{
	# getting sha of filesystem
	sha=`ls -lR . | sha1sum`
}

upload () {
	## upload commands here
	git add --all
	git commit -m "AWS GIT stakeholder commit $CURRENT_DATE"
	git push origin main:main
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
	#
	while true; do

		compare

		read -s -t 1 && (
		echo "--> Monitor $(date +%T): Forced Upload..."
		upload
		)
	done
}

echo "--> Monitor $(date +%T): Init..."
echo "--> Monitor $(date +%T): Monitoring filesystem... (Press enter to force update)"
run
