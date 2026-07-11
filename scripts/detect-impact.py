import yaml

with open(".github/documentation-map.yaml") as f:
    mapping = yaml.safe_load(f)

with open("changed-files.txt") as f:
    changed_files = f.readlines()

for changed in changed_files:

    changed = changed.strip()

    if changed in mapping["paths"]:

        print()
        print("Documentation Impact Found")
        print("--------------------------------")

        print(
            mapping["paths"][changed]
        )
