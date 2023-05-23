from botty import State, StatesGroup


class BroadcastState(StatesGroup):
    post = State()


class RequiredJoinState(StatesGroup):
    post = State()


class SignState(StatesGroup):
    sign = State()


class SendPictureState(StatesGroup):
    recipient = State()
    picture = State()
    confirm = State()
