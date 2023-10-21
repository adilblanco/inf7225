import os
import click
import shutil
import logging

from s3 import S3FileHandler
from common import process_request, json_items_to_geodataframe

logging.basicConfig(level=logging.INFO)

WGS84=4326
MTM8=32188

@click.command()
@click.option(
    '--command',
    required=True,
    type=click.Choice(['fetch_geo'])
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
    if command == "fetch_geo":
        handle(file_key, url)


def handle(file_key, url):
    logging.info(f"Retrieving the GEOJSON file from URL {url} with key {file_key} ...")
    
    s3_bucket = os.environ["S3_BUCKET"]
    s3_endpoint = os.environ["S3_ENDPOINT"]
    s3_access_key = os.environ["S3_ACCESS_KEY"]
    s3_secret_key = os.environ["S3_SECRET_KEY"]
        
    http_response = process_request(url)
    gdf = json_items_to_geodataframe(http_response)
    gdf.info(memory_usage="deep")
    
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

    logging.info(f"Geolocation File retrieval for {file_key} completed.")


if __name__ == "__main__":
    main()
