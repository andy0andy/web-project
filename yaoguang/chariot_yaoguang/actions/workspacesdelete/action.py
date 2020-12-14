import chariot
from .schema import WorkspacesdeleteInput, WorkspacesdeleteOutput, Input, Output, Component
# Custom imports below


class Workspacesdelete(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacesdelete',
                description=Component.DESCRIPTION,
                input=WorkspacesdeleteInput(),
                output=WorkspacesdeleteOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        id = params.get(Input.ID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{id}"

        try:

            data, code = yaoguang.reqData(api, "DELETE")
          
            result = {
                Output.STATUSCODE: code
            }

            if data.get("result"):
                result["result"] = data.get("result")

            return result

        except Exception as e:
            raise Exception(f"{self.__class__} - {str(e)}")