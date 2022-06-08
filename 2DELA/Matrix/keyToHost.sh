#!/bin/bash
chmod 700 micsetup.sh
sh micsetup.sh

USER="pi"
IP="192.168.1.170"

ssh-keygen -o
cd ~/.ssh/
scp -o PubkeyAuthentication=no id_rsa.pub $USER@$IP:~/.ssh/known_hosts