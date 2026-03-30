app = app1

node = app.getNode("Logo")

color_param = node.getParam("color")

color_param.set(1.0, 0.0, 0.0, 1.0)

####################### Stroke color ######################

app = app1

node = app.getNode("Logo")

for p in node.getParams():
    name = p.getScriptName().lower()

    if "color" in name:
        print("Test:", name)
        try:
            p.setValueAtTime(1.0, 1, 0)
            p.setValueAtTime(0.0, 1, 1)
            p.setValueAtTime(0.0, 1, 2)
            p.setValueAtTime(1.0, 1, 3)
        except Exception as e:
            print("Error :", name, e)

# or animate interpolation
# stroke_color.setValueAtTime(1.0, end_frame, 0)  # R
# stroke_color.setValueAtTime(0.0, end_frame, 1)  # G
# stroke_color.setValueAtTime(0.0, end_frame, 2)  # B
# stroke_color.setValueAtTime(1.0, end_frame, 3)  # A