import pandas as pd
import geopandas as gpd

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
