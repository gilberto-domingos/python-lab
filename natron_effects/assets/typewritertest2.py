app = natron.getGuiInstance(0) if natron.getGuiInstanceCount() > 0 else natron.createInstance()

project = app.getProject()

# ✅ RESOLUÇÃO CORRETA
project.getParam("projectWidth").setValue(1080)
project.getParam("projectHeight").setValue(1920)
project.getParam("pixelAspectRatio").setValue(1.0)

# duração
project.getParam("frameRange").setValue(1, 300)

# =========================
# NÓS
# =========================

bg = app.createNode("Constant")
bg.getParam("color").setValue([0, 0, 0, 1])

textNode = app.createNode("Text")

textNode.getParam("message").setValue(
    "Hello World!\nTypewriter Effect\nNatron 🚀"
)

textNode.getParam("font_size").setValue(80)
textNode.getParam("justify").setValue("center")
textNode.getParam("center").setValue([540, 960])

# =========================
# EXPRESSÃO
# =========================

expr = """
originalText = message
slowFac = 4

ptr = int(frame() / slowFac)
ptr = max(0, min(ptr, len(originalText)))

cursor = "|" if int(frame() % 20) < 10 else ""

ret = originalText[:ptr] + cursor
"""

textNode.getParam("message").setExpression(expr, True)

# =========================
# MERGE
# =========================

merge = app.createNode("Merge2")
merge.setInput(0, bg)
merge.setInput(1, textNode)

# =========================
# VIEWER
# =========================

viewer = app.createNode("Viewer")
viewer.setInput(0, merge)

app.setFrame(1)