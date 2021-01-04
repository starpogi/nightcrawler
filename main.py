import click
import indexer

@click.command()
@click.argument('path', type=click.Path())
@click.option('--page', default=4, help='Page to read')
def index(path: click.Path, page: int):
    """Indexes a catalog with a specified path."""
    click.echo(f"Indexing {path} at page {page}")
    indexer.read_boundaries(path, page)

if __name__ == '__main__':
    index()



