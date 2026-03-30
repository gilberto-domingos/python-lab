from typing import Any
app1: Any


node = app1.getNode("Slogan")
viewer = app1.getViewer("Viewer1")
frame = viewer.getCurrentFrame()

if frame == 50 :
    print('Ok !, param was found !')
else:
    print('Error : Not Found')


