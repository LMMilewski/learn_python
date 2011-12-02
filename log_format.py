#!/usr/bin/python2.7

import logging

def show_some_logs():
    log.debug("Normal operation + detailed debug info")
    log.info("Normal operation")
    log.warn("Library code. Issue is avoidable. Modify the application to eliminate this warn")
    log.warning("Note this event! Unfortunately the issue is NOT avoidable")
    log.error("Error, but I don't want to raise exception. Could not perform some function")
    log.critical("Error, but I don't want to raise exception. I probably can't continue running")


## set format
# http://docs.python.org/library/logging.html#logrecord-attributes
logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(lineno)d:%(funcName)s: %(message)s",
                    level=logging.DEBUG)
log = logging.getLogger(__name__)

show_some_logs()

