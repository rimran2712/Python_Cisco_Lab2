from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
import os
import ipdb


nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Python_Cisco_Lab2/Inventory/config.yaml")

""" 
This program will save "show version" output in task.host['ver'] key as structure data
using Genie Parser, we can trace key "ver" using ipdb.set_trace () method and explore all the keys
"""

# Clearing the Screen
os.system('clear')

def get_version_str_data (task):
    ver_un_structure_results = task.run (task=send_command, command="show version")
    task.host["ver"] = ver_un_structure_results.scrapli_response.genie_parse_output()
    
get_version_str_data_results = nr.run (task=get_version_str_data)
#print_result (get_version_str_data_results)

#ipdb.set_trace ()