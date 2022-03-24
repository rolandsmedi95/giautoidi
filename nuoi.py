import json
import os
import random
import string
import subprocess
import threading
import time
from sys import platform
from random import randint
import re

working_dir = os.path.dirname(os.path.realpath(__file__))

'''
if operate_system == 'linux':
    os.system('apt update -y')
    os.system('apt install python3-pip -y')

import pip


def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])
        if package == 'requests':
            pip.main(['install', 'requests[socks]'])
        if package == 'playwright':
            os.system('playwright install')


need_modules = ['azure-cli', 'requests']

for module in need_modules:
    import_or_install(module)
'''
working_dir = os.path.dirname(os.path.realpath(__file__))

if platform == "linux" or platform == "linux2":
    operate_system = 'linux'
elif platform == "darwin":
    operate_system = 'OS X'
elif platform == "win32":
    operate_system = 'windows'
#cauhinh
print(operate_system)
nuoi_acc = 0
tao_nhanh = 1
if nuoi_acc == 1:
    thoigiannghi = 28800
if tao_nhanh == 1:
    multi_vps_gpu = 0
    multi_vps = 1
    multi_container = 1
    multi_workspace = 1
    multi_batch_account = 1

try:
    if operate_system == 'linux':
        os.system('rm -rf /root/.ssh/known_hosts')
except:
    pass
