import os, sys

out = 'c:/semester 2/Web UAS/debug_output.txt'
with open(out, 'w') as f:
    bak_path = 'c:/semester 2/Web UAS/index.html.bak'
    f.write(f"bak exists: {os.path.exists(bak_path)}\n")
    if os.path.exists(bak_path):
        f.write(f"bak size: {os.path.getsize(bak_path)}\n")
    
    idx_path = 'c:/semester 2/Web UAS/index.html'
    f.write(f"idx exists: {os.path.exists(idx_path)}\n")
    f.write(f"idx size: {os.path.getsize(idx_path)}\n")
    
    # List all files in directory
    for fn in sorted(os.listdir('c:/semester 2/Web UAS')):
        fp = os.path.join('c:/semester 2/Web UAS', fn)
        if os.path.isfile(fp):
            f.write(f"  {fn}: {os.path.getsize(fp)}\n")

print("Done - check debug_output.txt")
sys.stdout.flush()
