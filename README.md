## Introduction
We have a project to refresh our access switches. One of the data point we would like to have is how many switchports are there on each switch stack and more importantly how many of them are actually utilized.

## Ansible Playbook

This playbook collects interfaces details using napalm_get_facts module. A jinja2 template is used with custom filers to:
- Calculate total number of interfaces in the switches stack.
- Calculate total number of interfaces with line protocol in UP state.
- Template also prints interfaces with UP state. 

At the end, Ansible assemble module is used to gather all results into one file.

## Custom Filters
Custom filters are tested with Cisco IOS. There may be some minor adjustments needed for other network operating systems. In interface selection logical interfaces like port-channels and vlans are excluded. The filter looks for keyword 'Ethernet' in the interface names.

## Output
The final results are presented in a text file of the following format.

```
----- PPA_SWITCH-01 -----
INFO: Total Interfaces: 109
INFO: UP Interfaces: 22
PPA_SWITCH-01  GigabitEthernet1/0/4
PPA_SWITCH-01  GigabitEthernet1/0/5
....
....
```

One can use egrep '\-\-|INFO' assembled.txt to get the executive summary from this file as shown below

```
----- PPA_SWITCH-01 -----
INFO: Total Interfaces: 109
INFO: UP Interfaces: 87
----- PPB_SWITCH-01 -----
INFO: Total Interfaces: 55
INFO: UP Interfaces: 23
----- PPC_SWITCH-01 -----
INFO: Total Interfaces: 271
INFO: UP Interfaces: 125

```
