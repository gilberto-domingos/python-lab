import sys
sys.path.append("/home/gil/python3/natron_effects")
from typing import Any
app1: Any

from typewriter_logo import Logo

if __name__ == "__main__":
    try:
        effects = Logo.effect_logo(app1)
    except Exception as ex:
        print(f"Erro: {ex}")