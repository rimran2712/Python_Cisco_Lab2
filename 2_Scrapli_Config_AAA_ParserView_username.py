from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks/Cisco_Lab2/Inventory/config.yaml")

"""
We will push Parser view configuiration in this lab which will be used 
in upcoming script automation for Automation Role BAse access. 
We already have admin/imran users at devices which will have full access to devices
We will create support user in this lab which will have limited show commands access as
configured in restricted parser view
"""
def config_basic_aaa (task):
    # Authentication & Authorization both will be local
    # We will also set enable password
    aaa_configs = ["aaa new-model",
                   "aaa authentication login default local",
                   "aaa authorization exec default local",
                   "enable secret Lovenation2712"
                ]
    task.run (task=send_configs, configs=aaa_configs)

def config_parser_view (task):
    # We will creaet parser view "restricted" and all users have limited access 
    # will be assigned to "restricted" parser view.
    paser_view_aaa_configs = ["parser view restricted",
                              "secret Lovenation2712",
                              "command exec include all show ip",
                              "command exec include show version",
                              "command exec include show",
                              "command exec include logout",
                              "command exec include terminal length 0",
                              "command exec include terminal width 512" 
                       ]
    task.run (task=send_configs, configs=paser_view_aaa_configs)

def config_users (task):
    # We will create Users which will have limited access 
    # as defined in above "restricted" parser view
    users_list = ["username support view restricted privilege 15 secret Lovenation2712",
                  "username mohid view restricted privilege 15 secret Lovenation2712",
                  ]
    task.run (task=send_configs, configs=users_list)

def config_aaa_parser_users (task):
    # Lets combine all above aaa, parser, users configuration
    task.run (task=config_basic_aaa)
    task.run (task=config_parser_view)
    task.run (task=config_users)

config_aaa_parser_users_results = nr.run (task=config_aaa_parser_users)
print_result (config_aaa_parser_users_results)
