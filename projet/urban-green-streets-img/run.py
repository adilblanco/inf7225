import click
from fetch_data import handle as main_fetch_data
from transform_data import handle as main_tranform_data

@click.command()
@click.option(
    '--command',
    required=True,
    type=click.Choice([
        'fetch_data', 
        'transform_data'
        ])
)
@click.option(
    '--url',
    type=str
)
@click.option(
    '--input_file_key',
    type=str
)
@click.option(
    '--output_file_key',
    type=str
)
@click.option(
    '--columns',
    type=str
)
def main(command, output_file_key, input_file_key, url, columns):
    if command == "fetch_data":
        main_fetch_data(output_file_key, url)
    elif command == "transform_data":
        main_tranform_data(input_file_key, output_file_key, columns)
        
if __name__ == '__main__':
    main()
