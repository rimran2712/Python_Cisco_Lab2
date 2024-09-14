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
This Program will tell BGP neighbor with updown time

Assumption: make sure devices configured with basic ip addresses using script
            make sure devices configured OSPF or anyother IGP and lo0 is reachable for TCP connections
            make sure basic devices has been configured with Basic iBGP
"""

def get_bgp_updown_time (task):
    bgp_summary_result = task.run(task=send_command, command="show ip bgp summary")
    task.host['bgp_summary'] = bgp_summary_result.scrapli_response.genie_parse_output()
    neighbors = task.host['bgp_summary']['vrf']['default']['neighbor']

    for neighbor in neighbors.keys():
        updown_time = task.host['bgp_summary']['vrf']['default']['neighbor'][neighbor]['address_family']['']['up_down']
        print (f"[bold red]{task.host}[/bold red] neighbor [green]{neighbor}[/green] updown time is [bold blue]{updown_time}[/bold blue]")
    
nr.run (task=get_bgp_updown_time)

#ipdb.set_trace ()