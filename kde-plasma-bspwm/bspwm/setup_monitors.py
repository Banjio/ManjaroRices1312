import os
import subprocess
import sys

# Sets up monitors for bspwm
# setup_monitors.py <num_desktops>

exec_result = subprocess.run(["bspc", "query", "--monitors", "--names"], stdout=subprocess.PIPE)
monitors = exec_result.stdout.decode('utf-8').split("\n")[:-1]

num_desktops = int(sys.argv[1])

if (num_desktops == 10):
    desktops = list(range(num_desktops))
    desktops = desktops[1:] + desktops[:1]
else:
    desktops = list(range(1, num_desktops + 1))

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

split_desktops = list(split(desktops, len(monitors)))
for i, monitor in enumerate(monitors):
    command = f"bspc monitor {monitor} -d {' '.join(str(x) for x in split_desktops[i])}"
    os.system(command)
