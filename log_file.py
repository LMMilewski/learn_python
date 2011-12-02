#/usr/bin/python2.7

import logging
import logging.config

def show_some_logs(log):
    log.debug("Normal operation + detailed debug info")
    log.info("Normal operation")
    log.warn("Library code. Issue is avoidable. Modify the application to eliminate this warn")
    log.warning("Note this event! Unfortunately the issue is NOT avoidable")
    log.error("Error, but I don't want to raise exception. Could not perform some function")
    log.critical("Error, but I don't want to raise exception. I probably can't continue running")


logging.config.fileConfig('log_file.conf')
dbg = logging.getLogger("dbg")
inf = logging.getLogger("inf")

show_some_logs(dbg)
show_some_logs(inf)
