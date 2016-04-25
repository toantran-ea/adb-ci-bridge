if [ -z "$ANDROID_SCREENSHOT" ]; then
    echo "Need to set ANDROID_SCREENSHOT"
    exit 1
fi  

echo Creating screenshots folder ...
mkdir -p $ANDROID_SCREENSHOT

nohup python -m server.py 9001 &

cd ~/

echo Bridge server with pid

echo All python processes running: $(ps aux | grep python)

export CI_BRIDGE_READY=1