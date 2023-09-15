from geopandas import GeoDataFrame

from shapely.geometry import Point, Polygon




# def asd(gdf: GeoDataFrame, col_geom="geometry") -> GeoDataFrame:
#     """ """
#     assert isinstance(gdf, GeoDataFrame) and gdf.geom_type
#     return gdf["geometry"].apply(lambda g: Polygon([Point(c[:2]) for c in g.exterior.coords]))