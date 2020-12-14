import chariot
from .schema import SystemserverstatusInput, SystemserverstatusOutput, Input, Output, Component
# Custom imports below


class Systemserverstatus(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='systemserverstatus',
                description=Component.DESCRIPTION,
                input=SystemserverstatusInput(),
                output=SystemserverstatusOutput())

    def run(self, params={}):
        # TODO: Implement run function
        

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v4/system/server_status"


        try:

            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }

            if data.get("status"):
                result["status"] = data.get("status")
            
            if data.get("server_status"):
                result["server_status"] = data.get("server_status")

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")