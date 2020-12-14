import chariot
from .schema import WorkspacesreportsgenerateInput, WorkspacesreportsgenerateOutput, Input, Output, Component
# Custom imports below


class Workspacesreportsgenerate(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacesreportsgenerate',
                description=Component.DESCRIPTION,
                input=WorkspacesreportsgenerateInput(),
                output=WorkspacesreportsgenerateOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)

        report = params.get(Input.REPORT)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{workspaceid}/reports/generate"


        try:

            yaoguang.addBody("report", report)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }

            if data.get("result"):
                result["result"] = data.get("result")
            
            if data.get("report_id"):
                result["report_id"] = data.get("report_id")

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")