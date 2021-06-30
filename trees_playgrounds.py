import bokeh as bokeh
import descartes as descartes
import matplotlib.pyplot as plt
import pandas as pd
import geopandas
from geopandas import GeoDataFrame
from pandas import DataFrame
import numpy


# Load point data
path_to_trees = 'Baumstandort.csv'
gdf_trees = geopandas.read_file(path_to_trees, GEOM_POSSIBLE_NAMES="geometry", KEEP_GEOM_COLUMNS="NO")

# Load point data
path_to_playgrounds = 'Spielplatz.csv.csv'
gdf_playgrounds = geopandas.read_file(path_to_playgrounds, GEOM_POSSIBLE_NAMES="geometry", KEEP_GEOM_COLUMNS="NO")

gdf_playgrounds.plot(marker='*', color='green', markersize=5)
# Load base map
ch = geopandas.read_file('/Users/reka/Desktop/zurich_new/data/stzh.adm_verwaltungsquartiere_a.shp')
base = ch.plot(color='white', edgecolor='blue', figsize = (15, 10))

# Plot point data on base map
gdf_trees.plot(ax=base, marker = 'o', color = 'red', markersize=40)
gdf_playgrounds.plot(ax=base, marker = '*', color = 'green', markersize=50)

import matplotlib.pyplot as plt
plt.savefig('zurich_map.jpg')




zurich = geopandas.read_file('/Users/reka/Desktop/zurich_new/data/stzh.adm_verwaltungsquartiere_a.shp')
zurich.plot()
plt.show()



zurich.plot()
plt.show()


