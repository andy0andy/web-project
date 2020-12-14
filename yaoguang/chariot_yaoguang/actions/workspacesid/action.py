import chariot
from .schema import WorkspacesidInput, WorkspacesidOutput, Input, Output, Component
# Custom imports below


class Workspacesid(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacesid',
                description=Component.DESCRIPTION,
                input=WorkspacesidInput(),
                output=WorkspacesidOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        id = params.get(Input.ID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{id}"

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
