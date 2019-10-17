# -*- coding: utf-8 -*-
"""Module with functions to parse list of UQLab citations.
"""

__author__ = "Damar Wicaksono"


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
            dates = "{0:%B} {0:%d}-{1:%d}, {0:%Y}".format(
                start_date, end_date)
        else:
            # Event dates cross into two months
            dates = "{0:%B} {0:%d} - {1:%B} {1:%d}, {0:%Y}".format(
                start_date, end_date)

    return "{}".format(dates)


def convert_dashes(pages):
    """Convert double dashes into a unicode."""

    return pages.replace("--", "&ndash;")


def parse_author_names(author_names):
    """Convert author names into a (oxford) comma list."""

    authors = [name.strip() for name in author_names.split("and")]

    # Process "Last Name, First Name"
    for i, author in enumerate(authors):
        author = [x.strip() for x in author.split(",")]
        if len(author) > 2:
            # "last name, Jr/I/III/etc., first names"
            authors[i] = "{} {}, {}".format(author[2], author[0], author[1])
        if len(author) == 2:
            author.reverse()
            authors[i] = " ".join(author)

    # Process the last entry of author names and add "and"
    if len(authors) > 1:
        authors[-1] = "and {}".format(authors[-1])

    # Join multiple author names
    if len(authors) > 2:
        parsed_author_names = ", ".join(authors)
    elif len(authors) == 2:
        parsed_author_names = " ".join(authors)
    else:
        parsed_author_names = authors[0]

    return parsed_author_names


def parse_biblist(biblist):
    """Parse the list of citations."""

    biblist_out = biblist.copy()

    for i, entry in enumerate(biblist):
        # Parse author names
        biblist_out[i]["author"] = parse_author_names(entry["author"])

        # Convert dashes to unicode
        if "pages" in entry:
            biblist_out[i]["pages"] = convert_dashes(entry["pages"])

        # Convert conference date
        if entry["ENTRYTYPE"] == "inproceedings":
            biblist_out[i]["eventdate"] = convert_conference_date(
                entry["eventdate"])

    return biblist_out
