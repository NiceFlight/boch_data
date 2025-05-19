import json
import os
import requests

headers = {
    "Referer": "https://nchdb.boch.gov.tw/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Dnt": "1",
    "Content-Type": "application/json",
    "Origin": "https://nchdb.boch.gov.tw",
    "Access_token": "9E9F5556-3C7C-4572-8D1E-B42E3CB7C1CC",
}

cate_list = [
    # "antiquity",
    # "archaeologicalSite",
    # "commemorativeBuilding",
    # "culturalLandscape",
    # "folklore",
    # "groupsOfBuildings",
    "historicalBuilding",
    # "historicSite",
    # "monument",
    # "ote",
    # "ptp",
    # "tkp",
    # "traditionalCraft",
    # "traditionalPerformingart",
]

for cate in cate_list:
    url = f"{cate}.json"
    os.makedirs(cate, exist_ok=True)
    with open(url, "r", encoding="utf-8") as f:
        data = json.loads(f.read())["rows"]

    for i in data:
        _name = i["caseName"]
        _caseId = i["caseId"]
        print(f"Name: {_name}")

        if not os.path.exists(f"{cate}/{_name}.json"):

            i_url = f"https://data.boch.gov.tw/api/assets/{cate}/{_caseId}"

            try:
                res = requests.get(i_url, headers=headers)
                if res.status_code == 200:
                    print(f"{_name} 連接成功")
                    data = json.loads(res.text)

                    with open(f"{cate}/{_name}.json", "w", encoding="utf-8") as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)
                        print(f"{_name} 下載成功")
            except Exception as e:
                with open(f"{cate}_error.txt", "a", encoding="utf-8") as f:
                    f.write(f"{_name}.json　下載失敗！\n")
        else:
            print(f"{_name}.json 已存在")
print("All data downloaded！")
