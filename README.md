# PortMonitor
简单的端口检测脚本

1、在脚本同一个目录下创建ip.txt
2、编辑ip.txt，添加ip、port信息，每条信息一行，ip与port之间使用英文空格分隔。
3、创建cron，定时执行
```
01 * * * * cd /xxx/monitor && /usr/bin/python port_monitor.py >> /tmp/port_monitor.log 2>&1
```
