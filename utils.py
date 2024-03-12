import random
from constants import GEMINI_TOKENS, AVAILABLE_PROXIES_LIST


async def get_gemini_token() -> str:
    return random.choice(GEMINI_TOKENS)


async def get_proxy() -> str:
    return random.choice(AVAILABLE_PROXIES_LIST)
