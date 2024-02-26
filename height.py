data_location = """D:/repository/python/timberborn/world.json"""
style_location = """D:/repository/python/timberborn/height.qml"""
import json
file = open(data_location)
json = json.load(file)
map_size = json['Singletons']['MapSize']['Size']
x = map_size['X']
y = map_size['Y']
heights = json['Singletons']['TerrainMap']['Heights']['Array'].split()
print(str(x) + ' ' + str(y))

layer = QgsVectorLayer('Point', 'Height', 'memory')
provider = layer.dataProvider()
provider.addAttributes([QgsField('height',  QVariant.Int)])
QgsProject.instance().addMapLayer(layer)
index = 0
layer.startEditing()
for yy in range(y):
    for xx in range(x):
        f = QgsFeature()
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(xx,yy)))
        f.setAttributes([heights[index]])
        provider.addFeature(f)
        index+=1
layer.commitChanges()

layer.loadNamedStyle(style_location)