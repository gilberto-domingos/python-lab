import sys
sys.path.append("/home/gil/python3/natron_effects")
from typing import Any
app1: Any

from typewriter_title import Title

if __name__ == "__main__":
    try:
        effects = Title.effect_title(app1)
    except Exception as ex:
        print(f"Erro: {ex}")