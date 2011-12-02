#!/usr/bin/python2.7

import logging

## this goes before importing log_1, log_2 because the root
## configuration is needed when global vars in log_1 and log_2 are
## created
logging.basicConfig(format="%(asctime)s %(levelname)s\t%(name)s:%(lineno)d: %(message)s",
                    level=logging.WARNING)

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

show_some_logs()
log_1.show_some_logs()
log_2.show_some_logs()
