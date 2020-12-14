import chariot
from .schema import TasksstartwebauditInput, TasksstartwebauditOutput, Input, Output, Component
# Custom imports below


class Tasksstartwebaudit(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasksstartwebaudit',
                description=Component.DESCRIPTION,
                input=TasksstartwebauditInput(),
                output=TasksstartwebauditOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)

        knowntargets = params.get(Input.KNOWNTARGETS)
        maxminutes = params.get(Input.MAXMINUTES)
        maxthreads = params.get(Input.MAXTHREADS)
        httpusername = params.get(Input.HTTPUSERNAME)
        httppassword = params.get(Input.HTTPPASSWORD)
        httpdomain = params.get(Input.HTTPDOMAIN)
        cookie = params.get(Input.COOKIE)
        useragent = params.get(Input.USERAGENT)
        sessioncookiename = params.get(Input.SESSIONCOOKIENAME)
        directobjectreference = params.get(directobjectreference)

        

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/start_webaudit"

        try:
            
            yaoguang.addBody("workspace_id", workspaceid)
            
            if knowntargets:
                yaoguang.addBody("known_targets", knowntargets)
            if maxminutes:
                yaoguang.addBody("max_minutes", maxminutes)
            if maxthreads:
                yaoguang.addBody("max_threads", maxthreads)
            if httpusername:
                yaoguang.addBody("http_username", httpusername)
            if httppassword:
                yaoguang.addBody("http_password", httppassword)
            if httpdomain:
                yaoguang.addBody("http_domain", httpdomain)
            if cookie:
                yaoguang.addBody("cookie", cookie)
            if useragent:
                yaoguang.addBody("user_agent", useragent)
            if sessioncookiename:
                yaoguang.addBody("session_cookie_name", sessioncookiename)
            if directobjectreference:
                yaoguang.addBody("direct_object_reference", directobjectreference)
            
           
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