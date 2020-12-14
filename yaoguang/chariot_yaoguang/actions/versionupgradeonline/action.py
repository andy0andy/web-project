import chariot
from .schema import VersionupgradeonlineInput, VersionupgradeonlineOutput, Input, Output, Component
# Custom imports below


class Versionupgradeonline(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='versionupgradeonline',
                description=Component.DESCRIPTION,
                input=VersionupgradeonlineInput(),
                output=VersionupgradeonlineOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        
        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/version/upgrade_online"


        try:

            data, code = yaoguang.reqData(api, "GET")

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