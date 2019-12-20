"""Arcos4Py 

Arcos4Py is a direct wrapper for the Washington Post's ARCOS DEA dataset

    >>> import arcos4py as arcos
    >>> national_arcos_df = arcos.national_data_with_geo()

See https://github.com/marc-rauckhorst/ARCOS4PY for more information
"""
#import importlib_resources as _resources

#try:
#    from configparser import ConfigParser as _ConfigParser
#except ImportError:  # Python 2
#    from ConfigParser import ConfigParser as _ConfigParser


import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Polygon, Point
import requests
from pandas.io.json import json_normalize

__version__ = "0.2.1"


us_abbr_list = [
    "AK",
    "AL","AR","AZ", "CA","CO","CT","DE","FL","GA",
    "HI",
    "IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND",
    "NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA",
    "VT","WA","WI","WV","WY"]

us_48_abbr_list = [
    #"AK",
    "AL","AR","AZ", "CA","CO","CT","DE","FL","GA",
    #"HI",
    "IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND",
    "NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA",
    "VT","WA","WI","WV","WY"]

from arcos4py import raw_data
from arcos4py import supplemental_data
from arcos4py import summary_data
from arcos4py import national_aggregates