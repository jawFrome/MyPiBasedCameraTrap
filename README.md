# General notes

## Setting in the pi zero with a video stream
used: https://github.com/smford/raspberry-pi-streaming-camera?search=1

but had to do the following modification:
```
The Solution was to edit /boot/config.txt, remove the line "camera_auto_detect=1", and add "start_x=1" and "gpu_mem=128".
```
