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

from create_coco_tf_record import _create_tf_record_from_coco_annotations
