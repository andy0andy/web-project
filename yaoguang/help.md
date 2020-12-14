# 碳泽 - 摇光

## About
碳泽-摇光 API接口

## Actions

### validatevulnsvalidate



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|report|file|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|status|string|false||<no value>|
|ids|object|false||<no value>|
|error|string|false||<no value>|
|statuscode|integer|true||<no value>|

### taskswebdata



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|operation|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|data|object|false||<no value>|
|statuscode|integer|true||<no value>|

### tasksstartwebscan



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|useragent|string|false||<no value>|
|knowntargets|string|false|JSON字符串, //POST /rest_api/v3/tasks/web_data, 返回data数据作为这个参数值|<no value>|
|excludepathpatterns|string|false||<no value>|
|httpusername|string|false||<no value>|
|httppassword|string|false||<no value>|
|workspaceid|string|true||<no value>|
|reportweak|boolean|false||<no value>|
|cookie|string|false||<no value>|
|urls|string|true||<no value>|
|maxpages|integer|false||<no value>|
|maxminutes|integer|false||<no value>|
|maxthreads|integer|false||<no value>|
|unauthorizedaccessforbiddenphrases|string|false||<no value>|
|sslreuired|boolean|false||<no value>|
|httpdomain|string|false||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|

### workspaceshostssessions



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|hostid|string|true||<no value>|
|workspacesid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspaceshostsserviceswebsiteswebvulns



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|
|websitesid|string|true||<no value>|
|workspacesid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspacescampaignswebpagesdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspacescampaignsvisits



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### loots



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|false||<no value>|
|hostid|string|false||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|loots|array|false||<no value>|

### sessionsdestroy



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|errors|string|false||<no value>|

### tasksstarttunnel



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|tunneldhcp|string|true||<no value>|
|tunneladdress|string|true||<no value>|
|tunnelnetmask|string|true||<no value>|
|workspaceid|string|true||<no value>|
|tunnelsession|string|true||<no value>|
|tunnelinterface|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|

### socialengineeringhumantargets



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspacescampaignsemails



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|data|array|false||<no value>|
|statuscode|integer|true||<no value>|

### syncconfigsync



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|dbpass|string|true||<no value>|
|consoleip|string|true||<no value>|
|dbuser|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|error|string|false||<no value>|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|

### tasklogtotallog



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|path|string|false||<no value>|
|state|string|false||<no value>|
|content|string|false||<no value>|
|error|string|false||<no value>|

### sessionsupload



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|
|path|string|true||<no value>|
|file|file|true||<no value>|
|Name|string|true||<no value>|
|execute|boolean|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### versionupgradeonline



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|result|string|false||<no value>|
|message|string|false||<no value>|

### workspaceshostsserviceswebsiteswebformsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|
|websitesid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### socialengineeringtargetlists



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspacescampaignsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspacescampaignswebpages



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### sessionsdownload



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|
|path|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|data|object|false||<no value>|
|statuscode|integer|true||<no value>|

### backupssee



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|result|string|false||<no value>|
|backups|array|false||<no value>|
|statuscode|integer|true||<no value>|

### workspaceshostsservices



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### sessionsfiles



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|false||<no value>|
|sessionid|string|false||<no value>|
|path|string|false|如果为空，则返回pwd当前目录下的文件夹和文件|<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspacescampaigns



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### tasksstartwebaudit



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|httppassword|string|false||<no value>|
|httpdomain|string|false||<no value>|
|cookie|string|false||<no value>|
|useragent|string|false||<no value>|
|workspaceid|string|true||<no value>|
|maxminutes|integer|false||<no value>|
|httpusername|string|false||<no value>|
|sessioncookiename|string|false||<no value>|
|directobjectreference|boolean|false||<no value>|
|knowntargets|string|false|JSON字符串, //POST /rest_api/v3/tasks/web_data, 返回data数据作为这个参数值|<no value>|
|maxthreads|integer|false||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|

### workspacesid



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### backupsdelete



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|backupname|array|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|result|string|false||<no value>|

### versionupgradeoffline



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|updatefile|file|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|result|string|false||<no value>|
|message|string|false||<no value>|

### workspaceshostsnotes



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspacescampaignsphishingresults



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### tasksstartexploit



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|blacklistports|string|false||<no value>|
|filterbyport|boolean|false||<no value>|
|speed|string|false||<no value>|
|httpusername|string|false||<no value>|
|minimumrank|string|true||<no value>|
|payloadports|string|false||<no value>|
|payloadhost|string|false||<no value>|
|stageencodeing|string|false||<no value>|
|useragent|string|false||<no value>|
|timeout|string|false||<no value>|
|evasionleveltcp|string|false||<no value>|
|evasionlevelapp|string|false||<no value>|
|httppassword|string|false||<no value>|
|workspaceid|string|true||<no value>|
|whiteliststring|string|true||<no value>|
|blackliststring|string|false||<no value>|
|whitelistports|string|false||<no value>|
|httpdomain|string|false||<no value>|
|macroname|string|false||<no value>|
|dynamicstager|string|false||<no value>|
|limitsessions|boolean|false||<no value>|
|onlymatch|boolean|false||<no value>|
|payloadtype|string|false||<no value>|
|connection|string|false||<no value>|
|filterbyos|boolean|false||<no value>|
|cookie|string|false||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|

