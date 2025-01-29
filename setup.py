#!/usr/bin/env python3
# steven@makeitwork.cloud
# https://github.com/makeitworkcloud/shelldefaults/blob/main/setup.py
# setup.py - Copies shell defaults into place

import os
import shutil

print("Creating `.bashrc.d`...")
os.makedirs(os.path.expanduser("~") + "/.bashrc.d", exist_ok=True)

print("Copying `vi`...")
shutil.copyfile("vi", os.path.expanduser("~") + "/.bashrc.d/vi")

print("Copying `.tmux.conf`...")
shutil.copyfile(".tmux.conf", os.path.expanduser("~") + "/.tmux.conf")

print("Success!")
