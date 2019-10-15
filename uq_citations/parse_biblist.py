# -*- coding: utf-8 -*-
"""Module with functions to parse list of UQLab citations
"""

__author__ = "Damar Wicaksono"


SUBJECTS = ["electrical engineering",
            "computational science and engineering",
            "civil engineering",
            "sensors engineering",
            "mechanical engineering",
            "chemical engineering",
            "ocean engineering",
            "geomechanics",
            "geoscience",
            "nuclear engineering",
            "biomedical science",
            "material science and engineering",
            "biology",
            "energy engineering",
            "hydrology",
            "environmental engineering"]


def convert_conference_date(event_date):
    """Convert conference date
    
        from YYYY-MM-DD/YYYY-MM-DD to B DD-DD, YYYY
        
        where B is the full name of a month
    """
    from dateutil import parser
    
    two_dates = event_date.split("/")
    start_date = parser.parse(two_dates[0])
    end_date = parser.parse(two_dates[1])
    if start_date == end_date:
        # One-day event
        dates = "{0:%B} {0:%d}, {0:%Y}".format(start_date)
    else:
        if start_date.month == end_date.month:
            # Event does not cross into the next month
            dates = "{0:%B} {0:%d}-{1:%d}, {0:%Y}".format(start_date,end_date)
        else:
            # Event dates cross into two months
            dates = "{0:%B} {0:%d} - {1:%B} {1:%d}, {0:%Y}".format(start_date,end_date)
    
    return "{}".format(dates)


def convert_dashes(pages):
    """Convert double dashes into a unicode."""
    return pages.replace("--","&ndash;")


def parse_author_names(author_names):
    """Convert author names into a (oxford) comma list."""
        
    authors = [author_name.strip() for author_name in author_names.split("and")]
    
    # Process "Last Name, First Name"
    for i, author in enumerate(authors):
        author = [x.strip() for x in author.split(",")]
        if len(author) > 2:
            # "last name, Jr/I/III/etc., first names"
            authors[i] = "{} {}, {}".format(author[2], author[0], author[1])
        if len(author) == 2:
            author.reverse()
            authors[i] = " ".join(author)
            
    # Process 
    if len(authors) > 1:
        authors[-1] = "and {}".format(authors[-1])
    
    if len(authors) > 2:
        parsed_author_names = ", ".join(authors)
    elif len(authors) == 2:
        parsed_author_names = " ".join(authors)        
    else:
        parsed_author_names = authors[0]
    
    return parsed_author_names


def determine_subject(keywords, subjects=SUBJECTS):
    """determine the subject based on assigned keyword in BibTeX file
    
        Here are the conventions:
        1. "geosciences" consist of "geomechanics", "hidrology", and "geoscience"
        2. "material" science and engineering belongs to "mechanical engineering"
        3. "sensors engineering" belong to "monitoring and remote sensing"
    """
    geosciences = ["geomechanics", "hydrology", "geoscience", "environmental engineering"]
    mechanical = ["mechanical engineering", "material science and engineering"]
    monitoring = ["sensors engineering"]
    for subject in subjects:
        if subject in keywords.lower():
            if subject in geosciences:
                subject = "geosciences and enviromental engineering"
            if subject in mechanical:
                subject = "mechanical engineering"
            if subject in monitoring:
                subject = "monitoring and remote sensing"
            break
    
    return subject


def parse_biblist(biblist):
    """Parse the list of citations"""
    
    biblist_out = biblist.copy()
    
    for i, entry in enumerate(biblist):
        # Parse author names
        biblist_out[i]["author"] = parse_author_names(entry["author"])

        # Convert dashes to unicode
        if "pages" in entry:
            biblist_out[i]["pages"] = convert_dashes(entry["pages"])

        # Convert conference date
        if entry["ENTRYTYPE"] == "inproceedings":
            biblist_out[i]["eventdate"] = convert_conference_date(entry["eventdate"])

        # Assign subjects
        biblist_out[i]["subject"] = determine_subject(entry["keywords"])
            
    return biblist_out
