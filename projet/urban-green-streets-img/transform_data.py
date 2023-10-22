import os
import shutil
import logging
import pandas as pd
from s3 import S3FileHandler

logging.basicConfig(level=logging.INFO)


def handle(input_file_key, output_file_key, columns):
    logging.info(f"Starting transformation from file_key: {input_file_key} to {output_file_key} ...")

    s3_bucket = os.environ["S3_BUCKET"]
    s3_endpoint = os.environ["S3_ENDPOINT"]
    s3_access_key = os.environ["S3_ACCESS_KEY"]
    s3_secret_key = os.environ["S3_SECRET_KEY"]

    # Répertoire de travail pour les fichiers locaux
    working_dir = "tmp"
    os.makedirs(working_dir, exist_ok=True)

    # Utilisez la méthode download() de S3FileHandler pour télécharger le fichier à partir du S3
    s3_handler = S3FileHandler(s3_bucket, s3_endpoint, s3_access_key, s3_secret_key)
    s3_handler.download(input_file_key, os.path.join(working_dir, input_file_key))

    gdf = pd.read_pickle(os.path.join(working_dir, input_file_key))
    gdf.columns = gdf.columns.str.lower()
    gdf = gdf.set_crs('epsg:4326')
    gdf = gdf.rename(columns={"id_trc": "id"})    
    gdf['date_maj'] = gdf['date_maj'].apply(lambda x: pd.to_datetime(x, format='%Y%m%d').strftime('%Y-%m-%d') if x is not None else x)
    gdf['date_amenagement'] = gdf['date_amenagement'].apply(lambda x: pd.to_datetime(x, format='%Y%m%d').strftime('%Y-%m-%d') if x is not None else x)

    if columns:
        columns = columns.split()
        columns = [col.strip() for col in columns]
        gdf = gdf.drop(columns=columns)
        
    gdf.info(memory_usage="deep")

    # Sauvegarder le fichier en local, utilisez la méthode upload() de S3FileHandler pour téléverser le fichier vers S3
    gdf.to_pickle(os.path.join(working_dir, output_file_key))
    s3_handler.upload(os.path.join(working_dir, output_file_key), output_file_key)

    # Supprimez le répertoire de travail après avoir terminé
    shutil.rmtree(working_dir)

    logging.info(f"Transformation data completed.")


if __name__ == "__main__":
    handle()
