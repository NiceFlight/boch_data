import json

filePath = r"historicalBuilding_geojson_error.txt"

with open(filePath, "r", encoding="utf-8") as f:
    content = f.readlines()
    # print(content)

    for line in content:
        if "沒有 geojson：'landLot'" in line:
            with open(
                "selected_historicalBiuilding_geojson.txt", "a", encoding="utf-8"
            ) as f:
                f.write(line)
            caseName = line.split(" 沒有")[0]
            with open(
                f"historicalBuilding/{caseName}.json", "r", encoding="utf-8"
            ) as f:
                data = json.load(f)["geojson"]
                data = data.replace("\\", "")
                json_data = json.loads(data[1:-1])

                with open(
                    f"historicalBuilding/{caseName}/{caseName}.geojson",
                    "w",
                    encoding="utf-8",
                ) as f:
                    json.dump(json_data, f, indent=4)
