# Wrapper for _create_tf_record_from_coco_annotations from
# create_coco_tf_record.py . Get original source file from
# https://github.com/tensorflow/models/blob/master/research/object_detection/dataset_tools/create_coco_tf_record.py

# Requires a version of TensorFlow's object_detection library with protos
# compiled with protoc; This is a very challenging installation process

#########################################
# Manual object_detection installation: #
#########################################

################ PROCESS ################

# Make sure you're on a TensorFlow compatible Python version (3.10/3.11/3.12)
#python -V

# Make sure you have no conflicting pip-based object_detection install
#python -m pip uninstall object_detection

# Clone the TensorFlow models repo (or use your existing clone).
#git clone https://github.com/tensorflow/models.git && cd models/research

# Compile the object_detection protos. This requires the protoc compiler.
#protoc object_detection/protos/*.proto --python_out=.

# Install the local object_detection package (no deps).
#python3 -m pip install --no-deps .

# Verify the proto module imports before running the script.
#from object_detection.protos import string_int_label_map_pb2

#########################################

# Library & Tool imports
from create_coco_tf_record import _create_tf_record_from_coco_annotations
import os

# Constants
PROJECT_ROOT = os.getcwd()	# NOTE: ALWAYS RUN THIS FROM PROJECT ROOT (~/.../learn2fruit)
DSDIR = PROJECT_ROOT + "/data_and_training/data/coco-2017/"




### json to tfrecord conversion ###

# Command format:
#_create_tf_record_from_coco_annotations(annotations_file, image_dir,
#output_path, include_masks,
#num_shards,
#keypoint_annotations_file='',
#densepose_annotations_file='',
#remove_non_person_annotations=False,
#remove_non_person_images=False)

# About include_masks:
# We just want to use the trained ai to detect where the trackable objects are;
# at this point no need to do instance segmentation. I'll leave this as False
# for the time being.

# About num_shards:
# I'll just follow the tensorflow object detection example
# (https://www.tensorflow.org/tfmodels/vision/object_detection) and set this
# to 1.

# The actual commands:
_create_tf_record_from_coco_annotations(DSDIR + "/train/trimmed_labels.json", DSDIR + "/train/data", DSDIR + "/train/tfrecords/", False, 1)
_create_tf_record_from_coco_annotations(DSDIR + "/test/labels.json", DSDIR + "/test/data", DSDIR + "/test/tfrecords/", False, 1)
_create_tf_record_from_coco_annotations(DSDIR + "/validation/trimmed_labels.json", DSDIR + "/validation/data", DSDIR + "/validation/tfrecords/", False, 1)
