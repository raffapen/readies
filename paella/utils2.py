
from __future__ import print_function
import sys
from subprocess import Popen, PIPE

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def sh(cmd, join=False, lines=False):
    shell = isinstance(cmd, str)
    proc = Popen(cmd, shell=shell, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(err)
    if lines is True:
        join = False
    if lines is True or join is not False:
        out = out.split("\n")
    if join is not False:
        s = join if type(join) is str else ' '
        out = s.join(out).strip()
    return out
