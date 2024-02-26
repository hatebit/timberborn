layer = QgsProject.instance().mapLayersByName('Height')[0]
layer.features

data_location = """D:/repository/python/timberborn/world.json"""
style_location = """D:/repository/python/timberborn/depth.qml"""
import json
file = open(data_location)
json = json.load(file)
map_size = json['Singletons']['MapSize']['Size']
x = map_size['X']
y = map_size['Y']
entities = json['Entities']
print(len(entities))
templates = set()
for entity in entities:
    template = entity['Template']
    templates.add(template)

print(templates)