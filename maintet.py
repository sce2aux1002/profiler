from profiling.useinput import Config
import os
import sys

if __name__ == "__main__":
    
    jdata = ""
    with open(sys.argv[1], 'r') as f:
        jdata = f.read()

    cfg = Config(jdata)
    print(cfg.tracked)
    