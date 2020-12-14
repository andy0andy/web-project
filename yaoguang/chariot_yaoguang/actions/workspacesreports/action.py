import chariot
from .schema import WorkspacesreportsInput, WorkspacesreportsOutput, Input, Output, Component
# Custom imports below


class Workspacesreports(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacesreports',
                description=Component.DESCRIPTION,
                input=WorkspacesreportsInput(),
                output=WorkspacesreportsOutput())

    def run(self, params={}):
        # TODO: Implement run function

        workspaceid = params.get(Input.WORKSPACEID)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{workspaceid}/reports"


        try:

            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }

            if data:
                result['data'] = data


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")