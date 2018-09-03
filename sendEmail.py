from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(name):
    from_addr = 'example@163.com'  # 替换成你打算用来发邮件的邮件地址
    password = '**********'  # 替换成你的邮箱密码
    to_addr = 'someone@someplace.com'  #替换成你想发到的邮箱地址
    smtp_server = 'smtp.163.com'  # smtp服务的服务器地址，163邮箱的是这个

    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr('可爱的小派 <%s>' % from_addr)
    msg['To'] = _format_addr(' 亲爱的小主人<%s>' % to_addr)
    msg['Subject'] = Header('来自树莓派的提示……', 'utf-8').encode()

    # 邮件正文是MIMEText:
    msg.attach(MIMEText('我刚看到了%s' % name, 'html', 'utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('./New friends/emmmm.jpg', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('test', 'jpg', filename='test.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    msg.attach(MIMEText('<html><body><h1>   </h1>' +
        '<p><img src="cid:0"></p>' +
        '</body></html>', 'html', 'utf-8'))

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

# send_email('test')
