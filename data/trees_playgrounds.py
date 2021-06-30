import matplotlib.pyplot as plt
import geopandas

# Load playground data
path_to_playground= '/Users/reka/Desktop/knowing_humnas_knowing_data/collab/Spielplatz.csv'
gdf_pg = geopandas.read_file(path_to_playground, GEOM_POSSIBLE_NAMES="geometry", KEEP_GEOM_COLUMNS="NO")

path_to_data = '/Users/reka/Desktop/knowing_humnas_knowing_data/collab/Baumstandort.csv'
gdf_trees = geopandas.read_file(path_to_data, GEOM_POSSIBLE_NAMES="geometry", KEEP_GEOM_COLUMNS="NO")

#gdf_trees.plot(marker='.', color='green', markersize=5)

#gdf_pg.plot(marker="d", color='#F18805', markersize=5)


zurich = geopandas.read_file('/Users/reka/Desktop/zurich_new/data/stzh.adm_verwaltungsquartiere_a.shp')
#zurich.plot()
#plt.show()

base = zurich.plot(color='#C2CAEB', edgecolor='white')

gdf_trees.plot(ax=base, marker='.', color='green', markersize=8, alpha = .075);
gdf_pg.plot(ax=base, marker='d', color='#F18805', markersize=15)

plt.show()

