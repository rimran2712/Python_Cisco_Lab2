from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command
import os
import ipdb
from rich import print

nr = InitNornir (config_file="/home/imran/Documents/Automation/Nornir/Runbooks_Repositories/Python_Cisco_Lab2/Inventory/config.yaml")

# Clearing the Screen
os.system('clear')

"""
This program will execute "show ip interface" command and will store structure data using Genie Parser
in interface_info variable which will embend to our inventory as key where we can manipulate
this data and use in our program 
we will also check if interface status is up than we will print device name, interface and status
"""

"""
IPDB Inspection of inteface_info

ipdb> pp nr.inventory.hosts['vIOS-R1']['interface_info']
{'GigabitEthernet0/0': {'address_determined_by': 'non-volatile memory',
                        'bgp_policy_mapping': False,
                        'directed_broadcast_forwarding': False,
                        'enabled': True,
                        'icmp': {'mask_replies': 'never sent',
                                 'redirects': 'always sent',
                                 'unreachables': 'always sent'},
                        'input_features': ['MCI Check'],
                        'ip_access_violation_accounting': False,
                        'ip_cef_switching': True,
                        'ip_cef_switching_turbo_vector': True,
                        'ip_fast_switching': True,
                        'ip_flow_switching': False,
                        'ip_multicast_distributed_fast_switching': False,
                        'ip_multicast_fast_switching': True,
                        'ip_output_packet_accounting': False,
                        'ip_route_cache_flags': ['CEF', 'Fast'],
                        'ipv4': {'172.16.100.2/30': {'broadcast_address': '255.255.255.255',
                                                     'ip': '172.16.100.2',
                                                     'prefix_length': '30',
                                                     'secondary': False}},
                        'local_proxy_arp': False,
                        'mtu': 1500,
                        'network_address_translation': False,
                        'oper_status': 'up',
                        'policy_routing': False,
                        'proxy_arp': True,
                        'router_discovery': False,
                        'rtp_ip_header_compression': False,
                        'security_level': 'default',
                        'split_horizon': True,
                        'tcp_ip_header_compression': False,
                        'vrf': 'MGMT',
                        'wccp': {'redirect_exclude': False,
                                 'redirect_inbound': False,
                                 'redirect_outbound': False}},
 'GigabitEthernet0/1': {'enabled': False, 'oper_status': 'down'},
 'GigabitEthernet0/2': {'enabled': False, 'oper_status': 'down'},
 'GigabitEthernet0/3': {'enabled': False, 'oper_status': 'down'}}
ipdb> 

"""

def get_interface_info (task):
    interface_result = task.run(task=netmiko_send_command, command_string="show ip interface", use_genie = True)
    task.host['interface_info'] = interface_result.result
    interfaces = task.host['interface_info']
    
    for interface in interfaces.keys():
        int_name = interface
        int_oper_status = interfaces[interface]['oper_status']
        if int_oper_status == 'up':
            print (f"[yellow bold]{task.host}[/yellow bold] [blue]{int_name}[/blue] [red]is up[/red]")

get_interface_info_results = nr.run (task=get_interface_info)
#print_result (get_interface_info_results)
#ipdb.set_trace ()