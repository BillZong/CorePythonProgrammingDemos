#!/usr/bin/env python

"""Answer for 11.4 in chapter 11."""


def total_minutes_from(h, m):
    """Total Minutes from hour and minute."""
    return h * 60 + m


def total_minutes_from_hour_comma_minute(hcm):
    """Convert HH:mm string to total minutes."""
    t = hcm.strip().split(':')
    if not t or len(t) < 2:
        return 0
    return total_minutes_from(int(t[0]), int(t[1]))

print total_minutes_from_hour_comma_minute('11: 25')
