import chariot
from .schema import WorkspaceshostsInput, WorkspaceshostsOutput, Input, Output, Component
# Custom imports below


class Workspaceshosts(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspaceshosts',
                description=Component.DESCRIPTION,
                input=WorkspaceshostsInput(),
                output=WorkspaceshostsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspacesid = params.get(Input.WORKSPACESID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{workspacesid}/hosts"

        try:
        
            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }
            
            if data:
                result.update({Output.DATA: data})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")

