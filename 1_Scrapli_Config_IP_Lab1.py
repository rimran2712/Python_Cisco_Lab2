from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs

"""
This Script will configure basic IP addresses on all interfaces of Lab devices
as in Topoly Cisco_Lab2
"""
nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks/Cisco_Lab2/Inventory/config.yaml")


def configure_basic_ip_addresses (task):
     interfaceslist = task.host ['interfaces']
     
     index = 0
     while (index < len(interfaceslist)):
          intterface = interfaceslist[index]
          for key in intterface:
               int_name = intterface[key]['name']
               int_ip = intterface[key]['ip']
               int_mask = intterface[key]['mask']
               int_config = [f"interface {int_name}", f"ip address {int_ip} {int_mask}", "no shut"]
               task.run (task=send_configs, configs=int_config)
          index = index+1
       
configure_basic_ip_addresses_results = nr.run (task=configure_basic_ip_addresses)

print_result (configure_basic_ip_addresses_results)
