#!/usr/local/bin/python3

import argparse
import collections
import os

if __name__ == "__main__":

    ignored_file_names = (".DS_Store",)
    
    parser = argparse.ArgumentParser(description="This script finds duplicate files by name.")
    parser.add_argument("dir", help="the directory to crawl")    
    args = parser.parse_args()

    assert os.path.isdir(args.dir), "dir must exist %s" % args.dir

    # dict of file name -> list of paths with that file
    fname_to_paths = collections.defaultdict(list)

    for root, dirs, files in os.walk(args.dir):
        for fname in files:
            if not fname in ignored_file_names:
                fname_to_paths[fname].append(os.path.join(root, fname))

    unique_dirs_with_duplicate_files = set()
    num_dups = 0            
    for fname, paths in fname_to_paths.items():
        if len(paths) > 1:
            num_dups += len(paths)
            unique_dirs_with_duplicate_files.update([os.path.dirname(p) for p in paths])
            print("%s found in multiple locations:\n  %s\n" % (fname, "\n  ".join(paths)))

    if num_dups > 0:
        print("Unique paths with duplicate files:\n  %s\n" % "\n  ".join(unique_dirs_with_duplicate_files))
    print("Found %s duplicates.\n" % num_dups)
