import chariot
from .schema import ValidatevulnsresultsInput, ValidatevulnsresultsOutput, Input, Output, Component
# Custom imports below


class Validatevulnsresults(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='validatevulnsresults',
                description=Component.DESCRIPTION,
                input=ValidatevulnsresultsInput(),
                output=ValidatevulnsresultsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        taskid = params.get(Input.TASKID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/validate_vulns/results"

        try:
        
            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("task_id", taskid)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("result"):
                result.update({Output.RESULT: data['result']})
            if data.get("error"):
                result.update({Output.ERROR: data['error']})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")