#!/bin/sh
#
# This script will reset all iptables rules.
# Usage: ./extingui.sh
# 

sudo iptables-restore < /root/firewall/iptables_reset
