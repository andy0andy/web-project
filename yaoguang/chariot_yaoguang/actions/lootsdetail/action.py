import chariot
from .schema import LootsdetailInput, LootsdetailOutput, Input, Output, Component
# Custom imports below


class Lootsdetail(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lootsdetail',
                description=Component.DESCRIPTION,
                input=LootsdetailInput(),
                output=LootsdetailOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        lootid = params.get(Input.LOOTID)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/loot/{lootid}"

        try:
            
            yaoguang.addBody("loot_id", lootid)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("status"):
                result.update({Output.STATUS: data['status']})
            if data.get("path"):
                result.update({Output.PATH: data['path']})
            if data.get("content"):
                result.update({Output.CONTENT: data['content']})
            if data.get("content_type"):
                result.update({Output.CONTENTTYPE: data['content_type']})
            if data.get("message"):
                result.update({Output.MESSAGE: data['message']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")