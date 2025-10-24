# Explore the structure of a .json file composed of objects and arrays
#
# For each top-level property:
# - If it's an object → list property types inside it
# - If it's an array of objects → mark as array and show types of first element
# - Otherwise → return the type as a string

with_entries(
  if (.value | type) == "object" then
    .value |= with_entries(.value |= type)
  elif (.value | type) == "array" and (.value[0] | type) == "object" then
    # Note: we assume that all objects in an array of objects have the same structure
    .value = {
      "_type": "array",
      "items": (.value[0] | with_entries(.value |= type))
    }
  else
    .value |= type
  end
)
