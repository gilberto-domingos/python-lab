################ Render and export ###############
###### path expample % sequence
 /home/gil/_Animes/frame_%04d.png

###### Writer conected last merge or node

Node ┐
     ├─> Merge1 (Over)
Node ┘---┐
         ├─> Merge2 (Over) ──> Write
Node ────┘

###### convert .png to mp4
#   ffmpeg -framerate 30 -i frame_%04d.exr -vf "scale=in_range=full:out_range=full" -pix_fmt rgb48le frame_%04d.png



# # Command example
# #color_param.set(1.0, 1.0, 1.0, 0.0, start_frame)
# /home/gil/Natron-2.5.0/bin/NatronRenderer /home/gil/_Animes/ShortsIntro.ntp -l /home/gil/python3/natron_effects/print_node_external.py

# Simple rule (remember this)
# What you want to do What to use
# Working with nodes             ->  NatronGui
# External engine/render/script  ->  NatronEngine

#----------------------------------
# # Script Editor
# Executes complete Python.
# Can create, modify, or animate nodes, parameters, keyframes, and even entire compositions.
# The script I gave you creates the Text Node (if it doesn't exist) and animates the text letter by letter, frame by frame.
#
# # Set Expression of the Text1 node
# Only used to set expressions as parameters, such as "message", "translateX", etc.
#
# Cannot create complex nodes or loops.
#
# You could use just a simple expression to animate text, but not for complete typewriter-style animation logic like the script does. ShortsIntro

# # Verificar objestos para usar do modulo Natron
# from NatronGui import *
#
# obj = app1.getNode("Text1")
# print(sorted(dir(obj)))

