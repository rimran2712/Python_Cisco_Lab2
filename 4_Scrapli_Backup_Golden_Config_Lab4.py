from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_commands, send_configs_from_file, send_interactive
import os

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks/Cisco_Lab2/Inventory/config.yaml")

""" 
We will backup running config to flash. These configuration will be 
our Golden configuration, These configuration will have default IP addresses set on all
interfaces with basic intial configuration so if we mess up with device configuration
we can rollback with these Golden configuration

Assumption: please execute "1_Scrapli_Config_IP_Lab1" script before executing 
this code because, Golden configuration have valid IP addresses.
*** Make sure Hostname in inventory match with real device hostname otherwise script
will not work because in intractive command execution device will return hostname# while hostfile will have diffrent hostname

Tesing: this script will backup Goldent configuration, after backup golden configuration
we can send some random configuration to devices either through Atomation or 
we can do some random configurations manually on devices and than we can roleback to thouht upcoming roleback script
"""

# Clearing the Screen
os.system('clear')

# This medthos will backup Golden configuration
def Backup_Golden_Config (task):
    cmds = [("copy running-config flash:backup_golden_config", "Destination filename"),
            ("\n",f"{task.host}#")]
    task.run (task=send_interactive, interact_events=cmds)

Backup_Golden_Config_Results = nr.run (task=Backup_Golden_Config)
print_result (Backup_Golden_Config_Results)
