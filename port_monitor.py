# coding=utf8
import socket,time,smtplib
from email.mime.text import MIMEText

mail_to_list=["aaa@aaa.com"]
mail_host="smtp.xxx.com"
mail_user="xxx@xxx.com"
mail_pass="xxx"

def send_mail(subject, content):
  me="PortNotify"+"<"+mail_user+">"
  msg = MIMEText(content,'plain','utf8') 
  msg['Subject'] = unicode(subject, 'utf-8')
  msg['From'] = me
  msg['To'] = ";".join(mail_to_list)
  try:
      server = smtplib.SMTP()
      server.connect(mail_host)
      server.login(mail_user,mail_pass)
      server.sendmail(me, mail_to_list, msg.as_string())
      server.close()
      return True  
  except Exception, e:  
      print e
      return False  

def main():
  file_obj = open('ip.txt')
  for line in file_obj:
    timenow=time.localtime()
    datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
    ip = line.split()[0]
    port = int(line.split()[1])
    print "%s:%s try..." %(ip,port)
    try:
      sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      sc.settimeout(2)
      sc.connect((ip,port))
      logstr="%s:%s success %s \n" %(ip,port,datenow)
      print logstr
      sc.close()
    except Exception, e:  
      print str(e)
      file=open("log.txt", "a")
      logstr="%s:%s failure %s \n" %(ip,port,datenow)
      print logstr
      subject = "[重要] 发现 %s:%s 端口异常（%s）"%(ip,port,datenow)
      send_mail(subject, logstr)
      file.write(logstr)
      file.close()

main()
