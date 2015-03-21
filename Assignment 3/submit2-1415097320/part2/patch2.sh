#!/bin/bash

sudo mkdir /home/memo-users # create memo-users directory in /home
sudo groupadd memo-users # create memo-users group and give them ownership
sudo chgrp -R memo-users /home/memo-users
sudo chmod 755 /home/memo-users

# at this point, users can be added to memo-users group
# all users dealing with memos should be added

sudo mkdir /home/memo-users/memo # add the actual dir for storing memos
sudo chmod 775 /home/memo-users/memo

sudo chmod +t /home/memo-users/memo # sticky bit keeps files from arbitrarily deletion

sudo cp fixed.patch /usr/lib/cgi-bin/ # copy the patch over to memo.cgi's dir
cd /usr/lib/cgi-bin
sudo chmod -s memo.cgi # remove root-SUID from memo.cgi altogether
patch < fixed.patch # apply the patch! this may need sudo su - access


