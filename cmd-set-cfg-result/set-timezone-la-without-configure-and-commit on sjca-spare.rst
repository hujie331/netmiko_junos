~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system time-zone America/Los_Angeles

Output: 
set system time-zone America/Los_Angeles 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:


Output: 


{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 
 

commit
 
configuration check succeeds
commit complete

{master:0}[edit]
jhu1@spsw03.corp.sjca# 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw04

Running:
set system time-zone America/Los_Angeles

Output: 
set system time-zone America/Los_Angeles 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

Running:


Output: 


{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 
 

commit
 
configuration check succeeds
commit complete

{master:0}[edit]
jhu1@spsw04.corp.sjca# 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw05

Running:
set system time-zone America/Los_Angeles

Output: 
set system time-zone America/Los_Angeles 

{master:0}[edit]
jhu1@spsw05.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw05.corp.sjca> 

Running:


Output: 


{master:0}[edit]
jhu1@spsw05.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw05.corp.sjca> 

commit
 
configuration check succeeds
commit complete

{master:0}[edit]
jhu1@spsw05.corp.sjca# 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw06

Running:
set system time-zone America/Los_Angeles

Output: 
set system time-zone America/Los_Angeles 

{master:0}[edit]
jhu1@spsw06.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw06.corp.sjca> 

Running:


Output: 


{master:0}[edit]
jhu1@spsw06.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw06.corp.sjca> 

commit
[edit interfaces ae0]
  'esi'
    warning: requires 'esi-lag' license
[edit protocols]
  'bgp'
    warning: requires 'bgp' license
[edit protocols evpn encapsulation]
  'encapsulation vxlan'
    warning: requires 'evpn-vxlan' license
[edit vlans v2501_dcs-mgmt]
  'vxlan'
    warning: requires 'vxlan' license
configuration check succeeds
commit complete

{master:0}[edit]
jhu1@spsw06.corp.sjca# 
