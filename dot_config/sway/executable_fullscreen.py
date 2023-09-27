#!/usr/bin/env python3
from i3ipc import Connection

i3 = Connection()
focused = i3.get_tree().find_focused()
if focused.ipc_data["app_id"] == "google-chrome":
    i3.command("split v; focus parent; fullscreen; focus child;")
else:
    focused.command("fullscreen")
