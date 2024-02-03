class AccountConfig:
    def __init__(self, uid: str, operater: str, number: int, remarks: str) -> None:
        """账号配置

        Args:
            uid (str): tiktok uid
            operater (str): 操作员姓名
            number (int): 序号
            remarks (str): 备注
        """
        self.uid = uid
        self.operater = operater
        self.number = number
        self.remarks = remarks
