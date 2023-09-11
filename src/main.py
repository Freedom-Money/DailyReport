import tiktok_utils


if __name__ == "__main__":
    list = ['i_jou96', 'dock_me_']

    proxy = {
        'http': '127.0.0.1:10501',
        'https': '127.0.0.1:10501'
    }
    
    cookie =''
    result = ""
    users = []
    for item in list:
        info = tiktok_utils.getUserInfo(item, cookie, proxy)
        users.append(info)
        result += info.toString()

    pass
