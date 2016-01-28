TAG=$1
TRACE=$2
NOW=$(date +"%m-%d-%Y-%H-%M-%S")
SPLITTER="_"
NAME=$TAG$SPLITTER$NOW

adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > $ANDROID_SCREENSHOT/$NAME.png

mkdir -p $ANDROID_SCREENSHOT/$TAG

if [[ ! -z "$TRACE" ]]
	then echo $TRACE >> $ANDROID_SCREENSHOT/$TAG/trace$SPLITTER$NOW.txt
fi

mv $ANDROID_SCREENSHOT/$NAME.png $ANDROID_SCREENSHOT/$TAG
