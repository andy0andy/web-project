import chariot
from .schema import SyncconfigsyncInput, SyncconfigsyncOutput, Input, Output, Component
# Custom imports below


class Syncconfigsync(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='syncconfigsync',
                description=Component.DESCRIPTION,
                input=SyncconfigsyncInput(),
                output=SyncconfigsyncOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        consoleip = params.get(Input.CONSOLEIP)
        dbuser = params.get(Input.DBUSER)
        dbpass = params.get(Input.DBPASS)


        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/sync_config/sync"

        try:

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("error"):
                result.update({Output.ERROR: data['error']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")