import json
import urllib.request, urllib.error,http.cookiejar  # 制定URL，获取网页数据
import urllib.parse as parse


if __name__ == '__main__':
    url='https://bkjw.cuc.edu.cn/jwapp/sys/xsbysj/modules/zdjsgl/jsjbxx.do'
    formdata = {
        'ZGH':1728
    }
    data = urllib.parse.urlencode(formdata).encode("utf-8")
    cookie='EMAP_LANG=zh; THEME=cherry; _WEU=mqg51uEf401E8q3yKwCQiOUdmMPeMog_ewYAOG0wIZ4LoaC6WY1XLo3iQUApvAfsXvUn6QJytDRtD4*lOszQvU43jKbOYnel; MOD_AUTH_CAS=MOD_AUTH_ST-906789-BWzbmSWDQlPRGCYdhAem-cL0gZosso0004; JSESSIONID=hDbmp_FFRWMTRBjYANYVM-rhNjKEXexTZgY4-QusYtGT3rrDLdqq!-2120649942'
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
    }
    req = urllib.request.Request(url, headers=headers, data=data)


    try:
        resp = urllib.request.urlopen(req)
        html = resp.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):  # hasattr（e,"code“): 判断e这个对象里面是否包含code这个属性
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    try:
        response = json.loads(html)
        print(response)
    except:
        print('error')

