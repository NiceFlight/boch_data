import json

filePath = r"monument_geojson_error.txt"

with open(filePath, "r", encoding="utf-8") as f:
    content = f.readlines()
    # print(content)

    for line in content:
        if "沒有 geojson：'landLot'" in line:
            # with open("selected_monument_geojson.txt", "a", encoding="utf-8") as f:
            #     f.write(line)
            caseName = line.split(" 沒有")[0]
            print(caseName)
            with open(f"monument/{caseName}.json", "r", encoding="utf-8") as f:
                data = json.load(f)["geojson"]
                # print(data)
                data = data.replace("\\", "")
                # print(data)
                json_data = json.loads(data[1:-1])
                # print(json_data)

                with open(
                    f"monument/{caseName}/{caseName}.geojson",
                    "w",
                    encoding="utf-8",
                ) as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)
