import chariot
from .schema import SocialengineeringtargetlistsInput, SocialengineeringtargetlistsOutput, Input, Output, Component
# Custom imports below


class Socialengineeringtargetlists(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='socialengineeringtargetlists',
                description=Component.DESCRIPTION,
                input=SocialengineeringtargetlistsInput(),
                output=SocialengineeringtargetlistsOutput())

    def run(self, params={}):
        # TODO: Implement run function
    
        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/social_engineering/target_lists"

        try:
        
            data, code = yaoguang.reqData(api, "GET")

            result = {
                Output.STATUSCODE: code
            }
            
            if data:
                result.update({Output.DATA: data})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")