import os
import subprocess
import sys

# Sets up monitors for bspwm
# setup_monitors.py <num_desktops> <top:bottom paddings...>

exec_result = subprocess.run(["bspc", "query", "--monitors", "--names"], stdout=subprocess.PIPE)
monitors = exec_result.stdout.decode('utf-8').split("\n")[:-1]

# setup paddings
for i, monitor in enumerate(monitors):
    index = 1 + i;
    if index >= len(sys.argv):
        os.system(f"bspc config -m {monitor} bottom_padding 0")
        os.system(f"bspc config -m {monitor} top_padding 0")
    else:
        padding = sys.argv[index].split(":")
        top = padding[0]
        bottom = padding[1]
        os.system(f"bspc config -m {monitor} bottom_padding {bottom}")
        os.system(f"bspc config -m {monitor} top_padding {top}")
