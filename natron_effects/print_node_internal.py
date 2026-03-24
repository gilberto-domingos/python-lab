from PySide.QtGui import *
from NatronGui import *

node = app1.getNode("Text1")

for p in node.getParams():
    if "text" in p.getScriptName().lower():
        print(p.get())