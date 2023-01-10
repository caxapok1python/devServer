from loader import dp
from .private_chat import isPrivate, isGroup

dp.filters_factory.bind(isPrivate)
dp.filters_factory.bind(isGroup)
