import chariot
from .schema import BackupsdeleteInput, BackupsdeleteOutput, Input, Output, Component
# Custom imports below


class Backupsdelete(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='backupsdelete',
                description=Component.DESCRIPTION,
                input=BackupsdeleteInput(),
                output=BackupsdeleteOutput())

    def run(self, params={}):
        # TODO: Implement run function
        

        backupname = params.get(Input.BACKUPNAME)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/backups/delete"


        try:
            
            yaoguang.addBody("backup_name", backupname)

            data, code = yaoguang.reqData(api, "DELETE")

            result = {
                Output.STATUSCODE: code
            }

            if data.get("result"):
                result["result"] = data.get("result")
            

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")


