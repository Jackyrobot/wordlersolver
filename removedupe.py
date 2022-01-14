import os
import sys

if __name__ == '__main__':
    fromfile = sys.argv[1]
    tofile = sys.argv[2]

    with open(fromfile, 'r') as f:
        words = [line.rstrip() for line in f]
        res = []
        [res.append(x) for x in words if x not in res]
        
    with open(tofile, 'w') as g:
        for word in res:
            g.write(word + "\n")