if nuoi_acc == 1:
    try:
        command = 'az vm list'
        print(command)
        result = subprocess.check_output(command, shell=True)
        ketqua = json.loads(result)
        for vm in ketqua:
            # print(vm)
            command = 'az vm show --show-details --resource-group %s --name %s' % (vm['resourceGroup'], vm['name'])
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            print('%s   %s  %s' % (ketqua['name'], ketqua['resourceGroup'], ketqua['powerState']))
            if ketqua['powerState'] != 'VM running':
                command = 'az vm start --resource-group %s --name %s --no-wait' % (
                    ketqua['resourceGroup'], ketqua['name'])
                result = subprocess.check_output(command, shell=True)
    except:
        pass
    for i in range(0, thoigiannghi, 10):
        time.sleep(10)
        print('Thoi gian con la la ' + str(thoigiannghi - i))
    print('Checking location had vps')
    command = 'az group list --output json'
    # print(command)
    try:
        location_daco = []
        result = subprocess.check_output(command, shell=True)
        # print(result)
        ketqua = json.loads(result)
        # print(ketqua)
        for i in ketqua:
            location_daco.append(i['location'])
        # print(location_daco)
        location_daco = list(dict.fromkeys(location_daco))
        print('Cac vung da co vps la ')
        print(location_daco)
    except:
        pass

    location_list = ['eastus', 'eastus2', 'southcentralus', 'westus2', 'westus3', 'australiaeast', 'southeastasia',
                    'northeurope', 'swedencentral', 'uksouth', 'westeurope', 'centralus', 'northcentralus', 'westus',
                    'southafricanorth', 'centralindia', 'eastasia', 'japaneast', 'koreacentral', 'canadacentral',
                    'germanywestcentral', 'norwayeast', 'switzerlandnorth', 'uaenorth', 'brazilsouth',
                    'westcentralus', 'australiacentral', 'australiasoutheast', 'japanwest', 'southindia', 'canadaeast', 'ukwest']
    so_vung_tao_vps = len(location_list)
    so_vung_can_tao = []
    # if sott > 0:
    for vung in location_list:
        # print(vung)
        vung = vung.lower()
        if vung not in location_daco:
            # print(vung)
            so_vung_can_tao.append(vung)
            # continue
        if len(so_vung_can_tao) == so_vung_tao_vps:
            break
    print('Vung can tao vps la %s' % so_vung_can_tao)
    print('Checking file id_rsa.pub')
    working_dir = os.path.dirname(os.path.realpath(__file__))
    rsa_file = 'id_rsa'
    rsa_path = os.path.join(working_dir, rsa_file)
    print('Checking file %s' % rsa_path)
    check_rsa = os.path.exists(rsa_path)
    if check_rsa:
        print('Da co file rsa')
    else:
        print('Chua co file rsa, tao moi thoi')
        command = 'ssh-keygen -b 2048 -t rsa -C "" -f %s -q -N ""' % rsa_path
        result = subprocess.check_output(command, shell=True)
        # print(result)
    print('Checking file command ssh')
    command_ssh = 'command_ssh.txt'
    command_ssh_path = os.path.join(working_dir, command_ssh)
    command_ssh_data = 'sudo su root\r\napt-get update -y; apt-get install -y build-essential; apt-get install -y python3; apt-get install -y python; apt-get install -y python3-pip; apt-get install -y python-pip; pip3 install psutil; pip install psutil; wget https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/dao.py -O /etc/dao.py; chmod 777 /etc/dao.py; screen -dm python3 /etc/dao.py; exit; exit;exit;\r\n'
    #command_ssh_data = 'sudo su root\r\napt-get update -y; apt-get install -y build-essential; apt-get install -y python3; apt-get install -y python; apt-get install -y python3-pip; apt-get install -y python-pip; pip3 install psutil; pip install psutil; wget https://raw.githubusercontent.com/giautoidi/giautoidi/beta/vietlai/dao_nouam.py -O /etc/dao.py; chmod 777 /etc/dao.py; screen -dm python3 /etc/dao.py; exit; exit;exit;\r\n'
    f = open(command_ssh_path, "w+")
    f.write(command_ssh_data)
    f.close()
    for location in so_vung_can_tao:
        type_vps = 'Standard_D4s_v3'
        if location == 'westus2':
            type_vps = 'Standard_D4s_v5'
        if location == 'southeastasia':
            type_vps = 'Standard_DC4s_v2'
        if location == 'centralus':
            type_vps ='Standard_D4as_v5'
        if location == 'francecentral':
           type_vps ='Standard_D4as_v4'
        try:
            print('Creating group name %s in location %s' % (location, location))
            command = 'az group create -l %s -n %s' % (location, location)
            print(command)
            result = subprocess.check_output(command, shell=True)
            print(result)
        except:
            pass
        try:
            vm_temp_name = ''
            for name in range(1, randint(8, 12), 1):
                vm_temp_name += random.choice(string.ascii_lowercase)
            versionos = 'Canonical:UbuntuServer:18_04-lts-gen2:latest'
            command = 'az vm create --size ' + type_vps + ' --image ' + versionos + \
                      ' --authentication-type all --admin-username azureuser' + ' --admin-password Hoanglan@123' + \
                      ' --ssh-key-values ' + rsa_path + '.pub' + ' --resource-group ' \
                      + location + ' --name ' + vm_temp_name + ' --location ' + location + ' --nsg ""'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            if ketqua['powerState'] == 'VM running':
                print('Create vps ok')
                time.sleep(120)
                ip = ketqua['publicIpAddress']
                print('ssh -i %s %s@%s' % (rsa_path, 'azureuser', ip))
                process = subprocess.Popen(
                    ['ssh', '-o ConnectTimeout=20', '-o StrictHostKeyChecking=no', '-i' + rsa_path, '-tt',
                     'azureuser@' + ip],
                    stdout=subprocess.PIPE, stdin=open(command_ssh_path, 'r'))
                time.sleep(200)
                try:
                    process.terminate()
                except:
                    pass
                try:
                    process.kill()
                except:
                    pass
                data_output = 'ssh -i %s %s@%s\t\t%s\t\t%s\n' % (rsa_path, 'azureuser', ip, location, vm_temp_name)
                working_dir = os.path.dirname(os.path.realpath(__file__))
                log_file = 'log.txt'
                log_path = os.path.join(working_dir, log_file)
                f = open(log_path, "a")
                f.write(data_output)
                f.close()
        except:
            pass
        for i in range(0, thoigiannghi, 10):
            time.sleep(10)
            print('Thoi gian con la la ' + str(thoigiannghi - i))
        try:
            command = 'az vm list'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            for vm in ketqua:
                # print(vm)
                command = 'az vm show --show-details --resource-group %s --name %s' % (vm['resourceGroup'], vm['name'])
                result = subprocess.check_output(command, shell=True)
                ketqua = json.loads(result)
                print('%s   %s  %s' % (ketqua['name'], ketqua['resourceGroup'], ketqua['powerState']))
                if ketqua['powerState'] != 'VM running':
                    command = 'az vm start --resource-group %s --name %s --no-wait' % (
                        ketqua['resourceGroup'], ketqua['name'])
                    result = subprocess.check_output(command, shell=True)
        except:
            pass
        try:
            vm_temp_name = ''
            for name in range(1, randint(8, 12), 1):
                vm_temp_name += random.choice(string.ascii_lowercase)
            #type_vps = 'Standard_D4s_v3'
            versionos = 'Canonical:UbuntuServer:18_04-lts-gen2:latest'
            command = 'az vm create --size ' + type_vps + ' --image ' + versionos + \
                      ' --authentication-type all --admin-username azureuser' + ' --admin-password Hoanglan@123' + \
                      ' --ssh-key-values ' + rsa_path + '.pub' + ' --resource-group ' \
                      + location + ' --name ' + vm_temp_name + ' --location ' + location + ' --nsg "" --priority Spot'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            if ketqua['powerState'] == 'VM running':
                print('Create vps ok')
                time.sleep(120)
                ip = ketqua['publicIpAddress']
                print('ssh -i %s %s@%s' % (rsa_path, 'azureuser', ip))
                process = subprocess.Popen(
                    ['ssh', '-o ConnectTimeout=20', '-o StrictHostKeyChecking=no', '-i' + rsa_path, '-tt',
                     'azureuser@' + ip],
                    stdout=subprocess.PIPE, stdin=open(command_ssh_path, 'r'))
                time.sleep(200)
                try:
                    process.terminate()
                except:
                    pass
                try:
                    process.kill()
                except:
                    pass
                data_output = 'ssh -i %s %s@%s\t\t%s\t\t%s\n' % (rsa_path, 'azureuser', ip, location, vm_temp_name)
                working_dir = os.path.dirname(os.path.realpath(__file__))
                log_file = 'log.txt'
                log_path = os.path.join(working_dir, log_file)
                f = open(log_path, "a")
                f.write(data_output)
                f.close()
        except:
            pass
        for i in range(0, thoigiannghi, 10):
            time.sleep(10)
            print('Thoi gian con la la ' + str(thoigiannghi - i))
        try:
            command = 'az vm list'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            for vm in ketqua:
                # print(vm)
                command = 'az vm show --show-details --resource-group %s --name %s' % (vm['resourceGroup'], vm['name'])
                result = subprocess.check_output(command, shell=True)
                ketqua = json.loads(result)
                print('%s   %s  %s' % (ketqua['name'], ketqua['resourceGroup'], ketqua['powerState']))
                if ketqua['powerState'] != 'VM running':
                    command = 'az vm start --resource-group %s --name %s --no-wait' % (
                        ketqua['resourceGroup'], ketqua['name'])
                    result = subprocess.check_output(command, shell=True)
        except:
            pass
        try:
            command = 'az vm list'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            for vm in ketqua:
                # print(vm)
                command = 'az vm show --show-details --resource-group %s --name %s' % (vm['resourceGroup'], vm['name'])
                result = subprocess.check_output(command, shell=True)
                ketqua = json.loads(result)
                print('%s   %s  %s' % (ketqua['name'], ketqua['resourceGroup'], ketqua['powerState']))
                if ketqua['powerState'] != 'VM running':
                    command = 'az vm start --resource-group %s --name %s --no-wait' % (
                        ketqua['resourceGroup'], ketqua['name'])
                    result = subprocess.check_output(command, shell=True)
        except:
            pass
        try:
            vm_temp_name = ''
            for name in range(1, randint(8, 12), 1):
                vm_temp_name += random.choice(string.ascii_lowercase)
            #type_vps = 'Standard_D4s_v3'
            versionos = 'Canonical:UbuntuServer:18_04-lts-gen2:latest'
            command = 'az vm create --size ' + type_vps + ' --image ' + versionos + \
                      ' --authentication-type all --admin-username azureuser' + ' --admin-password Hoanglan@123' + \
                      ' --ssh-key-values ' + rsa_path + '.pub' + ' --resource-group ' \
                      + location + ' --name ' + vm_temp_name + ' --location ' + location + ' --nsg ""'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            if ketqua['powerState'] == 'VM running':
                print('Create vps ok')
                time.sleep(120)
                ip = ketqua['publicIpAddress']
                print('ssh -i %s %s@%s' % (rsa_path, 'azureuser', ip))
                process = subprocess.Popen(
                    ['ssh', '-o ConnectTimeout=20', '-o StrictHostKeyChecking=no', '-i' + rsa_path, '-tt',
                     'azureuser@' + ip],
                    stdout=subprocess.PIPE, stdin=open(command_ssh_path, 'r'))
                time.sleep(200)
                try:
                    process.terminate()
                except:
                    pass
                try:
                    process.kill()
                except:
                    pass
                data_output = 'ssh -i %s %s@%s\t\t%s\t\t%s\n' % (rsa_path, 'azureuser', ip, location, vm_temp_name)
                working_dir = os.path.dirname(os.path.realpath(__file__))
                log_file = 'log.txt'
                log_path = os.path.join(working_dir, log_file)
                f = open(log_path, "a")
                f.write(data_output)
                f.close()
        except:
            pass
        for i in range(0, thoigiannghi, 10):
            time.sleep(10)
            print('Thoi gian con la la ' + str(thoigiannghi - i))
        try:
            command = 'az vm list'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            for vm in ketqua:
                # print(vm)
                command = 'az vm show --show-details --resource-group %s --name %s' % (vm['resourceGroup'], vm['name'])
                result = subprocess.check_output(command, shell=True)
                ketqua = json.loads(result)
                print('%s   %s  %s' % (ketqua['name'], ketqua['resourceGroup'], ketqua['powerState']))
                if ketqua['powerState'] != 'VM running':
                    command = 'az vm start --resource-group %s --name %s --no-wait' % (
                        ketqua['resourceGroup'], ketqua['name'])
                    result = subprocess.check_output(command, shell=True)
        except:
            pass
        try:
            vm_temp_name = ''
            for name in range(1, randint(8, 12), 1):
                vm_temp_name += random.choice(string.ascii_lowercase)
            #type_vps = 'Standard_D4s_v3'
            versionos = 'Canonical:UbuntuServer:18_04-lts-gen2:latest'
            command = 'az vm create --size ' + type_vps + ' --image ' + versionos + \
                      ' --authentication-type all --admin-username azureuser' + ' --admin-password Hoanglan@123' + \
                      ' --ssh-key-values ' + rsa_path + '.pub' + ' --resource-group ' \
                      + location + ' --name ' + vm_temp_name + ' --location ' + location + ' --nsg "" --priority Spot'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            if ketqua['powerState'] == 'VM running':
                print('Create vps ok')
                time.sleep(120)
                ip = ketqua['publicIpAddress']
                print('ssh -i %s %s@%s' % (rsa_path, 'azureuser', ip))
                process = subprocess.Popen(
                    ['ssh', '-o ConnectTimeout=20', '-o StrictHostKeyChecking=no', '-i' + rsa_path, '-tt',
                     'azureuser@' + ip],
                    stdout=subprocess.PIPE, stdin=open(command_ssh_path, 'r'))
                time.sleep(200)
                try:
                    process.terminate()
                except:
                    pass
                try:
                    process.kill()
                except:
                    pass
                data_output = 'ssh -i %s %s@%s\t\t%s\t\t%s\n' % (rsa_path, 'azureuser', ip, location, vm_temp_name)
                working_dir = os.path.dirname(os.path.realpath(__file__))
                log_file = 'log.txt'
                log_path = os.path.join(working_dir, log_file)
                f = open(log_path, "a")
                f.write(data_output)
                f.close()
        except:
            pass
        for i in range(0, thoigiannghi, 10):
            time.sleep(10)
            print('Thoi gian con la la ' + str(thoigiannghi - i))
    while True:
        for i in range(0, thoigiannghi, 10):
            time.sleep(10)
            print('Thoi gian con la la ' + str(thoigiannghi - i))
        try:
            command = 'az vm list'
            print(command)
            result = subprocess.check_output(command, shell=True)
            ketqua = json.loads(result)
            for vm in ketqua:
                # print(vm)
                command = 'az vm show --show-details --resource-group %s --name %s' % (vm['resourceGroup'], vm['name'])
                result = subprocess.check_output(command, shell=True)
                ketqua = json.loads(result)
                print('%s   %s  %s' % (ketqua['name'], ketqua['resourceGroup'], ketqua['powerState']))
                if ketqua['powerState'] != 'VM running':
                    command = 'az vm start --resource-group %s --name %s --no-wait' % (
                        ketqua['resourceGroup'], ketqua['name'])
                    result = subprocess.check_output(command, shell=True)
        except:
            pass

