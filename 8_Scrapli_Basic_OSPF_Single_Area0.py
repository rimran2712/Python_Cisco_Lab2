from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Python_Cisco_Lab2/Inventory/config.yaml")

"""
Configure Basic OSPF on all interfaces in area 0
"""
def config_basic_ospf (task):
    ospf_configs = ["router ospf 1",
                   "network 0.0.0.0 0.0.0.0 area 0"
                   ]
    task.run (task=send_configs, configs=ospf_configs)

config_basic_ospf_results = nr.run (task=config_basic_ospf)
print_result (config_basic_ospf_results)
