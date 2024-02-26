data_location = """D:/repository/python/timberborn/world.json"""
style_location = """D:/repository/python/timberborn/paths.qml"""
import json
file = open(data_location)
json = json.load(file)
map_size = json['Singletons']['MapSize']['Size']
x = map_size['X']
y = map_size['Y']
entities = json['Entities']
print(len(entities))

layer = QgsVectorLayer('Point', 'Paths', 'memory')
provider = layer.dataProvider()
provider.addAttributes([QgsField('type',  QVariant.String)])
QgsProject.instance().addMapLayer(layer)
layer.startEditing()

network_templates = [
    'Path.Folktails', 
    'WoodenStairs.Folktails', 
    'Slope',
    'SuspensionBridge3x1.Folktails'
]

for entity in entities:
    template = entity['Template']
    if template in network_templates:
        xx = entity['Components']['BlockObject']['Coordinates']['X']
        yy = entity['Components']['BlockObject']['Coordinates']['Y']
        f = QgsFeature()
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(xx,yy)))
        f.setAttributes([template])
        provider.addFeature(f)
layer.commitChanges()

layer.loadNamedStyle(style_location)