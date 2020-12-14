import chariot
from .schema import WorkspacesreportsdownloadInput, WorkspacesreportsdownloadOutput, Input, Output, Component
# Custom imports below


class Workspacesreportsdownload(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='workspacesreportsdownload',
                description=Component.DESCRIPTION,
                input=WorkspacesreportsdownloadInput(),
                output=WorkspacesreportsdownloadOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        id = params.get(Input.ID)
        fomat = params.get(Input.FORMAT)

        yaoguang = self.connection.yaoguang

        api = f"/rest_api/v2/workspaces/{workspaceid}/reports/{id}/download"


        try:
            
            yaoguang.addParams("format", fomat)

            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }

            if data:
                result["data"] = {
                    "filename": f"{workspaceid}-{id}.{fomat}",
                    "content": data[data.find("base64,"):].lstrip("base64,")
                }

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")