import requests
from bs4 import BeautifulSoup
import json
from models.AccountConfig import AccountConfig
import re


def parse_yuque_config(config_url: str) -> list[AccountConfig]:
    """解析语雀账号配置

    Args:
        yuque_doc_uid (str): 语雀文档uid

    Returns:
        set: 账号配置集合
    """
    try:
        book_id = get_book_id(config_url)
        if book_id == None:
            raise KeyError("获取配置book_id失败")
        doc_uid = config_url.split('/')[-1]
        url = f"https://www.yuque.com/api/docs/{doc_uid}?include_contributors=true&include_like=true&include_hits=true&merge_dynamic_data=false&book_id={book_id}"
        response = requests.get(url)
        data = json.loads(response.text)
        content = data['data']['content']
        print("表格内容："+content)
        soup = BeautifulSoup(content, "html.parser")
        configs = soup.find_all("table")
        rows = configs[0].find_all("tr")

        results = []
        for row in rows:
            cells = row.find_all("td")
            data = [cell.text for cell in cells]
            if data[0] == "序号":
                continue
            account = AccountConfig(data[2], data[1], int(data[0]), data[4], data[3])
            results.append(account)

        return results
    except Exception as err:
        print(err)
        raise ValueError("解析语雀配置失败") from err


def get_book_id(url: str) -> str:
    """获取book_id参数

    Args:
        url (str): _description_

    Returns:
        str: _description_
    """
    response = requests.get(url)
    match = re.search(r'book_id%22%3A(\d+)', response.text)
    if match:
        book_id = match.group(1)
        print(book_id)
        return book_id
    return None
