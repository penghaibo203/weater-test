import requests
import json
import _md5

#get请求的用法
# url = "http://v.juhe.cn/weather/index"
# param = "key=56cb1e1d6fb09c9b527a12b52dd94df7&cityname=深圳"
# response = requests.get(url, param)
# print(response.json())

#post请求的用法
# url = "http://v.juhe.cn/historyWeather/citys"
# payload = {"key":"d391709bada01c89be6dba753752bcd5","province_id":16}
# #jsondata = json.dumps(payload)
# response = requests.post(url, data=payload)

#获取省份
url = "http://v.juhe.cn/historyWeather/province"
#参数
param = "key=d391709bada01c89be6dba753752bcd5"
res = requests.get(url,param)
jsonRes = res.json()
reason = jsonRes.get("reason")
# print(reason)
province_id = 1
city_id = 1
if "查询成功" == reason :
    result = jsonRes.get("result")
    for i in range(len(result)):
        json = result[i]
        # print(json.get("province"))
        province = json.get("province")
        if("广东" == province):
            province_id = json.get("id")
            break
#获取城市
url = "http://v.juhe.cn/historyWeather/citys"
payload = {"key":"d391709bada01c89be6dba753752bcd5","province_id":province_id}
res = requests.post(url, data=payload)
jsonRes = res.json()
print(jsonRes)





