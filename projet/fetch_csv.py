import os
import click
import shutil
import logging
import pandas as pd
import geopandas as gpd
from s3 import S3FileHandler

logging.basicConfig(level=logging.INFO)

WGS84=4326
MTM8=32188

@click.command()
@click.option(
    '--command',
    required=True,
    type=click.Choice(['fetch_csv'])
)
@click.option(
    '--file_key',
    required=True,
    type=str
)
@click.option(
    '--url',
    required=True,
    type=str
)
def main(command, file_key, url):
    if command == "fetch_csv":
        fetch_csv(file_key, url)


def process_data(url):
    df = pd.read_csv(url)
    return df


def create_geodataframe(df):
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude)).set_crs(f"epsg:{WGS84}")
    return gdf


def fetch_csv(file_key, url):
    logging.info(f"Retrieving the CSV file from URL {url} with key {file_key} ...")
    
    s3_bucket = os.environ["S3_BUCKET"]
    s3_endpoint = os.environ["S3_ENDPOINT"]
    s3_access_key = os.environ["S3_ACCESS_KEY"]
    s3_secret_key = os.environ["S3_SECRET_KEY"]
    
    # url="https://donnees.montreal.ca/dataset/3ff400f3-63cd-446d-8405-842383377fb8/resource/26659739-540d-4fe2-8107-5f35ab7e807c/download/fontaine_eau_potable_v2018.csv"
    
    df = process_data(url)
    gdf = create_geodataframe(df)
    gdf.info()
    
    # Répertoire de travail pour les fichiers locaux
    working_dir = "working_directory"
    os.makedirs(working_dir, exist_ok=True)
    
    # Sauvegarder le fichier en local
    gdf.to_pickle(os.path.join(working_dir, file_key))
    
    # Utilisez la méthode upload() de S3FileHandler pour téléverser le fichier vers S3
    s3_handler = S3FileHandler(s3_bucket, s3_endpoint, s3_access_key, s3_secret_key)
    s3_handler.upload(os.path.join(working_dir, file_key), file_key)
    
    # Supprimez le répertoire de travail après avoir terminé
    shutil.rmtree(working_dir)


if __name__ == "__main__":
    main()
