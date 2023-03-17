from telegram import ext

from .. import mixins


class Message(mixins.Reply):
    filters: ext.filters.BaseFilter = ext.filters.UpdateType.MESSAGE

    @classmethod
    def get_filters(cls):
        return cls.filters

    @classmethod
    def build(cls):
        return ext.MessageHandler(cls.get_filters(), cls.handle)
