# MetricResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_occurence_id** | **int** | The id of the activity occurence where this score/metric occurred | 
**tags** | **list[str]** | Any tags for the metric. Each unique tag will translate into a unique leaderboard. Maximum 5 tags and 50 characters each | [optional] 
**user_id** | **int** | The id of the user this metric is for. Default to caller and requires METRICS_ADMIN permission to specify another | [optional] 
**value** | **int** | The value/score of the metric | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


