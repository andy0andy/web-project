import chariot
from .schema import TasksstartwebscanInput, TasksstartwebscanOutput, Input, Output, Component
# Custom imports below


class Tasksstartwebscan(chariot.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='tasksstartwebscan',
                description=Component.DESCRIPTION,
                input=TasksstartwebscanInput(),
                output=TasksstartwebscanOutput())

    def run(self, params={}):
        # TODO: Implement run function
        
        workspaceid = params.get(Input.WORKSPACEID)
        urls = params.get(Input.URLS)

        knowntargets = params.get(Input.KNOWNTARGETS)
        maxpages = params.get(Input.MAXPAGES)
        maxminutes = params.get(Input.MAXMINUTES)
        maxthreads = params.get(Input.MAXTHREADS)
        unauthorizedaccessforbiddenphrases = params.get(Input.UNAUTHORIZEDACCESSFORBIDDENPHRASES)
        sslreuired = params.get(Input.SSLREUIRED)
        reportweak = params.get(Input.REPORTWEAK)
        excludepathpatterns = params.get(Input.EXCLUDEPATHPATTERNS)
        httpusername = params.get(Input.HTTPUSERNAME)
        httppassword = params.get(Input.HTTPPASSWORD)
        httpdomain = params.get(Input.HTTPDOMAIN)
        cookie = params.get(Input.COOKIE)
        useragent = params.get(Input.USERAGENT)

        

        yaoguang = self.connection.yaoguang

        api = "/rest_api/v3/tasks/start_webscan"

        try:
            
            yaoguang.addBody("workspace_id", workspaceid)
            yaoguang.addBody("urls", urls)

            if knowntargets:
                yaoguang.addBody("known_targets", knowntargets)
            if maxpages:
                yaoguang.addBody("max_pages", maxpages)
            if maxminutes:
                yaoguang.addBody("max_minutes", maxminutes)
            if maxthreads:
                yaoguang.addBody("max_threads", maxthreads)
            if unauthorizedaccessforbiddenphrases:
                yaoguang.addBody("unauthorized_access_url_patterns", unauthorizedaccessforbiddenphrases)
            if sslreuired:
                yaoguang.addBody("ssl_required", sslreuired)
            if reportweak:
                yaoguang.addBody("report_weak", reportweak)
            if excludepathpatterns:
                yaoguang.addBody("exclude_path_patterns", excludepathpatterns)
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