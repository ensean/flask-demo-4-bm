#!/bin/sh
sudo yum groupinstall "Development Tools" -y
sudo yum install python3-devel mysql-devel -y
pip install -r requirements.txt