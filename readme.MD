CI Bridge Tookit 
==

1. What is this toolkit for?
=======
In an attempt to create a real-time debug tool that could run on any CI servers, can capture failed tests trace and screenshot. I create this. Well, the most `awesome` term here is `realtime`, but sadly to say that I have not completed this part :sosad:

2. Usage 
=======

- Define location to store screenshot and trace logs on your machine via env variable: `$ANDROID_SCREENSHOT`
Sample:
```shell
export ANDROID_SCREENSHOT="~/ubuntu/ci_screenshots"
```

- Run
```shell
git clone git@github.com:toantran-ea/adb-ci-bridge.git && cd adb-ci-bridge/ && ./setup_bridge.sh
```

Done!

3. What is the `science` behind? 
======

After running `setup_bridge.sh` script, there are few steps taken:

- The script will check if directory $ANDROID_SCREENSHOT is existing and create if not.
- Python webserver will be run in background via `nohup` on localhost at port `9001`
- Set system environment variable named `$ANDROID_SCREENSHOT` to be `1`. You can take advantage of this varible to know if you could contact the bridge-server.

4. Availble endpoints from bridge server
======
 - `POST /screenshot` 
	- request content: ```{"tag": <your screenshot tag>, "trace": <Your screenshot stracktrace if any>} ```
 - `POST /unlock` with empty body.
 
5. Sample:
=======
```shell
curl -H "Content-Type: application/json" -X POST -d '{"tag":"sample tag value","trace":"TooAwesomeException foo bar"}' http://localhost:9001/screenshot
```

