~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.55

Output: 
set system ntp server 172.31.24.55 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.55

Output: 
set system name-server 172.31.24.55 

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

Running:
show | compare

Output: 
show | compare 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
commit
Output: 
commit 
configuration check succeeds
commit complete

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw04

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

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
show | compare
Output: 
show | compare 
[edit system name-server]
    172.31.24.55 { ... }
+   172.31.24.56;
[edit system ntp]
     server 172.31.24.55 { ... }
+    server 172.31.24.56;

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 
<bound method JuniperBase.commit of <netmiko.juniper.juniper.JuniperSSH object at 0x7f7ac3b88400>>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw04

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

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
show | compare
Output: 
show | compare 
[edit system name-server]
    172.31.24.55 { ... }
+   172.31.24.56;
[edit system ntp]
     server 172.31.24.55 { ... }
+    server 172.31.24.56;

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 
<bound method JuniperBase.commit of <netmiko.juniper.juniper.JuniperSSH object at 0x7f7ac4ca3550>>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

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
show | compare
Output: 
show | compare 
[edit system name-server]
    172.31.24.55 { ... }
+   172.31.24.56;
[edit system ntp]
     server 172.31.24.55 { ... }
+    server 172.31.24.56;

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
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

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
show | compare
Output: 
show | compare 
[edit system name-server]
    172.31.24.55 { ... }
+   172.31.24.56;
[edit system ntp]
     server 172.31.24.55 { ... }
+    server 172.31.24.56;

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
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

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
configure 
Entering configuration mode
Users currently editing the configuration:
  root terminal u0 (pid 1669) on since 2019-05-29 22:04:22 PDT, idle 129w0d 16:28
      {master:0}[edit]
  jhu1 terminal p1 (pid 19137) on since 2021-11-18 13:23:37 PST, idle 00:10:38
      {master:0}[edit]

{master:0}[edit]
jhu1@spsw03.corp.sjca# show | compare 

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
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

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
show | compare 

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
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.56

Output: 
set system ntp server 172.31.24.56 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.56

Output: 
set system name-server 172.31.24.56 

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Connecting to device: spsw03

Running:
set system ntp server 172.31.24.57

Output: 
set system ntp server 172.31.24.57 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

Running:
set system name-server 172.31.24.57

Output: 
set system name-server 172.31.24.57 

{master:0}[edit]
jhu1@spsw03.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw03.corp.sjca> 

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
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

Running:
set system name-server 172.31.24.57

Output: 
set system name-server 172.31.24.57 

{master:0}[edit]
jhu1@spsw04.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw04.corp.sjca> 

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
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw05.corp.sjca> 

Running:
set system name-server 172.31.24.57

Output: 
set system name-server 172.31.24.57 

{master:0}[edit]
jhu1@spsw05.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw05.corp.sjca> 

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
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw06.corp.sjca> 

Running:
set system name-server 172.31.24.57

Output: 
set system name-server 172.31.24.57 

{master:0}[edit]
jhu1@spsw06.corp.sjca# exit configuration-mode 
The configuration has been changed but not committed
Exiting configuration mode

{master:0}
jhu1@spsw06.corp.sjca> 

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
