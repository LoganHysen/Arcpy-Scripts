# Name: Export Feature Classes 02/10/21
# Description: Iterates through specified feature classes and exports to GeoDataBase
import arcpy

# Takes input features and turns them into a list
in_features = arcpy.GetParameterAsText(0)
in_list = in_features.split(";")
print(in_list)

# Takes input features and adds "FC" (Feature Class) to the end, then puts those values into a new list
data = []
for i in in_list:
    x = "".join([i, "FC"])
    data.append(x)
print(data)


out_path = arcpy.GetParameterAsText(1)

# Exports features to a new Feature Class with the string "FC" added to the name
for var in in_list:
    for y in data:
        arcpy.conversion.FeatureClassToFeatureClass(var, out_path, y)
