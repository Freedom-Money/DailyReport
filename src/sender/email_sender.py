import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText


def send(username: str, password: str, receiver: str, body: str, file_path: str):
    """发送邮件

    Args:
        username (str): 发送邮件的用户名
        password (str): 发送邮件的密码
        receiver (str): 接收邮件的地址
        body (str): 邮件正文
        file_path (str): 附件的路径
    """
    # 创建一个MIMEMultipart对象
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = receiver
    msg['Subject'] = 'TikTok日报'
    smtp_server = 'smtp-mail.outlook.com'
    port = 587

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 添加附件
    if file_path != None and file_path != "":
        attachment = MIMEBase('application', 'octet-stream')
        with open(file_path, 'rb') as file:
            attachment.set_payload(file.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition',
                              'attachment', filename=file_path)
        msg.attach(attachment)

    # 连接到SMTP服务器并发送邮件
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
