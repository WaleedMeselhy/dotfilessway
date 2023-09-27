#!/bin/sh
wlr-randr --output DP-4 --mode 1920x1080 --pos 4640,0 --transform 270 --scale 1.0  \
    --output DP-3 --mode 3840x2160 --pos 1440,0 --transform normal --scale 1.2 \
    --output DP-2 --mode 2560x1440  --pos 0,0 --transform 90 --scale 1.0 \
    --output eDP-1 --off