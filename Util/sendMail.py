import os

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from smtplib import SMTP_SSL


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sendMail(report):
    from_addr = '1111111@qq.com'
    password = 'wbyeyajkrthzbhaa'
    to_addr = ['Dzreal@126.com']
    smtp_server = 'smtp.qq.com'

    report_name = os.path.split(report)
    msg = MIMEText(report, 'html', 'utf-8')
    msg['From'] = _format_addr('测试报告 {} <{}>'.format(report_name, 'CI'))
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    server = SMTP_SSL(smtp_server, 465)

    try:
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        print("发送成功")
    except:
        raise UserWarning("发送失败")
    finally:
        server.quit()