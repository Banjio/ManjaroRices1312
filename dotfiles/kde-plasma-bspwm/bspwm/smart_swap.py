import subprocess
import sys

# python smart_swap.py west/east/north/south
# Performs a default swap if neighbor leaf is lower or on the same depth
# else swaps with the parent on the same depth

direction = sys.argv[1]
r = subprocess.run(["bspc", "query", "-N", "-n", f"{direction}.local"], stdout=subprocess.PIPE)

if r.returncode != 0:
    # Desktop ends, used to send to desktop, if wanted
    exit(r.returncode)

me = subprocess.check_output(["bspc", "query", "-N", "-n"]).decode("utf-8").strip()
leaf_in_dir = r.stdout.decode("utf-8").strip()


def get_parents(node: str, cur_parents = []):
    r = subprocess.run(["bspc", "query", "-N", node, "-n", "@parent"], stdout=subprocess.PIPE)
    if r.returncode != 0:
        return cur_parents
    else:
        parent = r.stdout.decode("utf-8").strip()
        return get_parents(parent, cur_parents=[parent]+cur_parents)

my_parents = get_parents(me)
leaf_in_dir_parents = get_parents(leaf_in_dir)

if len(my_parents) < len(leaf_in_dir_parents):
    # Smart swap
    my_depth = len(my_parents)
    node_on_same_depth_of_leaf_in_direction = leaf_in_dir_parents[my_depth]
    r = subprocess.run(["bspc", "node", "-s", node_on_same_depth_of_leaf_in_direction, "--follow"])
    exit(r.returncode)
else:
    # normal swap
    r = subprocess.run(["bspc", "node", "-s", f"{direction}.local", "--follow"])
    exit(r.returncode)
