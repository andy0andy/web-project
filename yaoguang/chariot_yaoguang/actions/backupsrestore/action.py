import chariot
from .schema import BackupsrestoreInput, BackupsrestoreOutput, Input, Output, Component
# Custom imports below


class Backupsrestore(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='backupsrestore',
                description=Component.DESCRIPTION,
                input=BackupsrestoreInput(),
                output=BackupsrestoreOutput())

    def run(self, params={}):
        # TODO: Implement run function

        backupname = params.get(Input.BACKUPNAME)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/backups/restore"


        try:
            
            yaoguang.addBody("backup_name", backupname)

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
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")


