#!/usr/bin/python2.7

import logging

def show_some_logs():
    logging.debug("Normal operation + detailed debug info")
    logging.info("Normal operation")
    logging.warn("Library code. Issue is avoidable. Modify the application to eliminate this warn")
    logging.warning("Note this event! Unfortunately the issue is NOT avoidable")
    logging.error("Error, but I don't want to raise exception. Could not perform some function")
    logging.critical("Error, but I don't want to raise exception. I probably can't continue running")

def logs_with_data():
    data_int = 123456789
    data_str = "hello world"
    data_fun = show_some_logs
    logging.info("Debugging with data int: %d, str: %s, fun %s", data_int, data_str, data_fun)


logging.basicConfig(filename="test.log", level=logging.DEBUG)
## DOES NOT DO ANYTHING, all basicConfig calls but first are No-Ops
logging.basicConfig(filename="test.log", level=logging.ERROR)

show_some_logs()
logs_with_data()
