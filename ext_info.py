import pathlib
import sys
from collections import defaultdict

def suf(suffix):
    if suffix == "." or suffix == "":
        return "."
    else:
        return suffix[1:]

# Check arguments
if len(sys.argv) != 2:
    print("Usage: ext_info.py path")
    print("displays number of files and total size of files per extension in the specified path.")
    sys.exit()
    
path = pathlib.Path(sys.argv[1])
info = [(suf(f.suffix), f.stat().st_size)
    for f in path.iterdir() if f.is_file()]

sizes = defaultdict(int)
count = defaultdict(int)
for suffix, size in info:
    sizes[suffix] += size
    count[suffix] += 1

for suffix in sorted(sizes):
    print("%s %d %d" % (suffix, count[suffix], sizes[suffix]))
