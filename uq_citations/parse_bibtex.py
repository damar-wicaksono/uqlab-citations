# -*- coding: utf-8 -*-
"""Module with functions to parse BibTeX file of UQLab citations
"""
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

__author__ = "Damar Wicaksono"


def parse_bibtex(bibtex_file):
    """Parse BibTeX file of citations and return a list"""
    bib_parser = BibTexParser()
    bib_parser.customization = convert_to_unicode
    bib_db = bibtexparser.load(bibtex_file, parser=bib_parser)
    
    # Sort the list in reverse chronological order by year
    bib_db.entries.sort(key=lambda x: x['year'], reverse=True)

    return bib_db.entries
