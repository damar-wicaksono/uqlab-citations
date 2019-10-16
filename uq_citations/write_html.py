# -*- coding: utf-8 -*-
"""Module with functions write an HTML file for the list of citations
"""
import os
from jinja2 import Environment, FileSystemLoader

__author__ = "Damar Wicaksono"


def create_html_list(biblist_entries, html_list):
    """Write the list of citations into an HTML using template"""
    path_to_tpl, html_list_filename = os.path.split(os.path.abspath(html_list))
    
    file_loader = FileSystemLoader(path_to_tpl)
    env  = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
    
    list_tpl = env.get_template(html_list_filename)
    
    output = list_tpl.render(bib_entries=biblist_entries)
    
    return output


def create_html_per_subject(biblist_entries, html_list, subject):
    """Create HTML list of citations and group by the subject"""
    
    splitgroup = subject['splitgroup']
    
    if 'members' in subject.keys():
        subgroups = subject['members']
    else:
        subgroups = [subject['name']]
    
    entries = []
    output = []
    
    for subgroup in subgroups:
        for biblist_entry in biblist_entries:
            if subgroup in biblist_entry['keywords']:
                entries.append(biblist_entry)
        if splitgroup:
            if entries != []:
                output.append('<h5>{}</h5>'.format(subgroup.capitalize()))
                output.append(create_html_list(entries, html_list))
                entries = []
    
    if not splitgroup:
        output.append('<h4>{}</h4>'.format(subject["name"].title()))
        output.append(create_html_list(entries, html_list))
    
    return "\n".join(output)
    

def write_html(biblist_entries, subjects, html_tpl, html_list, output_filename):
    """Write the list of citations into an HTML file using templates."""
    
    # Create a list of citations group by subjects
    html_per_subject = []
    for subject in subjects:
        html_per_subject.append(create_html_per_subject(biblist_entries, html_list, subject))
    html_per_subject = "\n".join(html_per_subject)
    
    # Read the html template file
    path_to_tpl, html_tpl_filename = os.path.split(os.path.abspath(html_tpl))
    file_loader = FileSystemLoader(path_to_tpl)
    env  = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
    html_tpl = env.get_template(html_tpl_filename)
    
    # Replace template with list citations
    output = html_tpl.render(citations_list=html_per_subject)
    
    # Write down the full HTML in the output file
    with open(output_filename,"wt") as output_file:
        output_file.write(output)
