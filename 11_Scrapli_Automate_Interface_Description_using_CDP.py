from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command, send_configs
import os
import ipdb
from rich import print


nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Python_Cisco_Lab2/Inventory/config.yaml")

# Clearing the Screen
os.system('clear')

""" 
This Program will automatically set Interfaces Description usign CDP Output
We will exceute "show cdp neighbor" command and will parse output using Genie Parser
CDP information have info about local interface, remote interface and remote device name, 
We already know our local device name so once we will ahve all this information
we can send descition to all of our local interface in below format
Description:  "*** <local hostname> <local interface> connected to <remote hostname> <remote interface> ***"

Assumption: make sure devices connected interafces are no shut
            , so we can execute basic ip addresses script because it will no shut interfaces
"""
"""
IPDB Inspection of CDP neibors
ipdb> pp nr.inventory.hosts['vIOS-R1']['cdp_nbrs']['cdp']['index']

{1: {'capability': 'R S I',
     'device_id': 'MGMT-vSW',
     'hold_time': 145,
     'local_interface': 'GigabitEthernet0/0',
     'platform': '',
     'port_id': 'GigabitEthernet0/0'},
 2: {'capability': 'R B',
     'device_id': 'vIOS-R3.mylab.local',
     'hold_time': 168,
     'local_interface': 'GigabitEthernet0/1',
     'platform': 'Gig',
     'port_id': '0/1'},
 3: {'capability': 'R B',
     'device_id': 'vIOS-R4.mylab.local',
     'hold_time': 172,
     'local_interface': 'GigabitEthernet0/2',
     'platform': 'Gig',
     'port_id': '0/2'}}
"""
def set_interface_description (task):
    cdp_nbrs_result = task.run(task=send_command, command="show cdp neighbors")
    task.host['cdp_nbrs'] = cdp_nbrs_result.scrapli_response.genie_parse_output()
    # Below is the Dictionary of all the CDP neibhbors connected with host,
    # we can Iterate this Dicionary for each neighbor details, each Dic key represent info of one nbr
    cdp_neighbors = task.host['cdp_nbrs']['cdp']['index']

    for cdb_nbr in cdp_neighbors.keys():
        remote_host = cdp_neighbors[cdb_nbr]['device_id'].split(".")
        remote_host = remote_host[0] #we removed domain name to make host name shorted
        remote_platform = cdp_neighbors[cdb_nbr]['platform']
        remote_int = cdp_neighbors[cdb_nbr]['port_id']
        local_int = cdp_neighbors[cdb_nbr]['local_interface']

        int_description = f"{task.host} {local_int} Connected to {remote_host} {remote_platform}{remote_int}"
        
        int_desc_configs = [f'interface {local_int}', f"description {int_description}"]
        # Now we have interface description we can set it to each interface using send config
        task.run (task=send_configs, configs=int_desc_configs)        

set_interface_description_results = nr.run (task=set_interface_description)
print_result (set_interface_description_results)
#ipdb.set_trace ()