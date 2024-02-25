from datetime import datetime
import tiktok_utils
import sender.weixin_sender as weixin_sender
import os
import sys
import config
import pickle
import parse_yuque_config
import sender.email_sender as email_sender
import pandas as pd
import json
from models.AccountInfo import AccountInfo


def send_report(subject: str, body: str, file_path: str):
    """发送消息

    Args:
        subject (str): _description_
        body (str): _description_
        file_path (str): _description_
    """
    # 发送微信
    wxpusher_token = config.user_config['wxpusher_token']
    wechat_uid = config.user_config['wechat_uid']
    if (wechat_uid != None and wechat_uid != ""):
        tmp = weixin_sender.send(subject, body,  wxpusher_token, wechat_uid)
        print("发送微信成功")
        print(tmp)
    # 发送邮件
    receive_email = config.user_config['receive_email']
    if (receive_email != None and receive_email != ""):
        for item in receive_email:
            print(item)
            email_sender.send(
                os.environ['SEND_EMAIL'], os.environ['SEND_EMAIL_PASSWORD'], item, body, file_path)


def write_to_excel(data: list, file_path: str):
    """保存数据到excel

    Args:
        data (list): 数据
        file_path (str): 文件路径
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
        tmp_list = []
        for item in data:
            if item.is_valid == False:
                tmp_list.append([item.number, item.operater,
                                item.deviceId, item.uid, "-", "-", "-", "-"])
            else:
                tmp_list.append([item.number, item.operater, item.deviceId, item.uid,
                                item.video_change, item.like_change, item.fans_count, item.video_count])
        df = pd.DataFrame(tmp_list)
        df.columns = ['序号', '姓名', '机号', '账号', '今日视频量', '今日点赞量', '粉丝总数', '视频总数']
        df = df.sort_values(by='序号', ascending=True)
        df.to_excel(file_path, index=False)
    except Exception as err:
        print("保存文件错误")
        print(err)


def parse_settings(yml_name: str) -> bool:
    """获取系统设置

    Args:
        yml_name (str): actions配置文件名称

    Returns:
        bool: _description_
    """
    print(f"yml_name: {yml_name}")
    settings = []
    try:
        settings = json.loads(os.environ['SETTINGS'])
    except json.JSONDecodeError as err:
        print(f"解析参数失败，可能是参数格式设置错误\n:{err}")
        return False

    for item in settings:
        if item['name'] == yml_name or yml_name.split('#')[0] == item['name']:
            config.user_config['wechat_uid'] = item['wechat_uid']
            config.user_config['yuque_doc_url'] = item['settings_url']
            config.user_config['receive_email'] = item['receive_email']
            return True
    print(f"没有获取到 '{yml_name}' 对应的参数，请检查配置是否正确")
    return False


if __name__ == "__main__":
    try:
        # 读取项目配置
        tiktok_cookie = config.user_config['tiktok_cookie']

        args = sys.argv[1:]  # 排除脚本名称
        yml_name = args[0]
        if not parse_settings(yml_name):
            if yml_name != 'report_demo':
                raise Exception("获取配置失败")
            sys.exit(1)

        yuque_doc_url = config.user_config['yuque_doc_url']
        accounts = []
        try:
            accounts = parse_yuque_config.parse_yuque_config(yuque_doc_url)
        except Exception as err:
            print("获取语雀配置失败")
            send_report("TikTok日报 - 运行异常", "读取语雀配置错误，请检查配置", None)
            raise err
        doc_uid = yuque_doc_url.split('/')[-1]
        daily_data_file = os.path.abspath(f'{doc_uid}.pkl')
        data = None
        if os.path.exists(daily_data_file):
            # 打开保存对象的文件，使用二进制读取模式
            with open(daily_data_file, 'rb') as file:
                data = pickle.load(file)
        else:
            print(f"The file {daily_data_file} does not exist.")
        users = []
        result = ""
        for item in accounts:
            info = tiktok_utils.get_account_info(item, tiktok_cookie)
            if info == None:
                info = AccountInfo(item, None, 0, 0, 0, 0)
                info.set_invalid()
                print("用户uid配置错误，获取用户信息失败")
            else:
                yesterday = None
                try:
                    if data is not None:
                        for tmpItem in data:
                            if tmpItem.uid == info.uid:
                                yesterday = tmpItem
                                info.set_yesterday(int(yesterday.follow_count), int(yesterday.fans_count),
                                                   int(yesterday.like_count), int(yesterday.video_count))
                                break
                except Exception as err:
                    print('获取对比信息错误')
                    print(err)

            result += info.toString()
            users.append(info)

        # 保存文件
        with open(daily_data_file, 'wb') as file:
            pickle.dump(users, file)

        current_date = datetime.now().strftime("%Y%m%d")
        tmp_excel = f'TikTok_{current_date}.xlsx'
        write_to_excel(users, tmp_excel)
        send_report("TikTok日报", result, tmp_excel)

        # 删除excel文件
        if os.path.exists(tmp_excel):
            os.remove(tmp_excel)

    except Exception as err:
        print("运行错误")
        print(err)
