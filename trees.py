path_to_data = 'Baumstandort.csv'
gdf = geopandas.read_file(path_to_data, GEOM_POSSIBLE_NAMES="geometry", KEEP_GEOM_COLUMNS="NO")