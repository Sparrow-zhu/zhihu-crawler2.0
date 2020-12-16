import requests

def get_data(url):
    '''
    功能：访问 url 的网页，获取网页内容并返回
    参数：
        url ：目标网页的 url
    返回：目标网页的 html 内容
    '''

    # 用'cookie'模拟登录网页解决跳转登录的问题！
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'cookie': '''_zap=5af1d8c0-fbdc-4de4-9e41-190de568d21d; _xsrf=c5479e9c-866a-494e-8d8d-f0707d5043e4; d_c0="ANDRQfB1eBGPTqmQ4kihicWKnJywGW7C9XA=|1592921756"; _ga=GA1.2.504778147.1592921761; tst=h; tshl=; l_n_c=1; n_c=1; l_cap_id="NDgyOTZjNjU3M2NjNGZlZDhhOGM2NzhhYTE1ZTQ5MTM=|1605869815|f102f844358d7fcbd027d752cc6897255d8751a5"; r_cap_id="Zjk5YmMzZWM0NDJlNGNmNGIwMmEzOTlmNjRlOWYwOTc=|1605869815|10efa7ebaf58e63b10e1ef8b30cbebf40ce4d087"; cap_id="NjlkMWQ4MDUzN2Q2NDdiM2E0ZTc2ZDhkMDkwZGM2NmM=|1605869815|bfc0053415e365ecb67ad47c6272257560cfa39e"; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20180309=1^3=entry_date=20180309=1; q_c1=0618fdc555614340b32cc006ab8c0bd5|1606821757000|1594393532000; capsion_ticket="2|1:0|10:1607334279|14:capsion_ticket|44:MzJlNjQyNmM4NmZhNDY2Yjg0ZjI0MDBjZDU2MmViMGE=|1e269243eadcc867303b30ad3b424de0975bc9ddc79548632ff31d63fb809b62"; z_c0="2|1:0|10:1607334296|4:z_c0|92:Mi4xbU1JZENBQUFBQUFBME5GQjhIVjRFU2NBQUFDRUFsVk5tSWIxWHdBTTBSd0VoWUh6Y0M2NUF2eDVGVjZTVXJhQUF3|dddf59e82a7a6f47c9b1fde516d4b3acf8f1c2156f97296223b200a727fed40a"; __utma=51854390.504778147.1592921761.1606446798.1607399670.2; __utmz=51854390.1607399670.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/349474297/answer/1423622054; SESSIONID=OfegczPBeyklhXfystDblMcCOVMLlafhYPNsWd1oWYd; JOID=VFEUAEkn1U_TA89QRSJeVUnQa9dTZ7sotWS6CAVGoyy9apM5NHecg4kIyFpGipJFdw5M45qpO20n8Ph0W154ZQA=; osd=UVwTB0gi2EjUAspdQiVfUETXbNZWarwvtGG3DwJHpiG6bZI8OXCbgowFz11Hj59CcA9J7p2uOmgq9_91XlN_YgE=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1607418776,1607481249,1607568449,1607568851; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1607580617; KLBRSID=b33d76655747159914ef8c32323d16fd|1607581133|1607580598'''
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error !")