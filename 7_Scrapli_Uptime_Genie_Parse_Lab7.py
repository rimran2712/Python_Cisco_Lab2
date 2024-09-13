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
This Program will tell Devices uptime with hostname & if Os_version is 15.6 than its 
our Golden version otherwise will display the cureent version
"""

def get_dev_uptime (task):
    ver_result = task.run(task=send_command, command="show version")
    task.host['ver'] = ver_result.scrapli_response.genie_parse_output()
    uptime = task.host['ver']['version']['uptime']
    os_ver = task.host['ver']['version']['version_short']
    if os_ver == "15.6":
        print (f"[bold red]{task.host}[/bold red] [green]Uptime is[/green] [bold blue]{uptime}[/bold blue] & [yellow]has Golden OS Version[/yellow]")
    else:
        print (f"[bold red]{task.host}[/bold red] [green]Uptime is[/green] [bold blue]{uptime}[/bold blue] & [yellow]has {os_ver} OS Version[/yellow]")

nr.run (task=get_dev_uptime)

#ipdb.set_trace ()