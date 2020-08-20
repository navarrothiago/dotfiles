#!/bin/bash

set -e 
sudo modprobe v4l2loopback devices=2 video_nr=91,92 exclusive_caps=0,1
gst-launch-1.0 souphttpsrc location=http://$1:80/live ! jpegdec ! videoconvert ! v4l2sink device=/dev/video91 &
obs
