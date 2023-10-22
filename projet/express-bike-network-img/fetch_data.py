import os
import shutil
import logging
from s3 import S3FileHandler
from common import process_request, json_items_to_geodataframe

logging.basicConfig(level=logging.INFO)


def handle(output_file_key, url):
    logging.info(f"Retrieving data from URL {url} with key {output_file_key} ...")

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
    gdf.to_pickle(os.path.join(working_dir, output_file_key))

    # Utilisez la méthode upload() de S3FileHandler pour téléverser le fichier vers S3
    s3_handler = S3FileHandler(s3_bucket, s3_endpoint, s3_access_key, s3_secret_key)
    s3_handler.upload(os.path.join(working_dir, output_file_key), output_file_key)

    # Supprimez le répertoire de travail après avoir terminé
    shutil.rmtree(working_dir)

    logging.info(f"Retrieving data completed.")


if __name__ == "__main__":
    handle()
