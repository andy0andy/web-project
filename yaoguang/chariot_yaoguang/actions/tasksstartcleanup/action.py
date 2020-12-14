import chariot
from .schema import TasksstartcleanupInput, TasksstartcleanupOutput, Input, Output, Component
# Custom imports below


class Tasksstartcleanup(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasksstartcleanup',
                description=Component.DESCRIPTION,
                input=TasksstartcleanupInput(),
                output=TasksstartcleanupOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        cleanupsessions = params.get(Input.CLEANUPSESSIONS)


        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/start_cleanup"

        try:
            

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("cleanup_sessions", cleanupsessions)

           
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