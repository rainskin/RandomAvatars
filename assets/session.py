from botty import State, StatesGroup


class BroadcastState(StatesGroup):
    POST = State()


class RequiredJoinState(StatesGroup):
    POST = State()
