cd ~/Documents
git clone -b Copter-3.5.5 https://github.com/ardupilot/ardupilot
cd ardupilot
git submodule update --init --recursive
cd Tools/autotest
echo pwd
