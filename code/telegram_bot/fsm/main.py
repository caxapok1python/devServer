from loader import State, StatesGroup


class Base64Mem(StatesGroup):
    encode = State()
    decode = State()


class Hash(StatesGroup):
    type = State()
    size = State()
    text = State()


class Random(StatesGroup):
    number = State()

