import requests

def wxpusher_send_by_webapi(msg,app_token,uid):
    """利用 wxpusher 的 web api 发送 json 数据包，实现微信信息的发送"""
    webapi = 'http://wxpusher.zjiecode.com/api/send/message'
    data = {
        "appToken":app_token,
        "content":msg,
        "summary":"Freedom&Money 日报", # 该参数可选，默认为 msg 的前10个字符
        "contentType":1,
        "uids":[ uid, ],
        }
    result = requests.post(url=webapi,json=data)
    return result.text

