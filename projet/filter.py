import os
import click
import shutil
import logging
import pandas as pd

from s3 import S3FileHandler
from common import prepare_data

logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    '--command',
    required=True,
    type=click.Choice(['filter_data'])
)
@click.option(
    '--in_file_key',
    required=True,
    type=str
)
@click.option(
    '--columns', 
    required=False,
    type=str
)
@click.option(
    '--out_file_key',
    required=True,
    type=str
)
def main(command, in_file_key, out_file_key, columns):
    if command == "filter_data":
        handle(in_file_key, out_file_key, columns)


def handle(in_file_key, out_file_key, columns):
    logging.info(f"Filtering columns {columns} from {in_file_key} to {out_file_key} ...")

    s3_bucket = os.environ["S3_BUCKET"]
    s3_endpoint = os.environ["S3_ENDPOINT"]
    s3_access_key = os.environ["S3_ACCESS_KEY"]
    s3_secret_key = os.environ["S3_SECRET_KEY"]

    # Répertoire de travail pour les fichiers locaux
    working_dir = "tmp"
    os.makedirs(working_dir, exist_ok=True)

    # Utilisez la méthode upload() de S3FileHandler pour téléverser le fichier vers S3
    s3_handler = S3FileHandler(s3_bucket, s3_endpoint, s3_access_key, s3_secret_key)
    s3_handler.download(in_file_key, os.path.join(working_dir, in_file_key))

    gdf = pd.read_pickle(os.path.join(working_dir, in_file_key))
    gdf = prepare_data(gdf)

    if columns:
        columns = columns.split()
        gdf = gdf.loc[:, columns]

    # Sauvegarder le fichier en local
    gdf.to_pickle(os.path.join(working_dir, out_file_key))

    s3_handler.upload(os.path.join(working_dir, out_file_key), out_file_key)
    
    # Supprimez le répertoire de travail après avoir terminé
    shutil.rmtree(working_dir)
    
    logging.info(f"Filtering for {in_file_key} completed. File exported as {out_file_key}.")


if __name__ == "__main__":
    main()
