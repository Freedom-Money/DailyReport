import tiktok_utils
import weixin
import os
import config

if __name__ == "__main__":
    try:
        if config.user_config['switch_run']:
            tiktok_cookie = config.user_config['tiktok_cookie']
            wxpusher_token = config.user_config['wxpusher_token']
            wechat_uid = os.environ['WECHAT_UID']
            accounts = os.environ['TIKTOK_ACCOUNTS']

            list = accounts.split(',')
            users = []
            result = ""
            for item in list:
                info = tiktok_utils.getUserInfo(item, tiktok_cookie)
                if info == None:
                    print("获取用户信息失败")
                    result += "用户信息丢失:"+item
                else:
                    users.append(info)
                    print(item)
                    result += info.toString()

            weixin.wxpusher_send_by_webapi(
                result, "TikTok日报", wxpusher_token, wechat_uid)
        else:
            print('本次不执行')
    except Exception as err:
        print("运行错误")
        print(err)
