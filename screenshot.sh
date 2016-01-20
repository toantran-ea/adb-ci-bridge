SCREENSHOT_NAME=$1
NOW=$(date +"%m-%d-%Y-%H-%M-%S")
SPLITTER="_"
NAME=$SCREENSHOT_NAME$SPLITTER$NOW
echo Taking screenshot with name $SCREENSHOT_NAME

adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > $ANDROID_SCREENSHOT/$NAME.png