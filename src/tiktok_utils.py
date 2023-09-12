import re
import execjs
import urllib.parse
import re
import json
import requests
from enums import PlatformType
from models import UserInfo


def get_ms_token(cookie_str):
    """
    从cookie字符串中获取msToken的值
    :param cookie_str: 包含msToken的cookie字符串
    :return: msToken的值或None
    """
    pattern = re.compile(r'msToken=([^;]+)')
    match = pattern.search(cookie_str)
    if match:
        return match.group(1)
    else:
        return None


def get_sign(url, userAgent):
    with open('src/resources/tiktok/signer.js', 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)
    sign = ctx.call('sign', url, userAgent)
    return sign


def getUserInfo(username, cookie, proxies=None):
    try:
        headers = {
            "accept": "application/json, text/plain, */*",
            "cookie": cookie,
            "referer": "https://www.tiktok.com/",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }

        tmp_url = "https://www.tiktok.com/api/user/detail/?aid=1988&app_language=zh-Hans&app_name=tiktok_web&browser_language=zh-CN&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F113.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7159778424045831681&device_platform=web_pc&focus_state=false&from_page=user&history_len=17&is_fullscreen=false&is_page_visible=true&language=zh-Hans&os=windows&priority_region=TW&referer=&region=TW&screen_height=900&screen_width=1440&tz_name=Asia%2FShanghai&uniqueId={}&webcast_language=zh-Hans&msToken={}".format(
            username, get_ms_token(headers['cookie']))

        query = urllib.parse.urlparse(tmp_url).query
        sign = get_sign(query, headers['user-agent'])
        reqeust_url = tmp_url + "&X-Bogus=" + sign

        response = requests.get(url=reqeust_url, headers=headers, proxies=proxies)

        if not response.ok or len(response.text) == 0:
            return None
        json_result = json.loads(response.text, strict=False)

        return UserInfo(username,
                        json_result['userInfo']['user']['nickname'],
                        PlatformType.Tiktok,
                        None,
                        json_result['userInfo']['stats']['followingCount'],
                        json_result['userInfo']['stats']['followerCount'],
                        json_result['userInfo']['stats']['heartCount'],
                        json_result['userInfo']['stats']['videoCount'],)
    except Exception as err:
        return None
