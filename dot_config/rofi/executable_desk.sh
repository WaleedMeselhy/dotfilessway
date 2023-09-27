#!/bin/zsh
if [ "$ROFI_RETV" != "0" ]; then
    selected="$*"
    idasen-controller --move-to $selected > /dev/null 2>&1 &
fi
if [ "$ROFI_RETV" = "0" ]; then
    echo stand
    echo sit
fi
