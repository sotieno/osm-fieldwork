import os
from io import BytesIO
from osm_fieldwork.basemapper import create_basemap_file

# Get path to tests folder
tests_folder = os.path.join(os.path.dirname(__file__), 'tests')

# Construct path to geojson file
geojson_path = os.path.join(tests_folder, 'testdata', 'Salida.geojson')

with open(geojson_path, "rb") as geojson_file:
    boundary = geojson_file.read()  # read as a `bytes` object.
    boundary_bytesio = BytesIO(boundary)   # add to a BytesIO wrapper
    print(type(boundary_bytesio))

if isinstance(boundary_bytesio, BytesIO):
    create_basemap_file(
        verbose=True,
        boundary=boundary_bytesio,
        outfile="outreachy.mbtiles",
        zooms="12-15",
        source="esri",
    )
else:
    print("boundary_bytesio is not a valid BytesIO object")
