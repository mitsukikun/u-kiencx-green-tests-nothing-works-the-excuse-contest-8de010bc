import os

line = (
    "All green: my tests never test the product, "
    "they just ask the code if it's working — "
    "and the code always says yes."
)
# Limit: at most 139 characters.
assert len(line) <= 139

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
