# # Command example
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


# # print_node_external.py
# node = app.getNode("Text1")
#
# if node is None:
#     print("Erro: node 'Text1' não encontrado no projeto.")
# else:
#     for p in node.getParams():
#         if "text" in p.getScriptName().lower():
#             print(p.get())

