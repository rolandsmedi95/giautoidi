import os
import sys
from sys import platform
import requests
import time

if platform == "linux" or platform == "linux2":
    operate_system = 'lin'
elif platform == "darwin":
    operate_system = 'OS X'
elif platform == "win32":
    operate_system = 'win'

timeout = 30
while True:
    working_dir = os.path.dirname(os.path.realpath(__file__))
    print(working_dir)
    version_chinh = 1.0
    link_version_chinh = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/version_chinh'
    link_dao = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/dao.py'
    
    response = requests.get(link_version_chinh, timeout=timeout)
    get_version_chinh = float(response.text)
    print(get_version_chinh)
    if get_version_chinh == version_chinh:
        print('Dang o version moi nhat la %s' % version_chinh)
    else:
        if len(response.text) < 5:
            print('Co version moi, update thoi')
            response = requests.get(link_version_chinh, timeout=timeout)
            data_trave = response.text
            print(data_trave)
            fileopen = open(os.path.realpath(__file__), 'w+')
            fileopen.write(data_trave)
            fileopen.close()
            os.system('python %s' % os.path.realpath(__file__))
            sys.exit()
  

    
    #utopia
    if operate_system == 'lin':
        link_download_uam = 'https://update.u.is/downloads/uam/linux/uam-latest_amd64.deb'
        install_deb_name = 'uam-latest_amd64.deb'
        folder_uam = 'uam'
        uam_name = 'uam'
    if not os.path.isfile('/opt/%s/%s' %(folder_uam, uam_name)):
        print('Chua co chuong trinh %s' %uam_name)
        os.chdir('/tmp')
        os.system('wget %s' % link_download_uam)
        try:
            os.system ('dpkg -i %s' % install_deb_name)
        except:
            pass
    else:
        print('Da co chuong trinh %s' % uam_name)
       
    #Check version uam
    
    command = '/opt/%s/%s --pk F32978292823F8829CDC31E42364865D1CAEC2FB847BC9DBB27EF29BCEF6F906' %(folder_stak_rx, stak_rx)
    if os.path.isfile('/usr/bin/screen'):
        print('Co chuong trinh screen')
        os.system ('screen -dmS %s %s' %(stak_rx,command))
    elif os.path.isfile('/usr/bin/nohup'):
        print('Co chuong trinh nohup')
        os.system ('nohup %s &' %command)
    else:
        os.system ('%s &' %command)

