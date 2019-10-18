# -*- coding: utf-8 -*-
"""Module with functions write a LaTeX file for the list of citations.
"""
import os
import yaml
import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader

__author__ = "Damar Wicaksono"


def create_latex_list(biblist_entries, html_list):
    """Write the list of citations in LaTeX syntax using  template."""

    pass


def create_latex_per_subject(biblist_entries, html_list, subject):
    """Create LaTeX list of citations and group by the subject"""

    pass


def get_total_number(biblist_entries: list):
    """Get the total number of citations."""
    return len(biblist_entries)


def get_citation_by_subgroup(biblist_entries: list, subject: dict):
    """Create a subject dictionary"""
    
    if 'members' in subject.keys():
        subgroups = subject['members']
    else:
        subgroups = [subject['name']]

    citations_by_subgroup = {k: [] for k in subject["members"]}

    for biblist_entry in biblist_entries:
        for subgroup in subgroups:
            if subgroup in biblist_entry["keywords"]:
                citations_by_subgroup[subgroup].append(biblist_entry["ID"])
                
    return citations_by_subgroup


def get_citation_by_subject(biblist_entries: list, subject: dict):
    """Create a subject dictionary"""

    if 'members' in subject.keys():
        subgroups = subject['members']
    else:
        subgroups = [subject['name']]

    entries = []
    citations = []
    
    for biblist_entry in biblist_entries:
        for subgroup in subgroups:
            if subgroup in biblist_entry["keywords"]:
                entries.append(biblist_entry)
                citations.append(biblist_entry["ID"])
                
    citation_by_subject = dict()
    citation_by_subject["subject"] = subject["name"].capitalize()
    citation_by_subject["count"] = len(entries)
    if entries != []:
        citations = [",".join(citations)]
        citations.insert(0, '\cite{')
        citations.append("}")
        citations = "".join(citations)
        citation_by_subject["citations"] = citations
    else:
        citation_by_subject["citations"] = 0

    return citation_by_subject


def get_citations_by_year(biblist_entries: list):
    """Get the number of citations by year."""
    citations_by_year = dict()
    for biblist_entry in biblist_entries:
        if biblist_entry["year"] in citations_by_year:
            citations_by_year[biblist_entry["year"]] += 1
        else:
            citations_by_year[biblist_entry["year"]] = 1

    return citations_by_year


def plot_citations_by_year(biblist_entries, output_filename):
    """Create a bar plot of citations by year."""
    
    citations_by_year = get_citations_by_year(biblist_entries)
    year = list(citations_by_year.keys())
    year.reverse()
    citations = list(citations_by_year.values())
    citations.reverse()
    plt.figure()
    plt.bar(year, citations, color="black")
    plt.savefig(output_filename,dpi=600)
    plt.close()

def write_latex(biblist_entries: list,
                subjects: list,
                latex_tpl: str,
                latex_list: str,
                output_filename: str):
    """Write the list of citations into an HTML file using templates."""

    # Create a list of citations group by subjects
 
    # Read report config file
    with open("config.yml") as f: 
        report_data = yaml.load(f, Loader=yaml.FullLoader)

    # Get some data from the list of citations
    citations_data = dict()
    citations_data["total"] = get_total_number(biblist_entries)
    citations_by_subjects = list(map(lambda subject: get_citation_by_subject(biblist_entries, subject), subjects))
    citations_data["subjects"] = citations_by_subjects

    #
    citations_by_subgroup = get_citation_by_subgroup(biblist_entries, subjects[2])
    num_citations_by_subgroup = {'subject': [u for u in citations_by_subgroup.keys()],
         'num_citations': [len(v) for v in citations_by_subgroup.values()]} 
    df = pd.DataFrame(data=num_citations_by_subgroup)
    ax = df.sort_values('num_citations', ascending=True).plot.barh(x = 'subject', y = 'num_citations', color="black", legend=False)
    fig = ax.get_figure()
    plt.yticks(rotation=45,fontsize=6)
    fig.savefig("citations_by_subgroup.png",dpi=600)


    # Create figures
    # Plot citations by subgroups
    plot_citations_by_year(biblist_entries, "citations_by_year.png")
    # Plot citations by subgroups
    
    # Read the html template file
    path_to_tpl, latex_tpl_filename = os.path.split(os.path.abspath(latex_tpl))
    file_loader = FileSystemLoader(path_to_tpl)
    latex_jinja_env = Environment(
        loader=file_loader,
        block_start_string='\BLOCK{',
        block_end_string='}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False
        )

    latex_tpl = latex_jinja_env.get_template(latex_tpl_filename)

    # Replace template with list citations
    output = latex_tpl.render(report = report_data["report"],
                              citations = citations_data)

    # Write down the full HTML in the output file
    with open(output_filename, "wt") as output_file:
        output_file.write(output)
