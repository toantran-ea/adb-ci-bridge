echo Creating screenshots folder ...
mkdir -p $ANDROID_SCREENSHOT

nohup python -m simple_server.py 9000 &

cd ~/