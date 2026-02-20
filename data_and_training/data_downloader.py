import argparse
import fiftyone
import os

parser = argparse.ArgumentParser()
parser.add_argument("--max_samples", type=int, default=50,
                    help="Maximum number of samples to download per split")
args = parser.parse_args()

# Configuring download folder
fiftyone.config.dataset_zoo_dir = os.getcwd() + "/data"

# Downloading data
dataset = fiftyone.zoo.load_zoo_dataset(
	"coco-2017",
	splits=["train","validation","test"],
	label_types=["detections","segmentations","keypoints"],
	classes=["bowl","spoon","knife","banana","apple","orange"],
	max_samples=args.max_samples,
)
