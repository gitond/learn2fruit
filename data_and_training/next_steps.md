`data_pipeline.sh`:
everything that needs to be done to the data before training, starting with downloading, trimming, turning into tfrecords etc. Currently following this official tensorflow guide: https://www.tensorflow.org/tfmodels/vision/object_detection and attempting to integrate this script to my project: https://github.com/tensorflow/models/blob/master/research/object_detection/dataset_tools/create_coco_tf_record.py

`mobilenet_trainer.py`:
using the preformatted data: train a mobilenet-ssd-v2 with the preformatted data and save it in a tensorflow.js format
