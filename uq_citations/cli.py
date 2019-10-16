import click

from .parse_bibtex import parse_bibtex
from .parse_biblist import parse_biblist
from .write_html import write_html
from .constants import SUBJECTS_DICT

@click.command()
@click.argument("bibtex", type=click.File("rt"))
@click.option("--html_tpl", default="./html_tpl.html", help = "HTML template.")
@click.option("--html_list", default="./bib_list.html", help = "HTML list template.")
@click.option("--output", default="./output.html", help="HTML output filename.")
def bibtex2html(bibtex, html_tpl, html_list, output):
    """Convert BibTeX file of UQLab citations to a HTML file."""
    bib_db_entries = parse_bibtex(bibtex)
    
    biblist_entries = parse_biblist(bib_db_entries)
    
    write_html(biblist_entries, SUBJECTS_DICT, html_tpl, html_list, output)
    

if __name__ == "__main__":
    bibtex2html()
