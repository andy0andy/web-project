import chariot
from .schema import WorkspacescreateInput, WorkspacescreateOutput, Input, Output, Component
# Custom imports below


class Workspacescreate(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacescreate',
                description=Component.DESCRIPTION,
                input=WorkspacescreateInput(),
                output=WorkspacescreateOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        name = params.get(Input.NAME)
        description = params.get(Input.DESCRIPTION)
        boundary = params.get(Input.BOUNDARY)
        limit_to_network = params.get(Input.LIMIT_TO_NETWORK)
        owner_id = params.get(Input.OWNER_ID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/workspaces"

        try:
            yaoguang.addBody("name", name)
            yaoguang.addBody("description", description)
            yaoguang.addBody("boundary", boundary)
            yaoguang.addBody("limit_to_network", limit_to_network)
            yaoguang.addBody("name", owner_id)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }

            if data.get("result"):
                result.update({Output.RESULT: data['result']})

            if data.get("workspace"):
                result.update({Output.WORKSPACE: data['workspace']})

            if data.get("path"):
                result.update({Output.PATH: data['path']})

            return result

        except Exception as e:
            raise Exception(f"{self.__class__} - {str(e)}")
