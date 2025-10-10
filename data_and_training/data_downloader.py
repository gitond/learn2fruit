import fiftyone
import os

# Configuring download folder
fiftyone.config.dataset_zoo_dir = os.getcwd() + "/data"

# Downloading data
dataset = fiftyone.zoo.load_zoo_dataset(
	"coco-2017",
	splits=["train","validation","test"],
	label_types=["detections","segmentations","keypoints"],
	classes=["bowl","spoon","knife","banana","apple","orange"],
	max_samples=50,
)
