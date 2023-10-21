import os
import shutil
import logging
from s3 import S3FileHandler
from common import process_data

logging.basicConfig(level=logging.INFO)


def handle(file_key, url):
    logging.info(f"Retrieving data from URL {url} with key {file_key} ...")

    s3_bucket = os.environ["S3_BUCKET"]
    s3_endpoint = os.environ["S3_ENDPOINT"]
    s3_access_key = os.environ["S3_ACCESS_KEY"]
    s3_secret_key = os.environ["S3_SECRET_KEY"]

    df = process_data(url)
    df.info(memory_usage="deep")

    # Répertoire de travail pour les fichiers locaux
    working_dir = "working_directory"
    os.makedirs(working_dir, exist_ok=True)

    # Sauvegarder le fichier en local
    df.to_pickle(os.path.join(working_dir, file_key))

    # Utilisez la méthode upload() de S3FileHandler pour téléverser le fichier vers S3
    s3_handler = S3FileHandler(s3_bucket, s3_endpoint, s3_access_key, s3_secret_key)
    s3_handler.upload(os.path.join(working_dir, file_key), file_key)

    # Supprimez le répertoire de travail après avoir terminé
    shutil.rmtree(working_dir)

    logging.info(f"Retrieving data completed.")


if __name__ == "__main__":
    handle()
