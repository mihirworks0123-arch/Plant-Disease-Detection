#! /bin/sh
echo "======================="
echo "Welcome to setup"
echo "======================="

if [ -d "env" ];
then 
    echo "Enabling virtual env"

else
    echo "No virtual env"
    exit N
fi

# Activate virtual env
# . env/Scripts/activate
source env/Scripts/activate
# export ENV=developement
python main.py 
deactivate