# Main (Raw) Functions
# __version__ = "0.1.1"
from configparser import ConfigParser
from importlib import resources  # Python 3.7+
import sys

import raw
import supplemental
import summary
import national


if __name__ == "__main__":
    main()