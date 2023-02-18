from .dispatcher import Dispatcher, dp


class App:
    def __init__(self, dispatcher: Dispatcher):
        self._dp = dispatcher

    def run(self, skip_updates: bool = False):
        import handlers
        handlers.setup()
        self._dp.run(skip_updates)


app = App(dp)
