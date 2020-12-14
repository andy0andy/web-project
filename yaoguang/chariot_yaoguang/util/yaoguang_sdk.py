import requests
import json
import base64
from loguru import logger


# 消除 veritywarring
from requests.packages.urllib3.exceptions import InsecureRequestWarning
 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)





def catchError(func):
    '''
        捕捉错误
    '''

    def wrapping(*args, **kwargs):
        
        try:
            data, code = func(*args, **kwargs)

            return data, code
        except Exception as e:
            logger.debug(f"{func.__name__} - {str(e)}")
    
    return wrapping






class YaoGaung(object):

    def __init__(self, host="https://127.0.0.1:110", token=None):

        self.host = host

        self.headers = {
            "token": token
        }

        self.params = {}
        self.form_data = {}
        self.files = {}



    def addParams(self, k, v):

        # 添加数据进params

        self.params.update({k: v})


    def addBody(self, k, v):
        # 添加数据进body

        self.form_data.update({k: v})
  

    def addFiles(self,file):
        '''
            添加上传文件
        '''
        
        file_data = {
            file['filename']: base64.b64decode(file['content'].encode())
        }

        self.files.update(file_data)


    def clearParamsBody(self):

        self.params.clear()
        self.form_data.clear()
        self.files.clear()


    @catchError
    def reqData(self, api, method):

        url = self.host + api

        response = requests.request(method=method, url=url, headers=self.headers, params=self.params, data=self.form_data, files=self.files, verify=False)
        
        # print(response.text)
        data = response.json()
        
        # 清空params。body
        self.clearParamsBody()

        return data, response.status_code



if __name__ == "__main__":
    
    token = "ef6e3e406c2e98beed2f6db625d35779"
    host = "https://10.1.40.110"

    api = "/rest_api/v3/loots"

    yaoguang = YaoGaung(host, token)


    # yaoguang.addBody("workspace_id", "1")
    # yaoguang.addBody("host_id", "1")


    # yaoguang.addBody("workspace", {
	# 			"boundary": "10.1.40.1-222",
	# 			"description": "This is test2",
	# 			"limit_to_network": "0",
	# 			"name": "test2",
	# 			"owner_id": "1"
	# 		})

    data = yaoguang.reqData(api, "POST")

    print(data)



