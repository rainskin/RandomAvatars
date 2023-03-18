from telegram import ext

from .. import mixins


class Message(mixins.Reply):
    for_users: list[int] = None
    filters: ext.filters.BaseFilter = ext.filters.UpdateType.MESSAGE

    @classmethod
    def get_filters(cls):
        filters = cls.filters

        if cls.for_users:
            filters &= ext.filters.User(cls.for_users)

        return filters

    @classmethod
    def build(cls):
        return ext.MessageHandler(cls.get_filters(), cls.handle)
