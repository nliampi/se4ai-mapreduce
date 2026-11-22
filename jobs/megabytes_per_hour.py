"""Task 2: how much data did the server send in each hour of the day?

Operators use this to plan capacity: when is the peak, and how big is it?

Count EVERY request that can be parsed, whatever its method or status.
The key is the hour of the day (an int from 0 to 23). The result for each
hour is the total reply size in megabytes (1 MB = 1,000,000 bytes), rounded
to 1 decimal place.

Run it:  python3 run_job.py megabytes_per_hour
Test it: python3 -m pytest tests/test_megabytes_per_hour.py
"""

from mapreduce import parse_line

SORT_BY = "key"  # run_job.py prints hours in order (0, 1, 2, ...) rather than by size


def mapper(line):
    """Yield ``(hour, bytes)`` for every request that can be parsed."""
    # TODO
    log_parsed = parse_line(line)
    if log_parsed is None:
        return
    yield log_parsed['hour'], log_parsed['bytes']


def reducer(key, values):
    """Return the total of ``values`` in megabytes, rounded to 1 decimal."""
    # TODO
    if isinstance(values, list):
        total_bytes = sum(values)
        total_megabytes = total_bytes / 1_000_000
        return round(total_megabytes, 1)
    # raise NotImplementedError("Task 2: write the reducer")
