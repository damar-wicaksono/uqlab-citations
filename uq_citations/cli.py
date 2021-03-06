# -*- coding: utf-8 -*-
"""Module with the command line interface of the uq_citations package.
"""
import click

from .parse_bibtex import parse_bibtex
from .parse_biblist import parse_biblist
from .write_html import write_html
from .write_latex import write_latex
from .constants import SUBJECTS_DICT


@click.command()
@click.argument("bibtex", type=click.File("rt", encoding="utf-8"))
@click.option(
    "--html_tpl",
    default="./html_tpl.html",
    help="HTML template.",
    show_default=True)
@click.option(
    "--html_list",
    default="./bib_list.html",
    help="HTML list template.",
    show_default=True)
@click.option(
    "--output",
    default="./output.html",
    help="HTML output filename.",
    show_default=True)
def bibtex2html(bibtex, html_tpl, html_list, output):
    """Convert BibTeX file of UQLab citations to a HTML file."""

    # Parse the BibTeX file and return a list
    bib_db_entries = parse_bibtex(bibtex)

    # Process the list of citations
    biblist_entries = parse_biblist(bib_db_entries)

    # Write the list of citations into a file
    write_html(biblist_entries, SUBJECTS_DICT, html_tpl, html_list, output)


@click.command()
@click.argument("bibtex", type=click.File("rt", encoding="utf-8"))
@click.option(
    "--latex_tpl",
    default="./latex_tpl.tex",
    help="LaTeX template.",
    show_default=True)
@click.option(
    "--latex_list",
    default="./latex_list.tex",
    help="LaTeX list template.",
    show_default=True)
@click.option(
    "--output",
    default="./output.tex",
    help="LaTeX output filename.",
    show_default=True)
def bibtex2tex(bibtex, latex_tpl, latex_list, output):
    """Convert BibTeX file of UQLab citations to a LaTeX file."""

    # Parse the BibTeX file and return a list
    bib_db_entries = parse_bibtex(bibtex)

    # Process the list of citations
    biblist_entries = parse_biblist(bib_db_entries)

    # Write the list of citations into a file
    write_latex(biblist_entries, SUBJECTS_DICT, latex_tpl, latex_list, output)
