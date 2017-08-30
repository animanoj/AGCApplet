# Audio Gain Control Applet
A Gnome Applet that will stop Audio Gain Control used in WebRTC applications like Google Hangouts. The applet limits the microphone input volume continuously so as to prevent Audio Gain Control from increasing the volume depending on background noise.

Requires:
```
pacmd
python2.7
gtk3 >= 3.14
```
How to run:

Open a terminal (`Ctrl` + `Alt` + `t`) and execute (will run in background so you can close the terminal):
```
/usr/bin/python2.7 /path/to/project/microphone_applet.py &
```

The above command will work when adding the applet to Startup Applications as well (the `&` is unneccesary in this case).

The applet has options to disable and reeenable Audio Gain Control. On Exit, the applet will automatically stop limiting the microphone input volume, thus re-enabling Audio Gain Control.
