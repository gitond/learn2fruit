# Assuming you are running this from a python environment with access to the
# following libraries: fiftyone, json, os

# Downloading the data off of COCO
python3 data_downloader.py
# Note: line 13 has a `max_samples` variable. This may limit how much data is
# downloaded. Make sure you aren't limited by this.

# While `data_downloader` only downloads images relevant to us, We have plenty
# of annotations of classes we don't need. I made a python script to remove the
# unnecessary data
python3 data_preprocessor.py
# TODO: run this for all splits
