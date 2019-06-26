#!/usr/bin/env python
"""
Django administration utility.
"""

from __future__ import absolute_import
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "edxsearch.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
