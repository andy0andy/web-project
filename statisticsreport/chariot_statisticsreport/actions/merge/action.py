import chariot
from .schema import MergeInput, MergeOutput, Input, Output, Component
# Custom imports below


from ...util import utils
import time


class Merge(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='merge',
                description=Component.DESCRIPTION,
                input=MergeInput(),
                output=MergeOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        name = params.get(Input.NAME)
        reports = params.get(Input.REPORTS)
        
        if not name:
            name = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "-report"
        
        name += ".html"

        try:

            report = utils.write_temp(reports)

            result = {
                Output.CODE: 1,
                Output.MSG: "报表已生成",
                Output.REPORT: {
                    "filename": name,
                    "content": report
                }
            }
        except Exception as e:
            result = {
                Output.CODE: 0,
                Output.MSG: f"{'报表生成错误'} - {str(e)}"
            }

        return result
        







