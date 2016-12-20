# UserActionLog

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_description** | **str** | A description of the action taken | 
**action_name** | **str** | The name of the action taken | 
**created_date** | **int** | The date of the action, unix timestamp in seconds | [optional] 
**details** | **dict(str, str)** | A map of additional details such as the target of the action | [optional] 
**id** | **str** | The id of the log entry | [optional] 
**request_id** | **str** | The id of the api request that spawned the action, if generated internally | [optional] 
**user_id** | **int** | The id of the user that took the action, if any. Read-only if not posting with LOGS_ADMIN | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


