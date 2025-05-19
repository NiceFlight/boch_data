import json
import glob
import os

cate_list = [
    # "antiquity",
    # "archaeologicalSite",
    "commemorativeBuilding",
    # "culturalLandscape",
    # "folklore",
    # "groupsOfBuildings",
    "historicalBuilding",
    # "historicSite",
    "monument",
    # "ote",
    # "ptp",
    # "tkp",
    # "traditionalCraft",
    # "traditionalPerformingart",
]

for cate in cate_list:
    _path = f"{cate}/*.json"
    print(_path)

    for path in glob.glob(_path):
        # print(path)
        name = path.split("\\")[-1].split(".")[0]
        print(f"讀取 {path}")

        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                geo_data = data["geojson"]
                geo_data = json.loads(geo_data)
                filePath = f"{cate}/{name}"
                os.makedirs(filePath, exist_ok=True)  #  create file if it doesn't exist

                for i in geo_data:

                    with open(
                        f"{filePath}/{i["features"][0]["properties"]["landLot"].strip()}.geojson",
                        "w",
                        encoding="utf-8",
                    ) as f:
                        json.dump(i, f, indent=4, ensure_ascii=False)
                        print(
                            f"{i["features"][0]["properties"]["landLot"].strip()} geojson 儲存成功！"
                        )
            except Exception as e:
                with open(f"{cate}_geojson_error.txt", "a", encoding="utf-8") as f:
                    f.write(f"{name} 沒有 geojson：{e}\n")
print(f"All done!!!")
