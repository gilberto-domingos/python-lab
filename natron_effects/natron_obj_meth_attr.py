from NatronGui import *

output_file = "/home/gil/_Animes/natron_info_obj_meth_attr.txt"

def introspect(obj, name, file, level=0, visited=None):


    if visited is None:
        visited = set()

    if id(obj) in visited:
        return
    visited.add(id(obj))

    indent = "  " * level
    file.write(f"{indent}{name} : {type(obj)}\n")

    try:
        for attr_name in dir(obj):
            if attr_name.startswith("__") and attr_name.endswith("__"):
                continue

            try:
                attr_value = getattr(obj, attr_name)
            except Exception as e:
                file.write(f"{indent}  {attr_name} : <error accessing>\n")
                continue

            if callable(attr_value):
                file.write(f"{indent}  {attr_name}() : method\n")
            else:
                if isinstance(attr_value, (int, float, str, bool, list, tuple, dict, set)):
                    file.write(f"{indent}  {attr_name} : {type(attr_value)}\n")
                else:
                    introspect(attr_value, attr_name, file, level+1, visited)
    except Exception as e:
        file.write(f"{indent}<error listing dir of {name}>\n")

with open(output_file, "w", encoding="utf-8") as f:
    introspect(app1, "app1", f)

print(f"Complete introspection Objct, Meth, Attr saved in: {output_file}")