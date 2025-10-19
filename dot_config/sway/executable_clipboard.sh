#!/bin/bash

FAVFILE="$HOME/.config/cliphist/favorites"

# Combine favorites (plain) and cliphist (with IDs)
selected=$(
    { cat "$FAVFILE" 2>/dev/null | sed 's/^/⭐ /'; printf "\\n";
      cliphist list; } | \
    rofi -dmenu -font "$gui-font" -p "Select item to copy" -lines 10
)

# If it starts with ⭐, it's a favorite (copy as-is)
if [[ "$selected" == ⭐* ]]; then
    echo "${selected#⭐ }" | cut -d' ' -f2- | wl-copy
else
    # It's from cliphist, decode it
    echo "$selected" | cliphist decode | wl-copy
fi


