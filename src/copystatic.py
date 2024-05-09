import os, shutil

def copy_recursive(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
        print(f"made dir {dst}")
    src_paths = list(map(lambda f: os.path.join(src, f), os.listdir(src)))
    for p in src_paths:
        if os.path.isdir(p):
            dst_path = os.path.join(dst, os.path.split(p)[1])
            #os.mkdir(dst_path)
            copy_recursive(p, dst_path)
        else:
            shutil.copy(p, dst)
            print(f"copied {p} -> {dst}")