import requests
import json


headers = {
    "Referer": "https://nchdb.boch.gov.tw/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Dnt": "1",
    "Content-Type": "application/json",
    "Origin": "https://nchdb.boch.gov.tw",
    "Access_token": "9E9F5556-3C7C-4572-8D1E-B42E3CB7C1CC",
}
url = r"https://data.boch.gov.tw/api/assets/antiquity/20250507000003"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=1506&offset=0&query=%7B%22assetsClassifyType%22:null,%22classifyCode%22:%5B%221.1%22%5D,%22govInstitutionCode%22:null,%22belongCity%22:null,%22belongCityId%22:null%7D&sort=id&order=desc&classifyCode=1.1"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=6544&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22belongCityId%22:null,%22classifyCode%22:%5B%221.1%22,%221.2%22,%221.4%22,%221.3%22,%223.1%22,%223.2%22,%222.1%22,%226.1%22,%224.1%22,%224.2%22,%225.1%22,%225.2%22,%225.3%22,%227.1%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D%7D&sort=id&order=desc&classifyCode=1.1&classifyCode=1.2&classifyCode=1.4&classifyCode=1.3&classifyCode=3.1&classifyCode=3.2&classifyCode=2.1&classifyCode=6.1&classifyCode=4.1&classifyCode=4.2&classifyCode=5.1&classifyCode=5.2&classifyCode=5.3&classifyCode=7.1"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=1759&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%221.2%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null%7D&sort=id&order=desc&classifyCode=1.2"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=21&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%221.4%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null%7D&sort=id&order=desc&classifyCode=1.4"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=24&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%221.3%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null%7D&sort=id&order=desc&classifyCode=1.3"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=78&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%223.1%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null%7D&sort=id&order=desc&classifyCode=3.1"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=7&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%223.2%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null%7D&sort=id&order=desc&classifyCode=3.2"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=56&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%222.1%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null%7D&sort=id&order=desc&classifyCode=2.1"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=2645&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%226.1%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null,%22descAgeId%22:null%7D&sort=id&order=desc&classifyCode=6.1"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=247&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%224.1%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null,%22descAgeId%22:null%7D&sort=id&order=desc&classifyCode=4.1"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=299&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%224.2%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null,%22descAgeId%22:null%7D&sort=id&order=desc&classifyCode=4.2"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=253&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%225.1%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null,%22descAgeId%22:null%7D&sort=id&order=desc&classifyCode=5.1"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=22&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%225.2%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null,%22descAgeId%22:null%7D&sort=id&order=desc&classifyCode=5.2"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=4&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%225.3%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null,%22descAgeId%22:null%7D&sort=id&order=desc&classifyCode=5.3"
# url = r"https://data.boch.gov.tw/api/v2/assets/advancedSearch?limit=73&offset=0&query=%7B%22assetsClassifyType%22:null,%22govInstitutionCode%22:null,%22belongCity%22:null,%22classifyCode%22:%5B%227.1%22%5D,%22assetsTypeCode%22:%5B%5D,%22assetsClassifyCode%22:%5B%5D,%22buildingYearCode%22:%5B%5D,%22belongCityId%22:null,%22descAgeId%22:null%7D&sort=id&order=desc&classifyCode=7.1"
res = requests.get(url, headers=headers)

data = json.loads(res.text)

with open("ptp.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