### validatevulnsresults



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|taskid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|result|array|false||<no value>|
|error|string|false||<no value>|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|

### workspacesupdate



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|
|name|string|true||<no value>|
|description|string|true||<no value>|
|boundary|string|true||<no value>|
|limit_to_network|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|result|string|true||<no value>|
|workspace|object|false||<no value>|

### workspacesreportsdownload



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|id|string|true||<no value>|
|format|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|file|false||<no value>|

### workspaceshostsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|host|object|false||<no value>|
|services|array|false||<no value>|

### workspaceshostsnotesdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspaceshostsserviceswebsitesdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspaceshostsserviceswebsiteswebpagesdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|
|websitesid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspacescampaignsemailopenings



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### sessionsshow



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspaces



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### backupsrestore



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|backupname|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|result|string|false||<no value>|
|message|string|false||<no value>|

### lootsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|lootid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|contenttype|string|false||<no value>|
|message|string|false||<no value>|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|path|string|false||<no value>|
|content|string|false||<no value>|

### sessionssession



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|sessionid|string|true||<no value>|
|workspaceid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### sessionssearch



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|
|query|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|sessionid|string|false||<no value>|
|entries|array|false||<no value>|

### tasksstartcollectevidence



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|collectfilescount|integer|false||<no value>|
|workspaceid|string|true||<no value>|
|collectfilespattern|string|false||<no value>|
|collectapps|boolean|false||<no value>|
|collectdrivers|boolean|false||<no value>|
|collectdomain|boolean|false||<no value>|
|collectpasswd|boolean|false||<no value>|
|collectscreenshots|boolean|false||<no value>|
|collectfiles|boolean|false|如果值为true，必须配置collect_files_pattern、collect_files_count和collect_files_size参数对应值，且collect_files_pattern不能为空,collect_files_count>=1, collect_files_size>=0.1|<no value>|
|collectsessions|array|false||<no value>|
|collectsysinfo|boolean|false||<no value>|
|collectfilesize|number|false||<no value>|
|collectssh|boolean|false||<no value>|
|collectusers|boolean|false||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|

### systemserverstatus



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|server_status|object|false||<no value>|

### socialengineeringtargetlistsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspacescampaignsemailopeningsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|data|object|false||<no value>|
|statuscode|integer|true||<no value>|

### syncconfigstatus



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|randomstring|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|error|string|false||<no value>|
|randomstring|string|false||<no value>|

### tasksnewtunnel



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### sessionsdelete



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|
|path|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### sessionsshell



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|sessionid|string|true||<no value>|
|special|string|false||<no value>|
|cmd|string|false||<no value>|
|read|boolean|false||<no value>|
|workspaceid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|event|string|false||<no value>|

### workspaceshostsserviceswebsiteswebvulnsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|
|websitesid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspacescampaignsemailsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspacescampaignsphishingresultsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### sslcertdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|sslcertid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|path|string|false||<no value>|
|content|string|false||<no value>|
|message|string|false||<no value>|

### tasklogcurrentlog



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|
|lineno|string|true||<no value>|
|linenum|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|error|string|false||<no value>|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|content|string|false||<no value>|
|startlineno|string|false||<no value>|
|endlineno|string|false||<no value>|
|readstate|string|false||<no value>|

### tasksstartscan



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|fingerusers|boolean|false||<no value>|
|smbpassword|string|false||<no value>|
|h323scan|boolean|false||<no value>|
|portsextra|boolean|false||<no value>|
|identifyservices|boolean|false||<no value>|
|initialwebscan|boolean|false||<no value>|
|smbusernmae|string|false||<no value>|
|workspaceid|string|true||<no value>|
|smbdomain|string|false||<no value>|
|snmpscan|boolean|false||<no value>|
|porttscanspeed|integer|false||<no value>|
|portscantimeout|string|false||<no value>|
|httpusername|string|false||<no value>|
|addressstring|string|true||<no value>|
|httpdomian|string|false||<no value>|
|customnmap|string|false||<no value>|
|portsblacklist||false||<no value>|
|portscansourceport|string|false||<no value>|
|cookie|string|false||<no value>|
|initialnmap|boolean|false||<no value>|
|dryrun|boolean|false||<no value>|
|webscanmaxpages|String|false||<no value>|
|webscanmaxminute|String|false||<no value>|
|autotagos|string|false||<no value>|
|useragent|string|false||<no value>|
|fastdetect|boolean|false||<no value>|
|portscustom|string|false||<no value>|
|udpprobes|boolean|false||<no value>|
|singlescan|boolean|false||<no value>|
|webscanmaxthreads|string|false||<no value>|
|httppassword|string|false||<no value>|
|blackstring|string|false||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|
|statuscode|integer|true||<no value>|

