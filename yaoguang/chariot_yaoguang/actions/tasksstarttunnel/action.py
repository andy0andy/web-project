import chariot
from .schema import TasksstarttunnelInput, TasksstarttunnelOutput, Input, Output, Component
# Custom imports below


class Tasksstarttunnel(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasksstarttunnel',
                description=Component.DESCRIPTION,
                input=TasksstarttunnelInput(),
                output=TasksstarttunnelOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        tunnelsession = params.get(Input.TUNNELSESSION)
        tunnelinterface = params.get(Input.TUNNELINTERFACE)
        tunneldhcp = params.get(Input.TUNNELDHCP)
        tunneladdress = params.get(Input.TUNNELADDRESS)
        tunnelnetmask = params.get(Input.TUNNELNETMASK)

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/start_tunnel"

        try:

            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("tunnel_session", tunnelsession)
            yaoguang.addBody("tunnel_interface", tunnelinterface)
            yaoguang.addBody("tunnel_dhcp", tunneldhcp)
            yaoguang.addBody("tunnel_address", tunneladdress)
            yaoguang.addBody("tunnel_netmask", tunnelnetmask)

            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("succsess"):
                result.update({Output.SUCCESS: data['success']})
            if data.get("workspace_id"):
                result.update({Output.WORKSPACEID: data['workspace']})
            if data.get("task_id"):
                result.update({Output.TASKID: data["task_id"]})


            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")