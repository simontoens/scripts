#!/usr/local/bin/python3

import argparse
import collections
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This script finds duplicate files by name.")
    parser.add_argument("dir", help="the directory to crawl")    
    args = parser.parse_args()

    assert os.path.isdir(args.dir), "dir must exist %s" % args.dir

    # dict of file name -> list of paths with that file
    fname_to_paths = collections.defaultdict(list)

    for root, dirs, files in os.walk(args.dir):
        for fname in files:
            fname_to_paths[fname].append(os.path.join(root, fname))

    num_dups = 0            
    for fname, paths in fname_to_paths.items():
        if len(paths) > 1:
            num_dups += 1
            print("%s found in multiple locations:\n  %s\n" % (fname, "\n  ".join(paths)))

    print("Found %s duplicates.\n" % num_dups)
    
        
        
