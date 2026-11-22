"""Task 3: how many DIFFERENT pages were requested in each hour?

A colleague wrote this job and says it works. It counts, for every hour of the
day, how many distinct HTML pages (paths ending in ``.html``) were requested
at least once in that hour.

Run it twice and compare:

    python3 run_job.py distinct_pages_per_hour --workers 1
    python3 run_job.py distinct_pages_per_hour --workers 4

Then fix it (see the README). Test it:
    python3 -m pytest tests/test_distinct_pages_per_hour.py
"""

from mapreduce import parse_line

SORT_BY = "key"

# "Optimization": remember what we have already sent so we do not send
# the same page twice. Fewer pairs means a smaller shuffle!
# already_sent = set()


def mapper(line):
    request = parse_line(line)
    if request is None or not request["path"].lower().endswith(".html"):
        return
    page = request["path"]
    yield request["hour"], page
    # if page not in already_sent:
    #     already_sent.add(page)
    #     yield request["hour"], page


def reducer(key, values):
    """Return the number of distinct pages in ``values``."""
    if isinstance(values, list):
        return len(set(values))
    return 0
