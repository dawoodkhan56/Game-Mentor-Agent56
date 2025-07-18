#game_tools.py
from agents import function_tool
import random


@function_tool
def roll_dice() -> str:
    return f"You rolled a {random.randint(1, 65)}!"

@function_tool
def generate_event() -> str:
    events = [
        "You found a hidden treasure!",
        "A wild monster appears!",
        "You encountered a mysterious stranger.",
        "You discovered an ancient artifact.",
        "A storm is brewing in the distance."
        "You solved a challenging puzzle.",
        "You escaped from a dangerous trap.",
        "You stumbled upon a secret passage.",
        "You received a cryptic message.",
        "You found a magical item.",
        "You made a new ally.",
        "You faced a difficult choice.",
        "You uncovered a dark secret.",
        "You were ambushed by bandits.",
        "You entered a forbidden area.",
        "You witnessed a strange phenomenon.",
        "You learned a valuable lesson.",
        "You encountered a talking animal.",
        "You were granted a wish by a mystical being.",
        "You found a map leading to a hidden location.",
        "You were cursed by an ancient spell.",
    ]
    return random.choice(events)