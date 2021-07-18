box = {"height": 20, "width": 45, "length": 30}
print(box["height"])
print(box.get("width"))

box["weight"] = 1 # dodamo item
print(box)

box["height"] = 40 # spremenimo value
print(box)

box.pop("height") # odstranimo item
print(box)