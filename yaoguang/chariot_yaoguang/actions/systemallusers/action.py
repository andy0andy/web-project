import chariot
from .schema import SystemallusersInput, SystemallusersOutput, Input, Output, Component
# Custom imports below


class Systemallusers(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='systemallusers',
                description=Component.DESCRIPTION,
                input=SystemallusersInput(),
                output=SystemallusersOutput())

    def run(self, params={}):
        # TODO: Implement run function

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v4/system/all_users"


        try:

            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }

            if data.get("status"):
                result["status"] = data.get("status")
            
            if data.get("all_user"):
                result["allusers"] = data.get("all_user")

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")