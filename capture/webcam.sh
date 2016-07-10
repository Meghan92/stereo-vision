mkdir output
LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libv4l/v4l1compat.so fswebcam -r 544x288 -d /dev/video0 /home/meghan/Development/stereo-vision/capture/output/left.jpg &
LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libv4l/v4l1compat.so fswebcam -r 544x288 -d /dev/video1 /home/meghan/Development/stereo-vision/capture/output/right.jpg &
wait
