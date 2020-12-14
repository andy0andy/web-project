import chariot
from .schema import TasklogcurrentlogInput, TasklogcurrentlogOutput, Input, Output, Component
# Custom imports below


class Tasklogcurrentlog(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasklogcurrentlog',
                description=Component.DESCRIPTION,
                input=TasklogcurrentlogInput(),
                output=TasklogcurrentlogOutput())

    def run(self, params={}):
        # TODO: Implement run function



        id = params.get(Input.ID)
        lineno = params.get(Input.LINENO)
        linenum = params.get(Input.LINENUM)


        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v3/task_log/{id}/current_log"

        try:
            
            yaoguang.addBody('line_no', lineno)
            yaoguang.addBody('line_num', linenum)

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
            if data.get("start_line_no"):
                result.update({Output.STARTLINENO: data['start_line_no']})
            if data.get("end_line_no"):
                result.update({Output.ENDLINENO: data['end_line_no']})
            if data.get("read_state"):
                result.update({Output.READSTATE: data['read_state']})



            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")