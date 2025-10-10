# Libraries
import argparse
import json
import os

# Constants (Loading unformatted json)
ROOT = os.getcwd()
PARSER = argparse.ArgumentParser("learn2fruit_data_preprocessor", description="Takes a directory with a COCO formatted labels.json, produces new trimmed_labels.json file in the same directory which only contains annotations where the category_id is present in an internal CONVERSIONDICT variable. Also rewrites old category_id to the range [0,len(CONVERSIONDICT)-1]")
PARSER.add_argument("CDIR")
ARGS = PARSER.parse_args()
CDIR = ARGS.CDIR
with open(ROOT + "/" + CDIR + "/labels.json", "r") as INFILE:
    DATA = json.load(INFILE)
CONVERSIONDICT = {49: 0, 50: 1, 51: 2, 52: 3, 53: 4, 55: 5}
# 49: knives, 50: spoons, 51: bowls, 52: bananas, 53: apples, 55: oranges


# "trim" labels; only keep annotations we're interested in
myAnnotations = []
for annotation in DATA["annotations"]:
	if (annotation["category_id"] in list(CONVERSIONDICT.keys())):
		annotation["category_id"] = CONVERSIONDICT[annotation["category_id"]]
		myAnnotations.append(annotation)

# Save trimmed labels in separate json file
DATA["annotations"] = myAnnotations
with open(ROOT + "/" + CDIR + "/trimmed_labels.json", "w") as OUTFILE:
    json.dump(DATA, OUTFILE)
