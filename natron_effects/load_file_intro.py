import sys
sys.path.append("/home/gil/python3/natron_effects")
from typing import Any
app1: Any

from typewriter_intro import Intro

if __name__ == "__main__":
    try:
        effects = Intro.effect_intro(app1)
    except Exception as ex:
        print(f"Erro: {ex}")
