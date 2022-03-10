~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.57

Output: 
set system ntp server 172.31.24.57 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.57

Output: 
set system name-server 172.31.24.57 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system time-zone America/Los_Angeles

Output: 
set system time-zone America/Los_Angeles 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
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
set system ntp server 172.31.24.57

Output: 
set system ntp server 172.31.24.57 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

Running:
set system name-server 172.31.24.57

Output: 
set system name-server 172.31.24.57 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

Running:
set system time-zone America/Los_Angeles

Output: 
set system time-zone America/Los_Angeles 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
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
set system ntp server 172.31.24.57

Output: 
set system ntp server 172.31.24.57 

{master:0}[edit]
jhu1@spsw05.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw05.corp.sjca> 

Running:
set system name-server 172.31.24.57

Output: 
set system name-server 172.31.24.57 

{master:0}[edit]
jhu1@spsw05.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw05.corp.sjca> 

Running:
set system time-zone America/Los_Angeles

Output: 
set system time-zone America/Los_Angeles 

{master:0}[edit]
jhu1@spsw05.corp.sjca# exit configuration-mode 
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
set system ntp server 172.31.24.57

Output: 
set system ntp server 172.31.24.57 

{master:0}[edit]
jhu1@spsw06.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw06.corp.sjca> 

Running:
set system name-server 172.31.24.57

Output: 
set system name-server 172.31.24.57 

{master:0}[edit]
jhu1@spsw06.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw06.corp.sjca> 

Running:
set system time-zone America/Los_Angeles

Output: 
set system time-zone America/Los_Angeles 

{master:0}[edit]
jhu1@spsw06.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw06.corp.sjca> 
commit
[edit protocols]
  'bgp'
    warning: requires 'bgp' license
[edit vlans v2501_dcs-mgmt]
  'vxlan'
    warning: requires 'vxlan' license
configuration check succeeds
commit complete

{master:0}[edit]
jhu1@spsw06.corp.sjca# 
