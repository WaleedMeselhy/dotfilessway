#!/bin/zsh
if [ "$ROFI_RETV" != "0" ]; then
    selected="$*"
    ps aux | grep $selected | awk 'NR==1 {print $2}' | xargs kill
fi
if [ "$ROFI_RETV" = "0" ]; then
    echo notion-app
fi
