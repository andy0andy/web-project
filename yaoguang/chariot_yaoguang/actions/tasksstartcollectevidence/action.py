import chariot
from .schema import TasksstartcollectevidenceInput, TasksstartcollectevidenceOutput, Input, Output, Component
# Custom imports below


class Tasksstartcollectevidence(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasksstartcollectevidence',
                description=Component.DESCRIPTION,
                input=TasksstartcollectevidenceInput(),
                output=TasksstartcollectevidenceOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        
        cleanupsessions = params.get(Input.CLEANUPSESSIONS)
        collectsysinfo = params.get(Input.COLLECTSYSINFO)
        collectpasswd = params.get(Input.COLLECTPASSWD)
        collectssh = params.get(Input.COLLECTSSH)
        collectscreenshots = params.get(Input.COLLECTSCREENSHOTS)
        collectapps = params.get(Input.COLLECTAPPS)
        collectdrivers = params.get(Input.COLLECTDRIVERS)
        collectusers = params.get(Input.COLLECTUSERS)
        collectdomain = params.get(Input.COLLECTDOMAIN)
        collectfiles = params.get(Input.COLLECTFILES)
        collectfilespattern = params.get(Input.COLLECTFILESPATTERN)
        collectfilescount = params.get(Input.COLLECTFILESCOUNT)
        collectfilesize = params.get(Input.COLLECTFILESIZE)


        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/start_collect_evidence"

        try:
            

            yaoguang.addBody("workspace_id", workspaceid)
            
            if cleanupsessions:
                yaoguang.addBody("cleanup_sessions", cleanupsessions)
            if collectsysinfo:
                yaoguang.addBody("collect_sysinfo", collectsysinfo)
            if collectpasswd:
                yaoguang.addBody("collect_passwd", collectpasswd)
            if collectssh:
                yaoguang.addBody("collect_ssh", collectssh)
            if collectscreenshots:
                yaoguang.addBody("collect_screenshots", collectscreenshots)
            if collectapps:
                yaoguang.addBody("collect_apps", collectapps)
            if collectdrivers:
                yaoguang.addBody("collect_drives", collectdrivers)
            if collectusers:
                yaoguang.addBody("collect_users", collectusers)
            if collectdomain:
                yaoguang.addBody("collect_domain", collectdomain)
            if collectfiles:
                yaoguang.addBody("collect_files", collectfiles)
            if collectfilespattern:
                yaoguang.addBody("collect_files_pattern", collectfilespattern)
            if collectfilescount:
                yaoguang.addBody("collect_files_count", collectfilescount)
            if collectfilesize:
                yaoguang.addBody("collect_files_size", collectfilesize)

           
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