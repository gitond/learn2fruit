### DEPENDENCIES ###
# Python libraries (pip install or standard library):
# __future__, argparse, contextlib, fiftyone, hashlib, io, json, logging,
# numpy, os, PIL, pycocotools, tensorflow

# Python files:
# devtools/create_coco_tf_record.py	from https://github.com/tensorflow/models/blob/master/research/object_detection/dataset_tools/create_coco_tf_record.py

# Modified python libraries (manual installing):
# object_detection			(instructions in: devtools/cocoann2tfrecord.py)



# Assuming this is run learn2fruit/data_and_training/



### DOWNLOADING DATA ###
python3 data_downloader.py
# Note: line 13 has a `max_samples` variable. This may limit how much data is
# downloaded. Make sure you aren't limited by this.

# Current datastructure:
# data/
# └── coco-2017/
#     └── split/
#         ├── data/
#         └── labels.json
# , where:
# split ∈ {train,test,validation}



### STRIPPING DATA ###
# While `data_downloader` only downloads images relevant to us, We have plenty
# of annotations of classes we don't need. I made a python script to remove the
# unnecessary data
python3 data_preprocessor.py data/coco-2017/train
python3 data_preprocessor.py data/coco-2017/validation

# Modified datastructure:
# data/
# └── coco-2017/
#     └── split/
#         ├── data/
#         ├── labels.json
#         └── trimmed_labels.json
# , where:
# split ∈ {train,validation}



### DATA TO TFRECORD ###
# The tensorflow object detection api needs the data in a format called tfrecord
# Tensorflow has a coco-json to tfrecord converter. I made a driver for it.

# Let's modify the datastructure for my driver
mkdir data/coco-2017/train/tfrecords
mkdir data/coco-2017/test/tfrecords
mkdir data/coco-2017/validation/tfrecords

# Now let's run my driver
python3 devtools/cocoann2tfrecord.py

# And let's deal with the annoyingly named output file it produces
for split in "train" "test" "validation"; do
	mv data/coco-2017/"$split"/tfrecords/-00000-of-00001 data/coco-2017/"$split"/tfrecords/"$split".record;
done

# Current datastructure should look like:
# data/
# └── coco-2017/
#     ├── split/
#     │   ├── data/
#     │   ├── labels.json
#     │   └── trimmed_labels.json	# This doesn't exist in the test split!
#     └── tfecords
#         └── split.record
# , where:
# split ∈ {train,test,validation}
