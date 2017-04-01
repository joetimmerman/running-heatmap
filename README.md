running-heatmap
=====================

Download a copy of your Garmin Connect data and create a Google Maps heatmap of your activities. 

Description
-----------
Thes Python3 scripts will pull your activities from Garmin Connect. If you download the data in the default format of .gpx, you can then create a heatmap
of all your activities. Note that this is a very early version, and hasn't been tested anywhere besides my computer, and with any data besides
my own.

Usage
-----
The main script is gcexport.py. Here is the useage: 

```
usage: gcexport.py [-h] [-v] [--version] [--username [USERNAME]]
                   [--password [PASSWORD]] [-c [COUNT]]
                   [-f [{gpx,tcx,original}]] [-d [DIRECTORY]] [-u] [-s] [-m]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  --version             print version and exit
  --username [USERNAME]
                        your Garmin Connect username (otherwise, you will be
                        prompted)
  --password [PASSWORD]
                        your Garmin Connect password (otherwise, you will be
                        prompted)
  -c [COUNT], --count [COUNT]
                        number of recent activities to download, or 'all'
                        (default: 1)
  -f [{gpx,tcx,original}], --format [{gpx,tcx,original}]
                        export format; can be 'gpx', 'tcx', or 'original'
                        (default: 'gpx')
  -d [DIRECTORY], --directory [DIRECTORY]
                        the directory to export to (default: './YYYY-MM-
                        DD_garmin_connect_export')
  -u, --unzip           if downloading ZIP files (format: 'original'), unzip
                        the file and removes the ZIP file
  -s, --skipvalidation  if running in gpx format, skips the validation step
  -m, --map             create heatmap of activities (experimental)
```

Examples:
`python gcexport.py -s -c all -m --username email@email.com --password thisismypassword` will download all activities, skips the validation step, and creates a heatmap of your activities. 


History
-------
The core of the gcexport.py was written by @kjkjava, and can be found here: https://github.com/kjkjava/garmin-connect-export. This version of the script was no longer working due to 
changes on Garmin's side -- @moderation fixed these issues in a fork here: https://github.com/moderation/garmin-connect-export. This version also didn't work for me, so I made additional
changes to get it working. I have since ported the code to Python3, implemented additional options, and added the Google heatmap functionality (heatmap.py and parse_coords.py).

