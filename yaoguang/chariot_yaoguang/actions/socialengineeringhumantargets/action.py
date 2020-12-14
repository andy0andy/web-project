import chariot
from .schema import SocialengineeringhumantargetsInput, SocialengineeringhumantargetsOutput, Input, Output, Component
# Custom imports below


class Socialengineeringhumantargets(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='socialengineeringhumantargets',
                description=Component.DESCRIPTION,
                input=SocialengineeringhumantargetsInput(),
                output=SocialengineeringhumantargetsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v2/social_engineering/human_targets"

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