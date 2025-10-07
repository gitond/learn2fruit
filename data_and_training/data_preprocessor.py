# Libraries
import json
import os

# Constants (Loading unformatted json)
ROOT = os.getcwd() + "/data/coco-2017/"
CDIR = "validation/"
with open(ROOT + CDIR + "labels.json", "r") as INFILE:
    DATA = json.load(INFILE)
CONVERSIONDICT = {49: 0, 50: 1, 51: 2, 52: 3, 53: 4, 55: 5}
# 49: knives, 50: spoons, 51: bowls, 52: bananas, 53: apples, 55: oranges


# "trim" labels; only keep annotations we're interested in
myAnnotations = []
for annotation in DATA["annotations"]:
	if (annotation["category_id"] in [49,50,51,52,53,55]):
		annotation["category_id"] = CONVERSIONDICT[annotation["category_id"]]
		myAnnotations.append(annotation)

# Save trimmed labels in separate json file
DATA["annotations"] = myAnnotations
with open(ROOT + CDIR + "trimmed_labels.json", "w") as OUTFILE:
    json.dump(DATA, OUTFILE)