### systemloginuser



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|status|string|false||<no value>|
|loginuser|object|false||<no value>|
|statuscode|integer|true||<no value>|

### workspaceshostsservicesvulns



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### payloaddetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|payloadid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|message|string|false||<no value>|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|path|string|false||<no value>|
|content|string|false||<no value>|

### tasksstartbruteforcereuse



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|coreids|array|true||<no value>|
|serviceids|array|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|

### workspaceshostsservicesdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspaceshostsserviceswebsiteswebform



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|serviceid|string|true||<no value>|
|websitesid|string|true||<no value>|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspaceshostsserviceswebsiteswebpages



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|
|websitesid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspacescampaignsvisitsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|campaignid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|data|object|false||<no value>|
|statuscode|integer|true||<no value>|

### sessionshistory



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### tasksstartmodulerun



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|path|string|true||<no value>|
|whiteliststring|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|

### tasksstartcleanup



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|cleanupsessions|array|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|

### workspacesdelete



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|result|string|false||<no value>|

### systemallusers



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|status|string|false||<no value>|
|allusers|array|false||<no value>|

### workspaceshosts



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspaceshostssessionsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### socialengineeringhumantargetsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### creds



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|status|string|false||<no value>|
|creds|array|false||<no value>|
|statuscode|integer|true||<no value>|

### tasksstartimport



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|file|file|true||<no value>|
|blackliststring|string|false||<no value>|
|tags|string|false||<no value>|
|autotagos|boolean|false||<no value>|
|preservehosts|boolean|false||<no value>|
|workspaceid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|errors|string|false||<no value>|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|

### backupscreate



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|name|string|true||<no value>|
|description|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|result|string|true||<no value>|
|message|string|false||<no value>|

### workspacesreportsgenerate



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|report|reportstype|false||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|result|string|false||<no value>|
|report_id|string|false||<no value>|

### sessionsvnc



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|
|sessionid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### tasksstartwebsploit



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|useragent|string|false||<no value>|
|timeout|string|false||<no value>|
|limitsessions|boolean|false||<no value>|
|httpusername|string|false||<no value>|
|httppassword|string|false||<no value>|
|payloadports|string|false||<no value>|
|payloadhosts|string|false||<no value>|
|httpdomain|string|false||<no value>|
|cookie|string|false||<no value>|
|workspaceid|string|true||<no value>|
|targets|string|false|JSON字符串, //POST /rest_api/v3/tasks/web_data, 返回data数据作为这个参数值|<no value>|
|payloadtype|string|false||<no value>|
|connection|string|false||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|false||<no value>|
|taskid|string|false||<no value>|
|errors|string|false||<no value>|
|statuscode|integer|true||<no value>|
|success|string|false||<no value>|

### workspacescreate



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|name|string|true||<no value>|
|description|string|true||<no value>|
|boundary|string|true||<no value>|
|limit_to_network|string|true||<no value>|
|owner_id|string|true|创建项目时必填，更新时不填|<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|result|string|false||<no value>|
|workspace|object|false||<no value>|
|path|string|false||<no value>|
|statuscode|integer|true||<no value>|

### workspacesreports



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspaceid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|array|false||<no value>|

### workspaceshostsservicesvulnsdetail



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|
|id|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|statuscode|integer|true||<no value>|
|data|object|false||<no value>|

### workspaceshostsserviceswebsites



#### Input

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|workspacesid|string|true||<no value>|
|hostid|string|true||<no value>|
|serviceid|string|true||<no value>|


#### Output

|Name|Type|Required|Description|Default|
|----|----|--------|-----------|-------|
|data|array|false||<no value>|
|statuscode|integer|true||<no value>|


## Triggers



## Connection

|Name|Type|Required|Description|
|----|----|--------|-----------|
|token||true||
|host|string|true||


## Types


### workspacetype

|Name|Type|Required|Description|
|----|----|--------|-----------|
|boundary|string|true||
|limit_to_network|string|true||
|owner_id|string|false|创建项目时必填，更新时不填|
|name|string|true||
|description|string|true||

### reportstype

|Name|Type|Required|Description|
|----|----|--------|-----------|
|excluded_addresses|string|true||
|sections|string|true||
|options|string|true||
|email_recipients|string|true||
|report_type|string|true||
|file_fomats|string|true||
|name|string|true||
|included_addresses|string|true||

### qbtargettype

|Name|Type|Required|Description|
|----|----|--------|-----------|
|whitelisthost|string|true||
|blacklisthosts|string|true||
|allservices|boolean|true||
|type|string|true||

### qbcreds

|Name|Type|Required|Description|
|----|----|--------|-----------|
|importworkspacecreds|boolean|true||
|factorydefaults|boolean|true||

### quickbruteforcetype

|Name|Type|Required|Description|
|----|----|--------|-----------|
|target|qbtargettype|false||
|creds|qbcredstype|false||


## 版本信息

## 参考引用