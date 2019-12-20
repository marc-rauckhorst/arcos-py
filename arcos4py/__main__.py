# Main 
# __version__ = "0.1.6"

if __name__ == "__main__":
    main()


    from configparser import ConfigParser
    from importlib import resources  # Python 3.7+
    import sys
    import numpy as np
    import pandas as pd
    import geopandas as gpd
    from shapely.geometry import Polygon, Point
    import requests
    from pandas.io.json import json_normalize

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
