import requests
import pandas as pd
import geopandas as gpd

WGS84=4326
MTM8=32188


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


def process_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def json_items_to_geodataframe(http_response):
    return gpd.GeoDataFrame().from_features(http_response).set_crs(f"epsg:{WGS84}")
