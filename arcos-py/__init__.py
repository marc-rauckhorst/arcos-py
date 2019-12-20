"""Arcos-Py 

Arcos-Py

    >>> import arcospy as arcos
    >>> national_arcos_df = arcos.national_data_with_geo()

See https://github.com/marc-rauckhorst/ARCOSPY for more information
"""
import importlib_resources as _resources

#try:
#    from configparser import ConfigParser as _ConfigParser
#except ImportError:  # Python 2
#    from ConfigParser import ConfigParser as _ConfigParser

    
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon, Point
import requests
from pandas.io.json import json_normalize

import raw
import supplemental
import summary
import national
    
# Version of realpython-reader package
__version__ = "0.1.1"

# Read URL of feed from config file

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
