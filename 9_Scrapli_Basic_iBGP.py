from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs
import os
import ipdb

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Python_Cisco_Lab2/Inventory/config.yaml")

"""
Configure Basic iBGP in single ASN
"""
def config_basic_iBGP (task):
    iBGP_configs = [f"router bgp {task.host['bgp']['localAsn']}",
                    f"bgp router-id {task.host['bgp']['routerId']}"
                    ]
    neighborsList = task.host['bgp']['neighbors']
    index = 0
    while index < len (neighborsList):
        neighbor = neighborsList[index]['address']
        iBGP_configs.append (f"neighbor {neighbor} remote-as {task.host['bgp']['localAsn']}")
        iBGP_configs.append (f"neighbor {neighbor} update-source {task.host['interfaces']['lo0']['name']}")
        index += 1
    
    task.run (task=send_configs, configs=iBGP_configs)

config_basic_iBGP_results = nr.run (task=config_basic_iBGP)
print_result (config_basic_iBGP_results)

#ipdb.set_trace()
