#!/usr/bin/python2.7

import logging
import log_1
import log_2

def show_some_logs():
    log.debug("Normal operation + detailed debug info")
    log.info("Normal operation")
    log.warn("Library code. Issue is avoidable. Modify the application to eliminate this warn")
    log.warning("Note this event! Unfortunately the issue is NOT avoidable")
    log.error("Error, but I don't want to raise exception. Could not perform some function")
    log.critical("Error, but I don't want to raise exception. I probably can't continue running")

log = logging.getLogger(__name__)
## we don't set level - it should be inherited from it's parent (root in this case)
show_some_logs()
