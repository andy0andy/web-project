import chariot
from .schema import TaskswebdataInput, TaskswebdataOutput, Input, Output, Component
# Custom imports below


class Taskswebdata(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='taskswebdata',
                description=Component.DESCRIPTION,
                input=TaskswebdataInput(),
                output=TaskswebdataOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        operation = params.get(Input.OPERATION)
        

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/web_data"

        try:
            

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("operation", operation)
            
           
            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("success"):
                result.update({Output.SUCCESS: data['success']})
            if data.get("workspace_id"):
                result.update({Output.WORKSPACEID: data['workspace_id']})
            if data.get("data"):
                result.update({Output.DATA: data['data']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")