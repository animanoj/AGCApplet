#!/bin/bash
while [ 1 ]
do
    pacmd set-source-volume alsa_input.pci-0000_00_1b.0.analog-stereo 20000
    sleep 0.001
done
