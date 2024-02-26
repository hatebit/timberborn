data_location = """D:/repository/python/timberborn/world.json"""
style_location = """D:/repository/python/timberborn/depth.qml"""
import json
file = open(data_location)
json = json.load(file)
map_size = json['Singletons']['MapSize']['Size']
x = map_size['X']
y = map_size['Y']
depths = json['Singletons']['WaterMap']['WaterDepths']['Array'].split()
print(str(x) + ' ' + str(y))

layer = QgsVectorLayer('Point', 'Depth', 'memory')
provider = layer.dataProvider()
provider.addAttributes([QgsField('depth',  QVariant.Double)])
QgsProject.instance().addMapLayer(layer)
index = 0
layer.startEditing()
for yy in range(y):
    for xx in range(x):
        f = QgsFeature()
        f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(xx,yy)))
        f.setAttributes([depths[index]])
        provider.addFeature(f)
        index+=1
layer.commitChanges()

layer.loadNamedStyle(style_location)