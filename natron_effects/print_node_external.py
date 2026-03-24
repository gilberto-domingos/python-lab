#  output_dir = "/home/gil/_Animes"
import os

node = app.getNode("Text1")

if node is None:
    print("Error: node 'Text1' not found in the project.")
else:
    for p in node.getParams():
        if "text" in p.getScriptName().lower():
            print(p.get())

output_dir = "/home/gil/_Animes"
os.makedirs(output_dir, exist_ok=True)

writer = app.createNode("Write")
if writer is None:
    print("Error: Could not create Writer Node.")
else:
    writer.setLabel("Text1_Writer")
    writer.setParam("file", os.path.join(output_dir, "Text1_####.png"))
    writer.setParam("format", "PNG")
    writer.setParam("compression", 0)
    writer.setParam("renderMask", 0)
    writer.setParam("firstFrame", 1)
    writer.setParam("lastFrame", 100)
    writer.setParam("useProjectFormat", False)
    writer.setParam("projectWidth", 1920)
    writer.setParam("projectHeight", 1080)
    print(f"Writer Node created successfully in: {output_dir}")


