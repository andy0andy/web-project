import chariot
from .schema import BackupscreateInput, BackupscreateOutput, Input, Output, Component
# Custom imports below


class Backupscreate(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='backupscreate',
                description=Component.DESCRIPTION,
                input=BackupscreateInput(),
                output=BackupscreateOutput())

    def run(self, params={}):
        # TODO: Implement run function



        name = params.get(Input.NAME)
        description = params.get(Input.DESCRIPTION)
        
        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/backups"

        try:

            yaoguang.addBody("name", name)
            yaoguang.addBody("description", description)

            data, code = yaoguang.reqData(api, "POST")
          
            result = {
                Output.STATUSCODE: code
            }

            if data.get("result"):
                result["result"] = data.get("result")
            
            if data.get("message"):
                result["message"] = data.get("message")


            return result

        except Exception as e:
            raise Exception(f"{self.__class__} - {str(e)}")