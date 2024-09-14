from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_commands, send_configs_from_file
import os

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks/Cisco_Lab2/Inventory/config.yaml")

""" 
If script will be run by admin than admin will get full access
but if script will runn with support usernaem they will have limited show commands
access as we configured in Restricted Parser view in previous Scrip

Assumtion: This script assume you have already push 
Parser view, aaa, username configuration as in "2_Scrapli_Config_AAA_ParserView_username_Lab2" 
"""

# exceute his script with username admin (imran) as in Inventory and support username
# and check access level for both users, once admin user will input command it will have full access
# while support user have limited show access


# Clearing the Screen
os.system('clear')
# Test Case 1: Below method will test command execution level access
"""
# User Input for commands
input_cmds = input ("\nEnter Commands You Wish to Send Devices with ',' separated:- ")
cmds_list = input_cmds.split(',')

def push_cmds (task):
    task.run (task=send_commands, commands=cmds_list)

push_cmds_results = nr.run (task=push_cmds)
print_result (push_cmds_results)
"""

# Test Case 2:  Below method will test configuration level access
def push_random_config (task):
    task.run (task=send_configs_from_file, file="random_configuration.txt")

push_random_config_results = nr.run (task=push_random_config)
print_result (push_random_config_results)