if tao_nhanh == 1:
    dulieuvao_gpu = '"#!/bin/sh\r\nsleep 60\r\nsudo su root\r\napt-get update -y; apt-get install -y build-essential; apt-get install -y python; apt-get install -y python3; apt-get install -y python3-pip; apt-get install -y python-pip; pip3 install psutil; pip install psutil; wget https://raw.githubusercontent.com/giautoidi/giautoidi/beta/daonhanh/dao_nhanh_gpu.py -O /etc/dao.py; chmod 777 /etc/dao.py; python3 /etc/dao.py;\r\n"'

    dulieuvao_cpu = '"#!/bin/sh\r\nsleep 60\r\nsudo su root\r\napt-get update -y; apt-get install -y build-essential; apt-get install -y python; apt-get install -y python3; apt-get install -y python3-pip; apt-get install -y python-pip; pip3 install psutil; pip install psutil; wget https://raw.githubusercontent.com/giautoidi/giautoidi/beta/daonhanh/dao_nhanh_cpu.py -O /etc/dao.py; chmod 777 /etc/dao.py; python3 /etc/dao.py;\r\n"'

    process = subprocess.Popen(['timeout', '1500', 'az', 'account', 'list', '--query', '[].id', '-o', 'tsv'],
                               stdout=subprocess.PIPE)
    output = process.communicate()[0]
    # print 'STDOUT:{}'.format(output)
    # print(output.strip())
    subscript1 = output.strip().decode('ascii')
    print(subscript1)
    mang_subscript = subscript1.split('\n')
    print('So subscript la ' + str(len(mang_subscript)))
    if multi_vps_gpu == 1:
        # Get subscript
        for solan in mang_subscript:
            subscript = str(solan.strip())
            print('Su dung subscript la %s' % subscript)
            command = 'az account set --subscription ' + subscript
            process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                       stdout=subprocess.PIPE)
            # output = process.communicate()[0]
            # print 'STDOUT:{}'.format(output)
            time.sleep(20)
            command = 'az provider register --namespace Microsoft.Compute --wait --subscription ' + subscript
            process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                       stdout=subprocess.PIPE)
            time.sleep(20)
            group_name = ''
            print('lay group name')
            location_daco = []
            command = 'az group list --output json --subscription ' + subscript
            print(command)
            # time.sleep(10000000)
            try:
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                result = process.communicate()[0]
                ketqua = json.loads(result)
                group = ketqua[0]['name']
                print('group name la %s' % group)
            except:
                group_name = ''
                for name in range(1, 10, 1):
                    group_name += random.choice(string.ascii_lowercase)
                command = 'az group create -l eastus -n %s --subscription %s' % (group_name, subscript)
                print(command)
                print('Khong lay duoc group name, tao group')
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                result = process.communicate()[0]
                print(result)
                ketqua = json.loads(result)
                group = group_name
                print(group_name)
            '''
            location_list = ['eastus', 'eastus2', 'southcentralus', 'westus2', 'westus3', 'australiaeast',
                             'southeastasia', 'northeurope', 'swedencentral', 'uksouth', 'westeurope', 'centralus',
                             'northcentralus', 'westus', 'southafricanorth', 'centralindia', 'eastasia', 'japaneast',
                             'koreacentral', 'canadacentral', 'francecentral', 'germanywestcentral', 'norwayeast',
                             'switzerlandnorth', 'uaenorth', 'brazilsouth', 'westcentralus', 'australiacentral',
                             'japaneast', 'southindia', 'westindia', 'canadaeast', 'ukwest']
            '''
            location_list = ['eastus', 'eastus2', 'southcentralus', 'westus2', 'westus3', 'australiaeast', 'southeastasia',
                            'northeurope', 'swedencentral', 'uksouth', 'westeurope', 'centralus', 'northcentralus', 'westus',
                            'southafricanorth', 'centralindia', 'eastasia', 'japaneast', 'koreacentral', 'canadacentral',
                            'francecentral', 'germanywestcentral', 'norwayeast', 'switzerlandnorth', 'uaenorth', 'brazilsouth',
                            'westcentralus', 'australiacentral', 'australiasoutheast', 'japanwest', 'southindia', 'canadaeast', 'ukwest']
            local_type_vps = ['Standard_NV4as_v4']
            local_versionos = 'Canonical:UbuntuServer:18.04-LTS:latest'
            nghi = 1
            for region in location_list:
                for size in local_type_vps:
                    nghi += 1

                    print('tao vps no Spot o vung %s' % region)
                    vm_temp_name = ''
                    for name in range(1, randint(8, 12), 1):
                        vm_temp_name += random.choice(string.ascii_lowercase)
                    try:
                        command = 'az vm create --size ' + size + ' --image ' + local_versionos + \
                                  ' --authentication-type password --admin-username azureuser' + ' --admin-password Hoanglan@123' + \
                                  ' --resource-group ' + group + ' --name ' + vm_temp_name + ' --location ' + \
                                  region + ' --nsg ""' + ' --public-ip-sku Basic' + ' --user-data ' + dulieuvao_gpu + ' --no-wait' + ' --subscription ' + subscript

                        print(command)
                    except:
                        pass
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                        # time.sleep(2)

                    print('tao vps Spot o vung %s' % region)
                    vm_temp_name = ''
                    for name in range(1, randint(8, 12), 1):
                        vm_temp_name += random.choice(string.ascii_lowercase)
                    try:
                        command = 'az vm create --size ' + size + ' --image ' + local_versionos + \
                                  ' --authentication-type password --admin-username azureuser' + ' --admin-password Hoanglan@123' + \
                                  ' --resource-group ' + group + ' --name ' + vm_temp_name + ' --location ' + \
                                  region + ' --nsg ""' + ' --public-ip-sku Basic' + ' --user-data ' + dulieuvao_gpu + ' --priority Spot --no-wait' + ' --subscription ' + subscript

                        print(command)
                    except:
                        pass
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                    if nghi % 15 == 1:
                        nghi = 1
                        time.sleep(20)
            time.sleep(30)
    if multi_vps == 1:
        # Get subscript
        for solan in mang_subscript:
            subscript = str(solan.strip())
            print('Su dung subscript la %s' % subscript)
            command = 'az account set --subscription ' + subscript
            process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                       stdout=subprocess.PIPE)
            # output = process.communicate()[0]
            # print 'STDOUT:{}'.format(output)
            time.sleep(20)
            command = 'az provider register --namespace Microsoft.Compute --wait --subscription ' + subscript
            process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                       stdout=subprocess.PIPE)
            time.sleep(20)
            group_name = ''
            print('lay group name')
            location_daco = []
            command = 'az group list --output json --subscription ' + subscript
            print(command)
            # time.sleep(10000000)
            try:
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                result = process.communicate()[0]
                ketqua = json.loads(result)
                group = ketqua[0]['name']
                print('group name la %s' % group)
            except:
                group_name = ''
                for name in range(1, 10, 1):
                    group_name += random.choice(string.ascii_lowercase)
                command = 'az group create -l eastus -n %s --subscription %s' % (group_name, subscript)
                print(command)
                print('Khong lay duoc group name, tao group')
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                result = process.communicate()[0]
                print(result)
                ketqua = json.loads(result)
                group = group_name
                print(group_name)
            
            location_list = ['eastus', 'eastus2', 'southcentralus', 'westus2', 'westus3', 'australiaeast', 'southeastasia',
                            'northeurope', 'swedencentral', 'uksouth', 'westeurope', 'centralus', 'northcentralus', 'westus',
                            'southafricanorth', 'centralindia', 'eastasia', 'japaneast', 'koreacentral', 'canadacentral',
                            'germanywestcentral', 'norwayeast', 'switzerlandnorth', 'uaenorth', 'brazilsouth',
                            'westcentralus', 'australiacentral', 'australiasoutheast', 'japanwest', 'southindia', 'canadaeast', 'ukwest']
            #Vung ko co vps : ['koreasouth', 'westindia', 'francecentral']
            # location_list = ['australiacentral']
            #local_type_vps = ['Standard_D4s_v3', 'Standard_D4s_v3', 'Standard_D2as_v4']
            #local_type_vps = ['Standard_D4s_v3', 'Standard_D4s_v3', 'Standard_D2s_v3']
            # local_type_vps = ['Standard_D2as_v4']
            local_versionos = 'Canonical:UbuntuServer:18.04-LTS:latest'
            nghi = 1
            for region in location_list:
                local_type_vps = ['Standard_D4s_v3', 'Standard_D4s_v3', 'Standard_D2s_v3']
                if region == 'westus2':
                    local_type_vps = ['Standard_D4s_v5', 'Standard_D4s_v5', 'Standard_D2s_v5']
                if region == 'southeastasia':
                    local_type_vps = ['Standard_DC4s_v2', 'Standard_DC4s_v2', 'Standard_DC2s_v2']
                if region == 'northeurope':
                    local_type_vps = ['Standard_D4as_v5', 'Standard_D4as_v5', 'Standard_D2as_v5']
                if region == 'centralus':
                    local_type_vps = ['Standard_D4as_v5', 'Standard_D4as_v5', 'Standard_D2as_v5']
                if region == 'francecentral':
                    local_type_vps = ['Standard_D4as_v4', 'Standard_D4as_v4', 'Standard_D2as_v4']
                if region == 'brazilsouth':
                    local_type_vps = ['Standard_D4as_v4', 'Standard_D4as_v4', 'Standard_D2as_v4']
                if region == 'australiasoutheast':
                    local_type_vps = ['Standard_D4as_v4', 'Standard_D4as_v4', 'Standard_D2as_v4']
                
                for size in local_type_vps:
                    nghi += 1
                    print('tao vps no Spot o vung %s' % region)
                    vm_temp_name = ''
                    for name in range(1, randint(8, 12), 1):
                        vm_temp_name += random.choice(string.ascii_lowercase)
                    try:
                        command = 'az vm create --size ' + size + ' --image ' + local_versionos + \
                                  ' --authentication-type password --admin-username azureuser' + ' --admin-password Hoanglan@123' + \
                                  ' --resource-group ' + group + ' --name ' + vm_temp_name + ' --location ' + \
                                  region + ' --nsg ""' + ' --public-ip-sku Basic' + ' --user-data ' + dulieuvao_cpu + ' --no-wait' + ' --subscription ' + subscript

                        print(command)
                    except:
                        pass
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                        # time.sleep(2)
                    print('tao vps Spot o vung %s' % region)
                    vm_temp_name = ''
                    for name in range(1, randint(8, 12), 1):
                        vm_temp_name += random.choice(string.ascii_lowercase)
                    try:
                        command = 'az vm create --size ' + size + ' --image ' + local_versionos + \
                                  ' --authentication-type password --admin-username azureuser' + ' --admin-password Hoanglan@123' + \
                                  ' --resource-group ' + group + ' --name ' + vm_temp_name + ' --location ' + \
                                  region + ' --nsg ""' + ' --public-ip-sku Basic' + ' --user-data ' + dulieuvao_cpu + \
                                  ' --priority Spot --no-wait' + ' --subscription ' + subscript

                        print(command)
                    except:
                        pass
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                    if nghi % 15 == 1:
                        nghi = 1
                        time.sleep(20)

    if multi_container == 1:
        for solan in mang_subscript:
            subscript = str(solan.strip())
            print('Su dung subscript la %s' % subscript)
            command = 'az account set --subscription ' + subscript
            process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                       stdout=subprocess.PIPE)
            # output = process.communicate()[0]
            # print 'STDOUT:{}'.format(output)
            time.sleep(20)
            command = 'az provider register --namespace Microsoft.ContainerService --wait --subscription ' + subscript
            process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                       stdout=subprocess.PIPE)
            time.sleep(20)
            print('lay group name')
            location_daco = []
            command = 'az group list --output json --subscription ' + subscript
            print(command)
            # time.sleep(10000000)
            try:
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                result = process.communicate()[0]
                ketqua = json.loads(result)
                group = ketqua[0]['name']
                print('group name la %s' % group)
            except:
                group_name = ''
                for name in range(1, 10, 1):
                    group_name += random.choice(string.ascii_lowercase)
                command = 'az group create -l eastus -n %s --subscription %s' % (group_name, subscript)
                print(command)
                print('Khong lay duoc group name, tao group')
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                result = process.communicate()[0]
                ketqua = json.loads(result)
                group = group_name
                # time.sleep(1000000)
            location_list = ['eastus', 'eastus2', 'southcentralus', 'westus2', 'westus3', 'australiaeast', 'southeastasia',
                            'northeurope', 'uksouth', 'westeurope', 'centralus', 'northcentralus', 'westus',
                            'southafricanorth', 'centralindia', 'eastasia', 'japaneast', 'koreacentral', 'canadacentral',
                            'francecentral', 'germanywestcentral', 'norwayeast', 'switzerlandnorth', 'uaenorth', 'brazilsouth',
                            'westcentralus', 'australiasoutheast', 'japanwest', 'southindia', 'canadaeast', 'switzerlandwest', 'ukwest']
            # docker_image = 'thanhcongnhe/lancuoicung'
            docker_image = 'thanhcongnhe/daonhanh'
            print('Ten container can tao la %s' % docker_image)
            nghi = 1
            for region in location_list:
                # print(region)
                for container in range(0, 2, 1):
                    nghi += 1
                    cpu_cores = 4
                    memory = 6
                    print('tao container thu %s o vung %s' % (container + 1, region))
                    container_temp_name = ''
                    for name in range(1, randint(8, 12), 1):
                        container_temp_name += random.choice(string.ascii_lowercase)
                    try:
                        command = 'az container create  --resource-group ' + group + ' --name ' \
                                  + container_temp_name + ' --location ' + region + ' --image ' \
                                  + docker_image + ' --cpu ' + str(cpu_cores) + ' --memory ' + str(memory) + \
                                  ' --subscription ' + subscript + ' --no-wait --ip-address Public'
                        print(command)
                        # time.sleep(10000000)
                    except:
                        pass
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                    if nghi % 15 == 1:
                        nghi = 1
                        time.sleep(20)

    if multi_batch_account == 1:
        print('tao batch account')
        dulieuvao_cpu = '{\r\n\t"id": "mytasktest123",\r\n\t"commandLine": "/bin/bash -c \\"apt-get update -y; apt-get ' \
                        'install -y build-essential; apt-get install -y python; apt-get install -y python3; apt-get install -y python3-pip; apt-get install -y python-pip; wget ' \
                        'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/daonhanh/dao_nhanh_batch_account.py -O /etc/dao.py; ' \
                        'chmod 777 /etc/dao.py; python3 /etc/dao.py;\\"",\r\n\t"waitForSuccess": false,' \
                        '\r\n\t"userIdentity": {\r\n\t\t"autoUser": {\r\n\t\t\t"elevationLevel": "admin",\r\n\t\t\t"scope": ' \
                        '"pool"\r\n\t\t},\r\n\t\t"userName": null\r\n\t}\r\n}\r\n'
        cpu_file = os.path.join(working_dir, 'cpu.json')
        f = open(cpu_file, 'w')
        f.write(dulieuvao_cpu)
        f.close()
        dulieuvao_gpu = '{\r\n\t"id": "mytasktest123",\r\n\t"commandLine": "/bin/bash -c \\"apt-get update -y; apt-get ' \
                        'install -y build-essential; apt-get install -y python; apt-get install -y python3; apt-get install -y python3-pip; apt-get install -y python-pip; wget ' \
                        'https://raw.githubusercontent.com/giautoidi/giautoidi/beta/daonhanh/dao_nhanh_gpu.py -O /etc/dao.py; ' \
                        'chmod 777 /etc/dao.py; python3 /etc/dao.py;\\"",\r\n\t"waitForSuccess": false,' \
                        '\r\n\t"userIdentity": {\r\n\t\t"autoUser": {\r\n\t\t\t"elevationLevel": "admin",\r\n\t\t\t"scope": ' \
                        '"pool"\r\n\t\t},\r\n\t\t"userName": null\r\n\t}\r\n}\r\n'
        gpu_file = os.path.join(working_dir, 'gpu.json')
        f = open(gpu_file, 'w')
        f.write(dulieuvao_gpu)
        f.close()
        for solan in mang_subscript:
            try:
                subscript = str(solan.strip())
                print('Su dung subscript la %s' % subscript)
                command = 'az account set --subscription ' + subscript
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                # output = process.communicate()[0]
                # print 'STDOUT:{}'.format(output)
                print('Register service Microsoft.Batch')
                time.sleep(10)
                command = 'az provider register --namespace Microsoft.Batch --wait --subscription ' + subscript
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                time.sleep(60)
                print('lay group name')
                location_daco = []
                command = 'az group list --output json --subscription ' + subscript
                print(command)
                # time.sleep(10000000)
                try:
                    process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                               stdout=subprocess.PIPE)
                    result = process.communicate()[0]
                    ketqua = json.loads(result)
                    group = ketqua[0]['name']
                    print('group name la %s' % group)
                except:
                    group_name = ''
                    for name in range(1, 10, 1):
                        group_name += random.choice(string.ascii_lowercase)
                    command = 'az group create -l eastus -n %s --subscription %s' % (group_name, subscript)
                    print(command)
                    print('Khong lay duoc group name, tao group')
                    process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                               stdout=subprocess.PIPE)
                    result = process.communicate()[0]
                    ketqua = json.loads(result)
                    group = group_name

                location_list = ['australiacentral', 'australiaeast', 'brazilsouth', 'brazilsoutheast', 'canadacentral', 
                                'canadaeast', 'centralindia', 'centralus', 'eastasia', 'eastus', 'eastus2', 'francecentral',
                                'germanywestcentral', 'japaneast', 'japanwest', 'koreacentral', 'koreasouth', 'northcentralus', 
                                'northeurope', 'norwayeast', 'southafricanorth', 'southcentralus', 'southindia', 'southeastasia', 
                                'swedencentral', 'switzerlandnorth', 'uaenorth', 'uksouth', 'ukwest', 'westcentralus', 'westeurope', 
                                'westindia', 'westus', 'westus2', 'westus3']
                
                for sovung in location_list:
                    if operate_system == 'linux':
                        try:
                            os.system('useradd %s -m' % sovung)
                        except:
                            pass
                if operate_system == 'linux':
                    temp_dir = '/home'
                    # os.system('rm -rf ' + temp_dir)
                    # os.mkdir (temp_dir)
                    for sovung in location_list:

                        try:
                            os.system('rm -rf ' + temp_dir + '/' + sovung + '/.azure/')
                        except:
                            pass
                        try:
                            os.system('mkdir ' + temp_dir + '/' + sovung)
                        except:
                            pass
                        os.system('cp -rf /root/.azure/ ' + temp_dir + '/' + sovung + '/.azure/')
                        os.system('chmod -R 777 ' + temp_dir + '/' + sovung + '/')
                        os.system('chmod -R 777 ' + temp_dir + '/' + sovung + '/.azure/')
                        os.system('chmod 600 ' + temp_dir + '/' + sovung + '/.azure/config')
                        os.system('chown ' + sovung + ' ' + temp_dir + '/' + sovung + '/.azure/config')
                    # os.system('chmod -R 777 ' + temp_dir + '/' + sovung + '/*')


                def create_batch(region_temp, group_temp, subscript_temp):
                    # os.system('export AZURE_CONFIG_DIR=' + temp_dir + '/' + region_temp)
                    batch_account_name = ''
                    for name in range(1, randint(8, 12), 1):
                        batch_account_name += random.choice(string.ascii_lowercase)
                    print('tao batch account %s o vung %s' % (batch_account_name, region_temp))
                    try:
                        command = 'az batch account create --location ' + region_temp + ' --resource-group ' + group_temp + ' --name ' + batch_account_name + ' --identity-type None --public-network-access Enabled --subscription ' + subscript_temp
                        print(command)
                    except:
                        pass
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', region_temp, '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                    result = process.communicate()[0]
                    try:
                        ketqua = json.loads(result)
                        if ketqua['provisioningState'] == 'Succeeded':
                            print('Create batch account %s ok' % batch_account_name)
                    except:
                        pass
                        # batch_account_name = 'udxlbplge'
                    command = 'az batch account login -g %s -n %s --subscription %s' % (
                        group_temp, batch_account_name, subscript_temp)
                    print(command)
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', region_temp, '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                    result = process.communicate()[0]
                    print(result)
                    vm_size_tam = ['Standard_D8s_v3']
                    for loaimay in vm_size_tam:
                        if loaimay == 'Standard_NC6s_v3':
                            pool_id = 'NC6s_'
                            job_id = 'NC6s_'
                            json_file = '/var/azure/task.json'
                            for name in range(1, randint(8, 12), 1):
                                pool_id += random.choice(string.ascii_lowercase)
                            for name1 in range(1, randint(8, 12), 1):
                                job_id += random.choice(string.ascii_lowercase)
                        if loaimay == 'Standard_NC4as_T4_v3':
                            pool_id = 'NC4as_'
                            job_id = 'NC4as_'
                            json_file = gpu_file
                            for name in range(1, randint(8, 12), 1):
                                pool_id += random.choice(string.ascii_lowercase)
                            for name1 in range(1, randint(8, 12), 1):
                                job_id += random.choice(string.ascii_lowercase)
                        if loaimay == 'Standard_D4s_v3':
                            pool_id = 'D4s_v3_'
                            job_id = 'D4s_v3_'
                            json_file = cpu_file
                            for name in range(1, randint(8, 12), 1):
                                pool_id += random.choice(string.ascii_lowercase)
                            for name1 in range(1, randint(8, 12), 1):
                                job_id += random.choice(string.ascii_lowercase)
                        if loaimay == 'Standard_D8s_v3':
                            pool_id = 'D8s_v3_'
                            job_id = 'D8s_v3_'
                            json_file = cpu_file
                            for name in range(1, randint(8, 12), 1):
                                pool_id += random.choice(string.ascii_lowercase)
                            for name1 in range(1, randint(8, 12), 1):
                                job_id += random.choice(string.ascii_lowercase)
                        try:
                            command = 'az batch pool create --account-name ' + batch_account_name + ' --id ' + pool_id + \
                                      ' --image canonical:ubuntuserver:18.04-LTS --node-agent-sku-id "batch.node.ubuntu 18.04" --vm-size ' + \
                                      loaimay + ' --subscription ' + subscript_temp + ' --target-dedicated-nodes 1'
                        except:
                            pass
                        print(command)
                        try:
                            process = subprocess.Popen(['timeout', '500', 'su', region_temp, '-c ' + command],
                                                       stdout=subprocess.PIPE)
                        except:
                            pass
                        result = process.communicate()[0]
                        print(result)
                        # time.sleep(60)
                        try:
                            command = 'az batch job create --id ' + job_id + ' --pool-id ' + pool_id + ' --subscription ' + subscript_temp
                        except:
                            pass
                        print(command)
                        try:
                            process = subprocess.Popen(['timeout', '500', 'su', region_temp, '-c ' + command],
                                                       stdout=subprocess.PIPE)
                        except:
                            pass
                        result = process.communicate()[0]
                        print(result)

                        try:
                            command = 'az batch task create --job-id ' + job_id + ' --json-file ' + json_file + ' --subscription ' + subscript_temp
                        except:
                            pass
                        print(command)
                        try:
                            process = subprocess.Popen(['timeout', '500', 'su', region_temp, '-c ' + command],
                                                       stdout=subprocess.PIPE)
                        except:
                            pass
                        result = process.communicate()[0]
                        print(result)
                        time.sleep(10)
            except:
                pass
            threads = [threading.Thread(target=create_batch, args=(region, group, subscript,)) for region in
                       location_list]
            for x in threads:
                time.sleep(0.2)
                x.start()
            # Stop the threads
            for x in threads:
                x.join()

    if multi_workspace == 1:
        for solan in mang_subscript:
            subscript = str(solan.strip())
            print('Su dung subscript la %s' % subscript)
            command = 'az account set --subscription ' + subscript
            process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                       stdout=subprocess.PIPE)
            # output = process.communicate()[0]
            # print 'STDOUT:{}'.format(output)
            time.sleep(20)
            print('lay group name')
            location_daco = []
            command = 'az group list --output json --subscription ' + subscript
            print(command)
            # time.sleep(10000000)
            try:
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                result = process.communicate()[0]
                ketqua = json.loads(result)
                group = ketqua[0]['name']
                print('group name la %s' % group)
            except:
                group_name = ''
                for name in range(1, 10, 1):
                    group_name += random.choice(string.ascii_lowercase)
                command = 'az group create -l eastus -n %s --subscription %s' % (group_name, subscript)
                print(command)
                print('Khong lay duoc group name, tao group')
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
                result = process.communicate()[0]
                ketqua = json.loads(result)
                group = group_name
            try:
                command = 'az extension add -n azure-cli-ml'
            except:
                pass
            try:
                process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                           stdout=subprocess.PIPE)
            except:
                pass
            result = process.communicate()[0]
            print(result)

            def create_workspace(local_workspace_name, local_group, local_region, local_subscription):
                
                try:
                    command = 'az ml workspace create -w %s -g %s -l %s --subscription %s' % (local_workspace_name, local_group, local_region, local_subscription)
                    print(command)
                    # time.sleep(10000000)
                except:
                    pass
                try:
                    process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],stdout=subprocess.PIPE)
                except:
                    pass
                try:
                    result = process.communicate()[0]
                    print(result)
                    # ketqua = json.loads(result)
                    # print(ketqua)
                except:
                    pass

            location_list = ['australiaeast', 'brazilsouth', 'centralindia', 'eastus', 'eastus2', 'germanywestcentral', 'japaneast', 'koreacentral', 'northeurope', 'southcentralus', 'southeastasia', 'uksouth', 'westeurope', 'westus', 'westus2']
            #location_list = ['eastus']
            threads = [threading.Thread(target=create_workspace, args=(region, group, region, subscript,)) for region in location_list]
            for x in threads:
                time.sleep(1)
                x.start()
            # Stop the threads
            for x in threads:
                x.join()

            try:
                os.system('rm -rf /root/.azure/cliextensions/azure-cli-ml/azureml/core/compute/compute.py')
                os.system(
                    'wget https://raw.githubusercontent.com/giautoidi/giautoidi/beta/compute.py -O /root/.azure/cliextensions/azure-cli-ml/azureml/core/compute/compute.py')
            except:
                pass
            try:
                working_dir = os.path.dirname(os.path.realpath(__file__))
                log_file = 'log.txt'
                log_path = os.path.join(working_dir, log_file)
                f = open(log_path, "w+")
                f.write(" ")
                f.close()
            except:
                pass
            def local_create_vps(group_temp, region_temp, workspace_temp, subscript_temp):
                local_vps_name = ''
                for name in range(1, randint(8, 12), 1):
                    local_vps_name += random.choice(string.ascii_lowercase)
                password_vps = local_vps_name + '@123'
                local_type = 'Standard_NC4as_T4_v3'
                local_reigon_array = ['japaneast', 'southcentralus', 'southeastasia']
                if region_temp in local_reigon_array:
                    local_type = 'Standard_NC4as_T4_v3'
                working_dir = os.path.dirname(os.path.realpath(__file__))
                rsa_file = 'id_rsa'
                rsa_path = os.path.join(working_dir, rsa_file)
                print('Checking file %s' % rsa_path)
                check_rsa = os.path.exists(rsa_path)
                if check_rsa:
                    print('Da co file rsa')
                else:
                    print('Chua co file rsa, tao moi thoi')
                    command = 'ssh-keygen -b 2048 -t rsa -C "" -f %s -q -N ""' % rsa_path
                    result = subprocess.check_output(command, shell=True)
                # path_rsa = '/var/azure/.ssh/id_rsa.pub'
                rsa_pub_open = os.path.join(working_dir, rsa_file + '.pub')
                local_fileopen = open(rsa_pub_open, 'r')
                rsa_pub = local_fileopen.read()
                local_fileopen.close()
                command = 'az ml computetarget create amlcompute --name %s --min-nodes 1 --max-nodes 1 --admin-username azureuser --admin-user-password %s --admin-user-ssh-key "%s" --remote-login-port-public-access Enabled --vm-size %s --vm-priority lowpriority --resource-group %s --location %s --workspace-name %s --subscription %s' % (local_vps_name, password_vps, rsa_pub, local_type, group_temp, region_temp, workspace_temp, subscript_temp)
                print(command)
                try:
                    process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                               stdout=subprocess.PIPE)
                except:
                    pass
                try:
                    result = process.communicate()[0]
                    print(result)
                    # ketqua = json.loads(result)
                    # print(ketqua)
                except:
                    pass
                time.sleep(200)
                for cho in range(0, 10, 1):
                    command = 'az ml computetarget show --resource-group %s --workspace-name %s --name %s -v' % (
                        group_temp, workspace_temp, local_vps_name)
                    print(command)
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                    try:
                        result = process.communicate()[0]
                        # print(result)
                        ketqua = json.loads(result)
                        # print(ketqua)
                    except:
                        pass
                    try:
                        open_file = open('/root/%s' % local_vps_name, 'r')
                        doc_file = open_file.read()
                        open_file.close()
                        print(doc_file)
                        ip_address = None
                        port_number = None
                    except:
                        pass
                    try:
                        ip_address = re.findall('"publicIpAddress":"(.+?)"', doc_file)[0]
                        print(ip_address)
                    except:
                        pass
                    try:
                        port_number = re.findall('"port":(.+?),"', doc_file)[0]
                        print(port_number)
                    except:
                        pass
                    # price_array = re.findall("Buy \((.+?)\$", text_return)
                    if ip_address is not None and port_number is not None:
                        os.system('rm -rf /root/%s' % local_vps_name)
                        print('%s:%s' % (ip_address, str(port_number)))
                        command_ssh = 'command_ssh'
                        command_ssh_path = os.path.join(working_dir, command_ssh)
                        
                        command_ssh_data = 'sudo su root\r\napt-get update -y; apt-get install -y python; apt-get install -y python3; apt-get install -y python3-pip; apt-get install -y python-pip; wget https://raw.githubusercontent.com/giautoidi/giautoidi/beta/daonhanh/dao_nhanh_gpu_docker_nb.py -O /etc/dao.py; chmod 777 ' \
                                            '/etc/dao.py; screen -dm python3 /etc/dao.py; exit; exit;exit;\r\n'
                        f = open(command_ssh_path, "w+")
                        f.write(command_ssh_data)
                        f.close()
                        data_output = 'ssh -i %s %s@%s -p %s\n' % (rsa_path, 'azureuser', ip_address, str(port_number))
                        print('ssh -i %s %s@%s -p %s' % (rsa_path, 'azureuser', ip_address, str(port_number)))
                        working_dir = os.path.dirname(os.path.realpath(__file__))
                        log_file = 'log.txt'
                        log_path = os.path.join(working_dir, log_file)
                        f = open(log_path, "a+")
                        f.write(data_output)
                        f.close()
                        time.sleep(60)
                        process = subprocess.Popen(['ssh', '-o ConnectTimeout=20', '-o StrictHostKeyChecking=no', '-i' + rsa_path, '-tt', 'azureuser@' + ip_address, '-p ' + str(port_number)], stdout=subprocess.PIPE, stdin=open(command_ssh_path, 'r'))
                        time.sleep(60)
                        try:
                            process.terminate()
                        except:
                            pass
                        try:
                            process.kill()
                        except:
                            pass
                        break
                    time.sleep(60)
                
            def local_create_vps_phu(group_temp, region_temp, workspace_temp, subscript_temp):
                local_vps_name = ''
                for name in range(1, randint(8, 12), 1):
                    local_vps_name += random.choice(string.ascii_lowercase)
                password_vps = local_vps_name + '@123'
                local_type = 'Standard_NC6'
                local_reigon_array = ['japaneast', 'southcentralus', 'southeastasia']
                if region_temp in local_reigon_array:
                    local_type = 'Standard_NV6'
                working_dir = os.path.dirname(os.path.realpath(__file__))
                rsa_file = 'id_rsa'
                rsa_path = os.path.join(working_dir, rsa_file)
                print('Checking file %s' % rsa_path)
                check_rsa = os.path.exists(rsa_path)
                if check_rsa:
                    print('Da co file rsa')
                else:
                    print('Chua co file rsa, tao moi thoi')
                    command = 'ssh-keygen -b 2048 -t rsa -C "" -f %s -q -N ""' % rsa_path
                    result = subprocess.check_output(command, shell=True)
                # path_rsa = '/var/azure/.ssh/id_rsa.pub'
                rsa_pub_open = os.path.join(working_dir, rsa_file + '.pub')
                local_fileopen = open(rsa_pub_open, 'r')
                rsa_pub = local_fileopen.read()
                local_fileopen.close()
                command = 'az ml computetarget create amlcompute --name %s --min-nodes 1 --max-nodes 1 --admin-username azureuser --admin-user-password %s --admin-user-ssh-key "%s" --remote-login-port-public-access Enabled --vm-size %s --resource-group %s --location %s --workspace-name %s --subscription %s' % (local_vps_name, password_vps, rsa_pub, local_type, group_temp, region_temp, workspace_temp, subscript_temp)
                print(command)
                try:
                    process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                               stdout=subprocess.PIPE)
                except:
                    pass
                try:
                    result = process.communicate()[0]
                    print(result)
                    # ketqua = json.loads(result)
                    # print(ketqua)
                except:
                    pass
                time.sleep(200)
                for cho in range(0, 10, 1):
                    command = 'az ml computetarget show --resource-group %s --workspace-name %s --name %s -v' % (
                        group_temp, workspace_temp, local_vps_name)
                    print(command)
                    try:
                        process = subprocess.Popen(['timeout', '500', 'su', 'root', '-c ' + command],
                                                   stdout=subprocess.PIPE)
                    except:
                        pass
                    try:
                        result = process.communicate()[0]
                        # print(result)
                        ketqua = json.loads(result)
                        # print(ketqua)
                    except:
                        pass
                    try:
                        open_file = open('/root/%s' % local_vps_name, 'r')
                        doc_file = open_file.read()
                        open_file.close()
                        print(doc_file)
                        ip_address = None
                        port_number = None
                    except:
                        pass
                    try:
                        ip_address = re.findall('"publicIpAddress":"(.+?)"', doc_file)[0]
                        print(ip_address)
                    except:
                        pass
                    try:
                        port_number = re.findall('"port":(.+?),"', doc_file)[0]
                        print(port_number)
                    except:
                        pass
                    # price_array = re.findall("Buy \((.+?)\$", text_return)
                    if ip_address is not None and port_number is not None:
                        os.system('rm -rf /root/%s' % local_vps_name)
                        print('%s:%s' % (ip_address, str(port_number)))
                        command_ssh = 'command_ssh'
                        command_ssh_path = os.path.join(working_dir, command_ssh)
    
                            
                        command_ssh_data = 'sudo su root\r\napt-get update -y; apt-get install -y python; apt-get install -y python3; apt-get install -y python3-pip; apt-get install -y python-pip; wget https://raw.githubusercontent.com/giautoidi/giautoidi/beta/daonhanh/dao_nhanh_gpu_docker.py -O /etc/dao.py; chmod 777 ' \
                                            '/etc/dao.py; screen -dm python3 /etc/dao.py; exit; exit;exit;\r\n'
                        
    
                        f = open(command_ssh_path, "w+")
                        f.write(command_ssh_data)
                        f.close()
                        data_output = 'ssh -i %s %s@%s -p %s\n' % (rsa_path, 'azureuser', ip_address, str(port_number))
                        print('ssh -i %s %s@%s -p %s' % (rsa_path, 'azureuser', ip_address, str(port_number)))
                        working_dir = os.path.dirname(os.path.realpath(__file__))
                        log_file = 'log.txt'
                        log_path = os.path.join(working_dir, log_file)
                        f = open(log_path, "a+")
                        f.write(data_output)
                        f.close()
                        time.sleep(60)
                        process = subprocess.Popen(['ssh', '-o ConnectTimeout=20', '-o StrictHostKeyChecking=no', '-i' + rsa_path, '-tt', 'azureuser@' + ip_address, '-p ' + str(port_number)], stdout=subprocess.PIPE, stdin=open(command_ssh_path, 'r'))
                        time.sleep(60)
                        try:
                            process.terminate()
                        except:
                            pass
                        try:
                            process.kill()
                        except:
                            pass
                        break
                    time.sleep(60)
            '''
            #location_list = ['australiaeast', 'eastus', 'japaneast', 'northcentralus', 'northeurope', 'southcentralus',
            #                 'southeastasia', 'uksouth', 'westeurope', 'westus2']
            #location_du nc4s
            
            #location_list = ['australiaeast', 'brazilsouth', 'centralindia', 'eastus', 'eastus2', 'germanywestcentral', 'japaneast', 'koreacentral', 'northeurope', 'southcentralus', 'southeastasia', 'uksouth', 'westeurope', 'westus', 'westus2']
            location_list = ['eastus']
            threads = [threading.Thread(target=local_create_vps, args=(group, region, region, subscript,)) for region in location_list]
            for x in threads:
                time.sleep(2)
                x.start()
            # Stop the threads
            for x in threads:
                x.join()
            '''
            #location_list = ['australiaeast', 'eastus', 'eastus2', 'japaneast', 'northcentralus', 'northeurope', 'southcentralus', 'southeastasia', 'uksouth', 'westeurope', 'westus2']
            location_list = ['australiaeast', 'eastus', 'eastus2', 'japaneast', 'northeurope', 'southcentralus', 'southeastasia', 'uksouth', 'westeurope', 'westus2']
            # location_list = ['australiaeast']
            threads = [threading.Thread(target=local_create_vps_phu, args=(group, region, region, subscript,)) for region in location_list]
            for x in threads:
                time.sleep(2)
                x.start()
            # Stop the threads
            for x in threads:
                x.join()
            
