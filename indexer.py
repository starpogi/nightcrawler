"""
Extracts information from a catalog, and indexes them into a native data structure
that allows other functions to pull and query data from.
"""
import camelot
from camelot import utils
import re
import pathlib
import typing

# Catalog Indexer
nomenclature = r'(?P<prefix>[A-Z\-]*)(?P<device_series>[98|99]+)(?P<device_type>\d+[WDC]*)(?P<trim>[A-Z\-]+)-(?P<rating>[F|Blank|M]+)'

# TODO: Make this configurable, and ability to choose catalog
headers_re = r'(?P<index>[0-9]+)\\n(?P<header>[A-Za-z ]+)'

def read_boundaries(filename: pathlib.Path, page: int) -> typing.Dict:
    detail_mapping = {}

    layout, dim = utils.get_page_layout(str(filename))

    tables = camelot.read_pdf(
        str(filename), 
        flavor='stream',
        pages=str(page),
        table_areas=['50,610,612,50']
    )
    table = tables[0]

    # TODO: Iterate through every table
    frame = table.df

    print(frame.loc[:, 0:1].to_string())

    return detail_mapping
