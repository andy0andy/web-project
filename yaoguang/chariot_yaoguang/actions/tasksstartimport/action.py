import chariot
from .schema import TasksstartimportInput, TasksstartimportOutput, Input, Output, Component
# Custom imports below


class Tasksstartimport(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasksstartimport',
                description=Component.DESCRIPTION,
                input=TasksstartimportInput(),
                output=TasksstartimportOutput())

    def run(self, params={}):
        # TODO: Implement run function
        

        workspaceid = params.get(Input.WORKSPACEID)
        file = params.get(Input.FILE)
        
        blackliststring = params.get(Input.BLACKLISTSTRING)
        tags = params.get(Input.TAGS)
        autotagos = params.get(Input.AUTOTAGOS)
        preservehosts = params.get(Input.PRESERVEHOSTS)


        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/start_import"

        try:
            

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("file", file)
          
            if blackstring:
                yaoguang.addBody("blacklist_string", blackstring)
            if tags:
                yaoguang.addBody("tags", tags)
            if autotagos:
                yaoguang.addBody("autotag_os", autotag_os)
            if preservehosts:
                yaoguang.addBody("preserve_hosts", preserve_hosts)
           
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