if [ -z "$ANDROID_SCREENSHOT" ]; then
    echo "Need to set ANDROID_SCREENSHOT"
    exit 1
fi  

TAG=$1
TRACE=$2
NOW=$(date +"%m-%d-%Y-%H-%M-%S")
SPLITTER="_"
NAME=$TAG$SPLITTER$NOW

adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > $ANDROID_SCREENSHOT/$NAME.png

mkdir -p $ANDROID_SCREENSHOT/$TAG

mv $ANDROID_SCREENSHOT/$NAME.png $ANDROID_SCREENSHOT/$TAG
