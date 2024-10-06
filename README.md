# General notes

## Setting up the pi zero with a video stream
used: https://github.com/smford/raspberry-pi-streaming-camera?search=1

but had to do the following modification with the latest Raspbian lite (6-oct 2024):
```
The Solution was to edit /boot/firmware/config.txt, remove the line "camera_auto_detect=1", and add "start_x=1" and "gpu_mem=128".
```
