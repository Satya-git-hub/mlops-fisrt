
#!/bin/bash
sudo pip3 install virtualenv
cd /home/ec2-user/app
virtualenv environment
source environment/bin/activate
sudo pip3 install -r requirements.txt
sudo yum intall pip
sudo pip install supervisor 
sudo unlink /tmp/supervisor.sock