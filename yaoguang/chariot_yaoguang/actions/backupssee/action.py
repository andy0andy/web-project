import chariot
from .schema import BackupsseeInput, BackupsseeOutput, Input, Output, Component
# Custom imports below


class Backupssee(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='backupssee',
                description=Component.DESCRIPTION,
                input=BackupsseeInput(),
                output=BackupsseeOutput())

    def run(self, params={}):
        # TODO: Implement run function
    

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/backups"

        try:

            data, code = yaoguang.reqData(api, "GET")
          
            result = {
                Output.STATUSCODE: code
            }

            if data.get("result"):
                result["result"] = data.get("result")
            
            if data.get("backups"):
                result["backups"] = data.get("backups")

            return result

        except Exception as e:
            raise Exception(f"{self.__class__} - {str(e)}")