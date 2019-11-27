#!/usr/bin/env python

import sys
import logging
import subprocess
from threading import Thread

logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logging.addLevelName(logging.INFO+2,'STDERR')
logging.addLevelName(logging.INFO+1,'STDOUT')
logger = logging.getLogger()

pobj = subprocess.Popen(sys.argv[1:], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def logstream(stream,loggercb):
    while True:
        out = stream.readline()
        if out:
            loggercb(out.rstrip())       
        else:
            break

stdout_thread = Thread(target=logstream,
    args=(pobj.stdout,lambda s: logger.log(logging.INFO+1,s)))

stderr_thread = Thread(target=logstream,
    args=(pobj.stderr,lambda s: logger.log(logging.INFO+2,s)))

stdout_thread.start()
stderr_thread.start()

while stdout_thread.isAlive() and stderr_thread.isAlive():
     pass
