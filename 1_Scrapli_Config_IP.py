from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs
import os
import ipdb

"""
This Script will configure basic IP addresses on all interfaces of Lab devices
as in Topoly Cisco_Lab2
"""
nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Python_Cisco_Lab2/Inventory/config.yaml")

# Clearing the Screen
os.system('clear')

def configure_basic_ip_addresses (task):
     interfaceslist = task.host ['interfaces']
     
     for interface in interfaceslist.keys():
          int_ip = interfaceslist[interface]['ip']
          int_mask = interfaceslist[interface]['mask']
          int_config = [f"interface {interface}", f"ip address {int_ip} {int_mask}", "no shut"]
          task.run (task=send_configs, configs=int_config)
            
configure_basic_ip_addresses_results = nr.run (task=configure_basic_ip_addresses)

print_result (configure_basic_ip_addresses_results)

#pdb.set_trace()