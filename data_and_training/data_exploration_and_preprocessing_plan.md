
After running `data_downloader.py` as is on July 15, 2025, 5PM, we get the following datastructure:

```
data/
└── coco-2017
    ├── info.json
    ├── raw
    │   ├── captions_train2017.json
    │   ├── captions_val2017.json
    │   ├── image_info_test2017.json
    │   ├── image_info_test-dev2017.json
    │   ├── instances_train2017.json
    │   ├── instances_val2017.json
    │   ├── person_keypoints_train2017.json
    │   └── person_keypoints_val2017.json
    ├── test
    │   ├── data
    │   └── labels.json
    ├── train
    │   ├── data
    │   └── labels.json
    └── validation
        ├── data
        └── labels.json
```

Exploring from `data/coco-2017/`:

In `info.json`: 
 - Dataset metadata featuring: 
   - size
   - splits
   - classes
   - fiftyone metadata

`raw/captions_train2017.json` and `raw/captions_val2017.json` follow the following structure:
```json
{
  "info": {
    "description": "string",
    "url": "string",
    "version": "string",
    "year": "number",
    "contributor": "string",
    "date_created": "string"
  },
  "licenses": {
    "_type": "array",
    "items": {
      "url": "string",
      "id": "number",
      "name": "string"
    }
  },
  "images": {
    "_type": "array",
    "items": {
      "license": "number",
      "file_name": "string",
      "coco_url": "string",
      "height": "number",
      "width": "number",
      "date_captured": "string",
      "flickr_url": "string",
      "id": "number"
    }
  },
  "annotations": {
    "_type": "array",
    "items": {
      "image_id": "number",
      "id": "number",
      "caption": "string"
    }
  }
}
```

---

`raw/image_info_test2017.json` and `raw/image_info_test-dev2017.json` have the same `info`, and `licenses` structures as `raw/captions_train2017.json` and `raw/captions_val2017.json`, but they have no `annotations` and instead have the following  `categories` array:
```json
{
    "categories": {
        "_type": "array",
        "items": {
            "supercategory": "string",
            "id": "number",
            "name": "string"
        }
    }
}
```
also the `images` structure is a bit different (`flickr_url` property missing):
```json
{  
	"images": {
    "_type": "array",
    "items": {
      "license": "number",
      "file_name": "string",
      "coco_url": "string",
      "height": "number",
      "width": "number",
      "date_captured": "string",
      "id": "number"
    }
  }
}
```

---

`raw/instances_train2017.json` and `raw/instances_val2017.json` have identical `info`, `licenses` and `images` structures as `raw/captions_train2017.json` and `raw/captions_val2017.json` and an identical `categories` structures as `raw/image_info_test2017.json` and `raw/image_info_test-dev2017.json`, however they have a bit more complicated `annotations` structure:

```json
{
    "annotations": {
        "_type": "array",
        "items": {
            "segmentation": "array",
            "area": "number",
            "iscrowd": "number",
            "image_id": "number",
            "bbox": "array",
            "category_id": "number",
            "id": "number"
        }
    }
}
```

Here `segmentation` is an array of arrays of numbers and `bbox` is an array of numbers.

---

`raw/person_keypoints_train2017.json` and `raw/person_keypoints_val2017.json` have identical `info`, `licenses` and `images` structures as  `raw/captions_train2017.json` and `raw/captions_val2017.json`. However they have the following `annotations` and `categories` structures:

```json
{
    "annotations": {
        "_type": "array",
        "items": {
            "segmentation": "array",
            "num_keypoints": "number",
            "area": "number",
            "iscrowd": "number",
            "keypoints": "array",
            "image_id": "number",
            "bbox": "array",
            "category_id": "number",
            "id": "number"
        }
    },
    "categories": {
        "_type": "array",
        "items": {
            "supercategory": "string",
            "id": "number",
            "name": "string",
            "keypoints": "array",
            "skeleton": "array"
        }
    }
}
```

In `annotations`: `segmentation` is an array of arrays of numbers and `bbox` and `keypoints` are arrays of numbers.

In `categories`: `keypoints` is an array of strings and `skeleton` is an array of arrays of numbers.

---

`test/data` and `train/data` have a bunch of `.jpg` images. 

In `train/data` and `validation/data` all images should be relevant (contain at least one of the wanted classes (bowl, spoon, knife, banana, apple, orange)). 

In `test/data` the images are for testing, so not all images even contain the wanted classes. But in `test/data` at least `000000000619.jpg` has bananas, so that specifc image should be flagged by the finished neural network as valid.

---

`test/labels.json` has identical `images`, `licenses` and `categories` structures as `raw/image_info_test2017.json` and `raw/image_info_test-dev2017.json`, but it has the following `info` structure:

```json
{
    "info": {
        "description": "string",
        "url": "string",
        "version": "string",
        "year": "number",
        "contributor": "string",
        "date_created": "string",
        "licenses": "array",
        "categories": "array"
    }
}
```

--- 

`train/labels.json` and `validation/labels.json` have an identical `info`, `licenses` and `categories` structures to  `test/labels.json` and an identical `images` and `annotations` structures as `raw/instances_train2017.json`.
