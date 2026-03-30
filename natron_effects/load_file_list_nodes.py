import sys
sys.path.append("/home/gil/python3/natron_effects")
from typing import Any
app1: Any

from list_nodes import ListNodes

if __name__ == "__main__":
    try:
        effects = ListNodes.list_nodes(app1)
    except Exception as ex:
        print(f"Erro: {ex}")
