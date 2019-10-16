uqlab-citations
===============

Project to keep track of the external citations of UQLab_.


The project contains command line utilities to convert the list of citations stored in a BibTeX file
into an HTML page (as shown in the UQLab `publications page`_

Google Scholar
--------------

Google Scholar is used to track the UQLab citation.

BibTeX file
-----------

The full list of UQLab external citations is stored in a BibTeX file.
The file contains only citations that explicitly mentioned that UQLab has been used in the work.
Therefore, this excludes works that merely mention UQLab.

The file ``uqlab-citations.bib`` inside the folder ``./bib`` contains the latest list of UQLab external citations.

BibTeX2HTML
-----------

The command line utility ``uq_citations_bibtex2html`` is used to create a list of citations as an HTML page.
The utility requires the following:

- the BibTeX file (containing only the UQLab external citations)
- the html list template file (included as ``./templates/bib_list.html``)
- the html page template file (included as ``./template/html_tpl.html``)

To show the help of the utility, type:

.. code-block:: bash
   
   uq_citations_bibtex2html --help

.. _UQLab: http://www.uqlab.com/
.. _`publications page`: https://uqlab.com/publications
