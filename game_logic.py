import random
import turtle
from cursor import Cursor
from constants import *


def generate_secret_code() -> list:
    """Generate a random secrete code"""
    secret_code = []
    for _ in range(4):
        secret_code.append(COLORS[random.randint(0, 5)])
    return secret_code

def click_marble():
    if clicked_in_region


