import chariot
from .schema import TasklogtotallogInput, TasklogtotallogOutput, Input, Output, Component
# Custom imports below


class Tasklogtotallog(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasklogtotallog',
                description=Component.DESCRIPTION,
                input=TasklogtotallogInput(),
                output=TasklogtotallogOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        id = params.get(Input.ID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v3/task_log/{id}/total_log"

        try:

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("error"):
                result.update({Output.ERROR: data['error']})
            if data.get("content"):
                result.update({Output.CONTENT: data['content']})
            if data.get("path"):
                result.update({Output.PATH: data['path']})
            if data.get("state"):
                result.update({Output.STATE: data['state']})



            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")