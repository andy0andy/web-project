import chariot
from .schema import WorkspacesupdateInput, WorkspacesupdateOutput, Input, Output, Component
# Custom imports below


class Workspacesupdate(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacesupdate',
                description=Component.DESCRIPTION,
                input=WorkspacesupdateInput(),
                output=WorkspacesupdateOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        name = params.get(Input.NAME)
        description = params.get(Input.DESCRIPTION)
        boundary = params.get(Input.BOUNDARY)
        limit_to_network = params.get(Input.LIMIT_TO_NETWORK)
        id = params.get(Input.ID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{id}"

        try:
            yaoguang.addBody("name", name)
            yaoguang.addBody("description", description)
            yaoguang.addBody("boundary", boundary)
            yaoguang.addBody("limit_to_network", limit_to_network)

            data, code = yaoguang.reqData(api, "PUT")
          
            result = {
                Output.STATUSCODE: code
            }

            if data.get("result"):
                result.update({Output.RESULT: data['result']})

            if data.get("workspace"):
                result.update({Output.WORKSPACE: data['workspace']})

            return result

        except Exception as e:
            raise Exception(f"{self.__class__} - {str(e)}")
