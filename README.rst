uqlab-citations
===============

Project to keep track of the external citations of UQLab_.
External citations of UQLab exclude publications made
by the current members of the Chair of Risk, Safety and Uncertainty Quantification
and only include works that explicitly used UQLab, not merely citing it.

The project contains command line utilities to convert the list of citations stored in a BibTeX file
into an HTML page (as shown in the UQLab `publications page`_ 
or a short PDF report with some numbers and figures.

Installation
------------

Use the package manager pip_ to install the python package ``uq_citations``
from the cloned source directory::

   pip install 

or for editable mode::

   pip install -e .

Successful installation will make the following command line utilities available in the path:

- ``uq_citations_bibtex2html``
- ``uq_citations_bibtex2pdf``


BibTeX2HTML
-----------

The command line utility ``uq_citations_bibtex2html`` is used to create a list of citations as an HTML page.
The utility requires the following:

- the BibTeX file (containing only the UQLab external citations)
- the html list template file (included as ``./templates/bib_list.html``)
- the html page template file (included as ``./template/html_tpl.html``)

To show the help of the utility, type:

.. codeblock:: bash
   
   uq_citations_bibtex2html --help

Additional Notes
----------------

Google Scholar
~~~~~~~~~~~~~~

Google Scholar is used to track the UQLab citation.

BibTeX file
~~~~~~~~~~~

The full list of UQLab external citations is stored in a BibTeX file.
The file contains only citations that explicitly mentioned that UQLab has been used in the work.
Therefore, this excludes works that merely mention UQLab.

The file ``uqlab-citations.bib`` inside the folder ``./bib`` contains the latest list of UQLab external citations.

.. _UQLab: http://www.uqlab.com/
.. _`publications page`: https://uqlab.com/publications
.. _pip: https://pip.pypa.io/en/stable/
