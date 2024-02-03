import requests
from bs4 import BeautifulSoup
import json
from models.AccountConfig import AccountConfig


def parse_yuque_config(yuque_doc_uid: str) -> set:
    """解析语雀账号配置

    Args:
        yuque_doc_uid (str): 语雀文档uid

    Returns:
        set: 账号配置集合
    """
    try:
        url = f"https://www.yuque.com/api/docs/{yuque_doc_uid}?include_contributors=true&include_like=true&include_hits=true&merge_dynamic_data=false&book_id=37366329"
        response = requests.get(url)
        data = json.loads(response.text)
        content = data['data']['content']
        print("表格内容："+content)
        soup = BeautifulSoup(content, "html.parser")
        configs = soup.find_all("table")
        rows = configs[0].find_all("tr")

        results = set()
        for row in rows:
            cells = row.find_all("td")
            data = [cell.text for cell in cells]
            if data[0] == "序号":
                continue
            account = AccountConfig(data[1], data[2], int(data[0]), data[3])
            results.add(account)

        return results
    except Exception as err:
        print(err)
        raise ValueError("解析语雀配置失败") from err
