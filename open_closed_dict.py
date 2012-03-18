# Subclasses should not be able to brake superclasses

class MyDict(object):
    def __init__(self, iterable):
        self.item_list = []
        # we don't want to call update here, because if subclass
        # overrides update it can break __init__ which is not expected
        # behaviour by the subclass
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    # instead we do little trick that makes sure you can't override
    # update called by init while you can override update itself
    __update = update
