import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.spatial import cKDTree
from geopy.distance import distance

WGS84 = 4326
MTM8 = 32188


def process_data(url):
    df = pd.read_csv(url)
    return df


def prepare_data(gdf):
    gdf.columns = gdf.columns.str.lower()
    gdf_mtm8 = gdf.to_crs(epsg=MTM8)
    return gdf_mtm8


def create_geodataframe(df):
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)).set_crs(f"epsg:{WGS84}")
    return gdf


def calculate_nearest_fountains_info(row, gdf):
    point = row['geometry']
    closest_point = row['closest_point']
    distance_meters = distance((point.y, point.x), (closest_point.y, closest_point.x)).meters
    closest_fountain_id = gdf[gdf['geometry'] == closest_point]['id'].values[0]
    return pd.Series({'distance_meters': distance_meters, 'closest_fountain_id': closest_fountain_id})


def get_nearest_fountains(gdf):
    # Create a KDTree from the geometry of the GeoDataFrame
    tree = cKDTree(np.array(gdf.geometry.apply(lambda geom: [geom.x, geom.y])).tolist())
    # Query the tree for the closest points to each point in the GeoDataFrame
    distances, indices = tree.query(np.array(gdf.geometry.apply(lambda geom: [geom.x, geom.y])).tolist(), k=2)
    # Get the closest point for each row
    gdf['closest_point'] = gdf.geometry.iloc[indices[:, 1]].values
    return gdf
