import click

from . import parse_bibtex
from . import parse_biblist

@click.command()
@click.argument("bibtex", type=click.File("rt"))
@click.option("--html_head", help = "HTML head template.")
@click.option("--html_list", help = "HTML list template.")
@click.option("--output", default="./output.html", help="HTML output filename.")
def bibtex2html(bibtex, html_head, html_list, output):
    """Convert BibTeX file of UQLab citations to a HTML file"""
    bib_db_entries = parse_bibtex.parse_bibtex(bibtex)
    
    biblist_entries = parse_biblist.parse_biblist(bib_db_entries)
    
    for entry in biblist_entries:
        print(entry["subject"])

if __name__ == "__main__":
    bibtex2html()
