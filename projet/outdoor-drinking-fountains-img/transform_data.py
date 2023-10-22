import os
import shutil
import logging
import pandas as pd

from s3 import S3FileHandler
from common import create_geodataframe

logging.basicConfig(level=logging.INFO)


def handle(file_key, input_file_key, columns):
    logging.info(f"Starting transformation from file_key: {file_key} to {input_file_key} ...")

    s3_bucket = os.environ["S3_BUCKET"]
    s3_endpoint = os.environ["S3_ENDPOINT"]
    s3_access_key = os.environ["S3_ACCESS_KEY"]
    s3_secret_key = os.environ["S3_SECRET_KEY"]

    # Répertoire de travail pour les fichiers locaux
    working_dir = "tmp"
    os.makedirs(working_dir, exist_ok=True)

    # Utilisez la méthode download() de S3FileHandler pour télécharger le fichier à partir du S3
    s3_handler = S3FileHandler(s3_bucket, s3_endpoint, s3_access_key, s3_secret_key)
    s3_handler.download(file_key, os.path.join(working_dir, file_key))

    df = pd.read_pickle(os.path.join(working_dir, file_key))
    gdf = create_geodataframe(df)
    gdf.columns = gdf.columns.str.lower()
    
    if columns:
        columns = columns.split()
        columns = [col.strip() for col in columns]
        gdf = gdf.drop(columns=columns)
    
    # Sauvegarder le fichier en local, utilisez la méthode upload() de S3FileHandler pour téléverser le fichier vers S3
    gdf.to_pickle(os.path.join(working_dir, input_file_key))
    s3_handler.upload(os.path.join(working_dir, input_file_key), input_file_key)

    # Supprimez le répertoire de travail après avoir terminé
    shutil.rmtree(working_dir)

    logging.info(f"Transformation data completed.")


if __name__ == "__main__":
    handle()
