import chariot
from .schema import SystemloginuserInput, SystemloginuserOutput, Input, Output, Component
# Custom imports below


class Systemloginuser(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='systemloginuser',
                description=Component.DESCRIPTION,
                input=SystemloginuserInput(),
                output=SystemloginuserOutput())

    def run(self, params={}):
        # TODO: Implement run function
        

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v4/system/login_user"


        try:

            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }

            if data.get("status"):
                result["status"] = data.get("status")
            
            if data.get("login_user"):
                result["loginuser"] = data.get("login_user")

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")