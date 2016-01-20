SCREENSHOT_NAME=$1
echo Taking screenshot with name $SCREENSHOT_NAME

adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > $ANDROID_SCREENSHOT/$SCREENSHOT_NAME.png