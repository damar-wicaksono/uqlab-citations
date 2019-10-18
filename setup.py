from setuptools import setup, find_packages

setup(
    name="uq_citations",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        uq_citations_bibtex2html=uq_citations.cli:bibtex2html
        uq_citations_bibtex2tex=uq_citations.cli:bibtex2tex
    """
)
