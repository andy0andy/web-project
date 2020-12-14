import chariot
from .schema import TasksstartscanInput, TasksstartscanOutput, Input, Output, Component
# Custom imports below


class Tasksstartscan(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasksstartscan',
                description=Component.DESCRIPTION,
                input=TasksstartscanInput(),
                output=TasksstartscanOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        addressstring = params.get(Input.ADDRESSSTRING)

        blackstring = params.get(Input.BLACKSTRING)
        initialnmap = params.get(Input.INITIALNMAP)
        customnmap = params.get(Input.CUSTOMNMAP)
        portsextra = params.get(Input.PORTSEXTRA)
        portsblacklist = params.get(Input.PORTSBLACKLIST)
        portscustom = params.get(Input.PORTSCUSTOM)
        portscansourceport = params.get(Input.PORTSCANSOURCEPORT)
        fastdetect = params.get(Input.FASTDETECT)
        porttscanspeed = params.get(Input.PORTTSCANSPEED)
        portscantimeout = params.get(Input.PORTSCANTIMEOUT)
        udpprobes = params.get(Input.UDPPROBES)
        snmpscan = params.get(Input.SNMPSCAN)
        h323scan = params.get(Input.H323SCAN)
        fingerusers = params.get(Input.FINGERUSERS)
        identifyservices = params.get(Input.IDENTIFYSERVICES)
        singlescan = params.get(Input.SINGLESCAN)
        dryrun = params.get(Input.DRYRUN)
        initialwebscan = params.get(Input.INITIALWEBSCAN)
        smbusernmae = params.get(Input.SMBUSERNMAE)
        smbpassword = params.get(Input.SMBPASSWORD)
        smbdomain = params.get(Input.SMBDOMAIN)
        webscanmaxpages = params.get(Input.WEBSCANMAXPAGES)
        webscanmaxminute = params.get(Input.WEBSCANMAXMINUTE)
        webscanmaxthreads = params.get(Input.WEBSCANMAXTHREADS)
        autotagos = params.get(Input.AUTOTAGOS)
        httpusername = params.get(Input.HTTPUSERNAME)
        httppassword = params.get(Input.HTTPPASSWORD)
        httpdomian = params.get(Input.HTTPDOMIAN)
        cookie = params.get(Input.COOKIE)
        useragent = params.get(Input.USERAGENT)




        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/start_scan"

        try:
            

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("address_string", addressstring)

            if blackstring:
                yaoguang.addBody("blacklist_string", blackstring)
            if initialnmap:
                yaoguang.addBody("initial_nmap", initialnmap)
            if customnmap:
                yaoguang.addBody("custom_nmap", customnmap)
            if portsextra:
                yaoguang.addBody("ports_extra", portsextra)
            if portsblacklist:
                yaoguang.addBody("ports_blacklist", portsblacklist)
            if portscustom:
                yaoguang.addBody("ports_custom", portscustom)
            if portscansourceport:
                yaoguang.addBody("portscan_source_port", portscansourceport)
            if fastdetect:
                yaoguang.addBody("fast_detect", fastdetect)
            if porttscanspeed:
                yaoguang.addBody("portscan_speed", porttscanspeed)
            if portscantimeout:
                yaoguang.addBody("portscan_timeout", portscantimeout)
            if udpprobes:
                yaoguang.addBody("udp_probes", udpprobes)
            if snmpscan:
                yaoguang.addBody("snmp_scan", snmpscan)
            if h323scan:
                yaoguang.addBody("h323_scan", h323scan)
            if fingerusers:
                yaoguang.addBody("finger_users", fingerusers)
            if identifyservices:
                yaoguang.addBody("identify_services", identifyservices)
            if singlescan:
                yaoguang.addBody("single_scan", singlescan)
            if dryrun:
                yaoguang.addBody("dry_run", dryrun)
            if initialwebscan:
                yaoguang.addBody("initial_webscan", initialwebscan)
            if smbusernmae:
                yaoguang.addBody("smb_username", smbusernmae)
            if smbpassword:
                yaoguang.addBody("smb_password", smbpassword
            if smbdomain:
                yaoguang.addBody("smb_domain", smbdomain)
            if webscanmaxpages:
                yaoguang.addBody("webscan_max_pages", webscanmaxpages)
            if webscanmaxminute:
                yaoguang.addBody("webscan_max_minutes", webscanmaxminute)
            if webscanmaxthreads:
                yaoguang.addBody("webscan_max_threads", webscanmaxthreads)
            if autotagos:
                yaoguang.addBody("autotag_os, autotagos)
            if httpusername:
                yaoguang.addBody("http_username", httpusername)
            if httppassword:
                yaoguang.addBody("http_password", httppassword)
            if httpdomian:
                yaoguang.addBody("http_domian", httpdomian)
            if cookie:
                yaoguang.addBody("cookie", cookie)
            if useragent:
                yaoguang.addBody("user_agent", useragent)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("success"):
                result.update({Output.SUCCESS: data['success']})
            if data.get("workspace_id"):
                result.update({Output.WORKSPACEID: data['workspace_id']})
            if data.get("task_id"):
                result.update({Output.TASKID: data['task_id']})
            if data.get("errors"):
                result.update({Output.ERRORS: data['errors']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")