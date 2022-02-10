#!/bin/bash

clear

sha=0
previous_sha=0

cd ~/projects/zalupa_slona/

update_sha()
{
	# getting sha of filesystem
	sha=`ls -lR . | sha1sum`
}

upload () {
	## upload commands here
	git add --all
	git commit -m "AWS GIT stakeholder commit $(date +%d-%b-%Y%t%T)"
	git push origin main:main
	echo "--> Monitor $(date +%T): Files uploaded. OK"
	echo "--> Monitor $(date +%T): 2 hours timeout. Next check at $(($(date +%H)+2)):$(date +%M)"
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
	## if not match -  making upload and wait 2h
    	update_sha
    	if [[ $sha != $previous_sha ]]; then 
    		changed
    		sleep 2h
    	else
    		sudo shutdown -h now
    	fi
}

run () {
	#
	while true; do
		compare
		#read -s -t 1 && (
		#echo "--> Monitor $(date +%T): Forced Upload..."
		#upload
		#)
	done
}

echo "--> Monitor $(date +%T): Init..."
echo "--> Monitor $(date +%T): Monitoring filesystem..."
run
