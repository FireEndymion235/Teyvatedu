
import aiosmtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from conf import config
from webcore.logcontroller import log
# STMP Server
smtp_server = config.STMP_SERVER
# STMP User
from_addr = config.STMP_USER
# STMP Password
password = config.STMP_PASS

async def send_email(send_to_addr:str,
                     send_to_name:str,
                     subject:str,
                     contest_msg:str):
    # connect to smtp server
    server = aiosmtplib.SMTP(hostname=smtp_server, port=465,use_tls=True)
    # esablish connection with smtp server
    await server.connect()
    # login
    await server.login(from_addr, password)
    # config email content

    msg = MIMEMultipart()
    msg['From'] = Header(config.APP_NAME)    # from
    msg['To'] = Header(send_to_name)      # to
    msg['Subject'] = Header(subject, 'utf-8')  # title and subject
    # content
    msg.attach(MIMEText(contest_msg, 'html', 'utf-8'))
    # send email
    log.debug(f'Sending email to {send_to_addr}...')
    await server.sendmail(from_addr, send_to_addr, msg.as_string())
    # close connection
    await server.quit()

async def send_email_log(send_to_addr:str,
                     send_to_name:str,
                     subject:str,
                     contest_msg:str,
                     filename:str):

    server = aiosmtplib.SMTP(hostname=smtp_server, port=465,use_tls=True)
    await server.connect()
    await server.login(from_addr, password)


    msg = MIMEMultipart()
    msg['From'] = Header(config.APP_NAME)
    msg['To'] = Header(send_to_name)
    msg['Subject'] = Header(subject, 'utf-8')

    msg.attach(MIMEText(contest_msg, 'html', 'utf-8'))

    image_file_name = filename
    image_file = MIMEImage(open(image_file_name, 'rb').read())
    image_file.add_header('Content-Type', 'application/octet-stream')
    image_file.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', image_file_name))
    msg.attach(image_file)
    log.debug(f'Sending email to {send_to_addr}...')
    await server.sendmail(from_addr, send_to_addr, msg.as_string())
    await server.quit()
