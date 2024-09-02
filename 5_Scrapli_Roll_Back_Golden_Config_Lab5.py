from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_commands
import os

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks/Cisco_Lab2/Inventory/config.yaml")

""" 
We will roll back current invalid configuration from Golden configuration.

Assumption: Golden configuration already saved on flash drive

Tesing: We can mess up with cureent configuration either manually on devices or
we can send some randome configuration to devices and then we can roll back to golden configuration 
"""

# Clearing the Screen
os.system('clear')

# This medthos will backup Golden configuration
def Roll_Back_Golden_Config (task):
    cmds = ["configure replace flash:backup_golden_config force"]
    task.run (task=send_commands, commands=cmds)

Roll_Back_Golden_Config_Results = nr.run (task=Roll_Back_Golden_Config)
print_result (Roll_Back_Golden_Config_Results)
