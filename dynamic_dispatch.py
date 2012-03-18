#!/usr/bin/python2.7

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

## Instead of doing framework (assuming that you want to use framework
## pattern for some reason) with limited number of commands it's
## better to do it using dynamic dispatch.
##
## That way subclass can define any behavior it needs instead of being
## able to choose only from the set of predefined methods
##
## See cmd.py for example of use
class Framework(object):  # obviously in real project you want more
                          # specyfic class name

    def execute(self, cmd_name, *args, **kwargs):
        try:
            # here you can put some code that's run before handler
            func = getattr(self, "handle_" + cmd_name)
            # here you can put some code that's run after handler
        except AttributeError:
            return self.default(cmd_name)
        log.info("calling [%s] with arguments [%s], [%s]",
                 func.__name__, args, kwargs)
        return func(*args, **kwargs)

    def default(self, cmd_name):
        log.warn("Unknown cmd [%s]", cmd_name)



## Implementation of framework
class CdPlayer(Framework):
    
    def handle_play(self, filename, repeat=1):
        log.info("Playing file %s, %s times", filename, repeat)
        return 1  # channel id

    def handle_stop(self, channel_id):
        log.info("Stopping channel %s", channel_id)


if __name__ == "__main__":
    player = CdPlayer()
    channel = player.execute("play", "my_music.ogg", repeat=2)
    player.execute("stop", channel)
    player.execute("set_volume", 20)

