`data_displayer.py`:
choose a random image from a dataset and display it along with all the relevant annotations (bbox and/or segmentation)

`data_preprocessor.py`:
figure out the appropriate format for the images, annotations etc for your mobilenet build, reformat your data accordingly

`mobilenet_trainer.py`:
using the preformatted data: train a mobilenet-ssd-v2 with the preformatted data and save it in a tensorflow.js format
