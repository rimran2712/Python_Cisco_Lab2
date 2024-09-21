from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
import os
import ipdb
from rich import print


nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Python_Cisco_Lab2/Inventory/config.yaml")

# Clearing the Screen
os.system('clear')

"""
This program will execute "show clock" command and will store structure data using TextFSM
in clock_info variable which will embend to our inventory as key where we can manipulate
this data and u12_Scrapli_Parsing_with_TexSFM.pyse in our program 
"""

"""
IPDB Inspection of clock_info

ipdb> pp nr.inventory.hosts['vIOS-R1']['clock_info']
[{'day': '21',
  'dayweek': 'Sat',
  'month': 'Sep',
  'time': '10:46:24.021',
  'timezone': 'GMT',
  'year': '2024'}]

"""

def get_clock_info (task):
    clock_result = task.run(task=send_command, command="show clock")
    task.host['clock_info'] = clock_result.scrapli_response.textfsm_parse_output()
    print (f"[yellow bold]{task.host} Clock Info[/yellow bold]")
    print (f"[blue]{task.host['clock_info']}[/blue]")   

get_clock_info_results = nr.run (task=get_clock_info)
#print_result (get_clock_info_results)
#ipdb.set_trace ()