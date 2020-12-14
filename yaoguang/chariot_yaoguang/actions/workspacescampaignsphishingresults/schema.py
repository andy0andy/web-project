# GENERATED BY CHARIOT SDK - DO NOT EDIT
import chariot
import json


class Component:
    DESCRIPTION = ""


class Input:
    WORKSPACEID = "workspaceid"
    CAMPAIGNID = "campaignid"
    

class Output:
    STATUSCODE = "statuscode"
    DATA = "data"
    

class WorkspacescampaignsphishingresultsInput(chariot.Input):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"campaignid": {
			"type": "string",
			"title": "活动ID",
			"description": "",
			"order": 2
		},
		"workspaceid": {
			"type": "string",
			"title": "项目id",
			"description": "",
			"order": 1
		}
	},
	"required": [
		"workspaceid",
		"campaignid"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class WorkspacescampaignsphishingresultsOutput(chariot.Output):
    schema = json.loads("""
   {
	"type": "object",
	"title": "Variables",
	"properties": {
		"data": {
			"type": "array",
			"title": "返回数据",
			"description": "",
			"order": 2,
			"items": {
				"type": "object"
			}
		},
		"statuscode": {
			"type": "integer",
			"title": "状态码",
			"description": "",
			"order": 1
		}
	},
	"required": [
		"statuscode"
	]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
