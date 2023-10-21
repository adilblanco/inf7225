import click
from fetch_data import handle as main_fetch_data
from transform_data import handle as main_tranform_data

@click.command()
@click.option(
    '--command',
    required=True,
    type=click.Choice([
        'fetch_data', 
        'transform_data', 
        'load_data'])
)
@click.option(
    '--url',
    type=str
)
@click.option(
    '--file_key',
    required=True,
    type=str
)
@click.option(
    '--optional_file_key',
    type=str
)
def main(command, file_key, url, optional_file_key):
    if command == "fetch_data":
        main_fetch_data(file_key, url)
    elif command == "transform_data":
        main_tranform_data(file_key, optional_file_key)
        
if __name__ == '__main__':
    main()
