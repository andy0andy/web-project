import chariot
from .schema import VersionupgradeofflineInput, VersionupgradeofflineOutput, Input, Output, Component
# Custom imports below


class Versionupgradeoffline(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='versionupgradeoffline',
                description=Component.DESCRIPTION,
                input=VersionupgradeofflineInput(),
                output=VersionupgradeofflineOutput())

    def run(self, params={}):
        # TODO: Implement run function

        updatefile = params.get(Input.UPDATEFILE)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/version/upgrade_offline"


        try:
            
            yaoguang.addBody("update_file", updatefile)

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