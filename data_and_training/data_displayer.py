# Libraries
import json
import os
from PIL import Image, ImageDraw

# Constants (Loading reference image)
ROOT = os.getcwd() + "/data/coco-2017/"
CDIR = "validation/"
with open(ROOT + CDIR + "labels.json", "r") as FILE:
    DATA = json.load(FILE)
IMGM = DATA["images"][1]
IMDC = Image.open(ROOT + CDIR + "data/" + IMGM["file_name"], "r")
DRAWMODE = "seg"	# "box" or "seg"
COLORDICT = {49:"purple",50:"blue",51:"green",52:"yellow",53:"red",55:"orange"}
# 49: knives, 50: spoons, 51: bowls, 52: bananas, 53: apples, 55: oranges


# Reference image exploration, processing, outputting
print("Exploring reference image:\n" + ROOT + CDIR + "data/" + IMGM["file_name"] + "\nWith id: " + str(IMGM["id"]))
print()
imgDrawer = ImageDraw.Draw(IMDC)

for annotation in DATA["annotations"]:
	if ((annotation["image_id"] == IMGM["id"]) and (annotation["category_id"] in [49,50,51,52,53,55])):
		print(annotation)
		print()

		# Drawing
		match DRAWMODE:
			case "box":
				imgDrawer.line([(round(annotation["bbox"][0]),round(annotation["bbox"][1])),(round(annotation["bbox"][0])+round(annotation["bbox"][2]),round(annotation["bbox"][1])),(round(annotation["bbox"][0])+round(annotation["bbox"][2]),round(annotation["bbox"][1])+round(annotation["bbox"][3])),(round(annotation["bbox"][0]),round(annotation["bbox"][1])+round(annotation["bbox"][3])),(round(annotation["bbox"][0]),round(annotation["bbox"][1]))], fill = COLORDICT[annotation["category_id"]], width = 2)
			case "seg":
				for pointlist in annotation["segmentation"]:
					if len(pointlist)%2 != 0:
						raise Exception('annotation["segmentation"] has odd number of numerical values, cannot form coordinates!')
					segCoordList = []
					for i in range(int(len(pointlist)/2)):
						segCoordList.append((round(pointlist[i*2]),round(pointlist[i*2+1])))
					segCoordList.append((round(pointlist[0]),round(pointlist[1])))
					imgDrawer.line(segCoordList, fill = COLORDICT[annotation["category_id"]], width = 0)
			case _:
				pass

print()
IMDC.show()
