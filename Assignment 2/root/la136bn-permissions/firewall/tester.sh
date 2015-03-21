#!/bin/bash

# firewall tester -- while this script is running, it will wipe and reinstall
# the CURRENT version of the firewall script. You do NOT need this to do the
# lab and it does NOT test the correctness of your firewall.

COUNT=0
SLEEP=15

while true;
do
	wall "[$COUNT] Flushing and restarting firewall:" > /dev/null
	sudo ~/permissions/firewall/extingui.sh
	sudo ~/permissions/firewall/firewall.sh
	echo -n "[$COUNT] Sleeping "
	for i in `seq 1 $SLEEP`; do
		# echo $SLEEP $i
		echo -n "."
		sleep 1
	done;
	echo
	COUNT=$(($COUNT + 1))
	
done
