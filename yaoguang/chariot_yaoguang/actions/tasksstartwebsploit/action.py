import chariot
from .schema import TasksstartwebsploitInput, TasksstartwebsploitOutput, Input, Output, Component
# Custom imports below


class Tasksstartwebsploit(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasksstartwebsploit',
                description=Component.DESCRIPTION,
                input=TasksstartwebsploitInput(),
                output=TasksstartwebsploitOutput())

    def run(self, params={}):
        # TODO: Implement run function
        

        workspaceid = params.get(Input.WORKSPACEID)
        targets = params.get(Input.TARGETS)

        timeout = params.get(Input.TIMEOUT)
        limitsessions = params.get(Input.LIMITSESSIONS)
        payloadtype = params.get(Input.PAYLOADTYPE)
        connection = params.get(Input.CONNECTION)
        payloadports = params.get(Input.PAYLOADPORTS)
        payloadhosts = params.get(Input.PAYLOADHOSTS)
        httpusername = params.get(Input.HTTPUSERNAME)
        httppassword = params.get(Input.HTTPPASSWORD)
        httpdomain = params.get(Input.HTTPDOMAIN)
        cookie = params.get(Input.COOKIE)
        useragent = params.get(Input.USERAGENT)
    
        

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/start_websploit"

        try:
            
            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("targets", targets)
            
            if timeout:
                yaoguang.addBody("timeout", timeout)
            if limitsessions:
                yaoguang.addBody("limit_sessions", limitsessions)
            if payloadtype:
                yaoguang.addBody("payload_type", payloadtype)
            if connection:
                yaoguang.addBody("connection", connection)
            if payloadports:
                yaoguang.addBody("payload_ports", payload_ports)
            if payloadtype:
                yaoguang.addBody("payload_type", payloadtype)
            if payloadhosts:
                yaoguang.addBody("payload_lhost", payloadhosts)
            if httppassword:
                yaoguang.addBody("http_password", httppassword)
            if httpdomain:
                yaoguang.addBody("http_domain", httpdomain)
            if cookie:
                yaoguang.addBody("cookie", cookie)
            if useragent:
                yaoguang.addBody("user_agent", useragent)
           
            data, code = yaoguang.reqData(api, "POST")

            result = {
                Output.STATUSCODE: code
            }
            
            if data.get("success"):
                result.update({Output.SUCCESS: data['success']})
            if data.get("workspace_id"):
                result.update({Output.WORKSPACEID: data['workspace_id']})
            if data.get("task_id"):
                result.update({Output.TASKID: data['task_id']})
            if data.get("errors"):
                result.update({Output.ERRORS: data['errors']})

            return result

        except Exception as e:
            raise Exception(f"f{self.__class__.__name__} - {str(e)}")