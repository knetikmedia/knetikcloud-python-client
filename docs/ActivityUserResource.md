# ActivityUserResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **bool** | Whether this user is the &#39;host&#39; of the occurrence and has increased access to settings/etc (default: false) | [optional] 
**id** | **int** | The id of the activity user entry | [optional] 
**joined_date** | **int** | The date this user last joined the occurrence, unix timestamp in seconds | [optional] 
**left_date** | **int** | The date this user last left the occurrence, unix timestamp in seconds. Null if still present | [optional] 
**metric** | [**MetricResource**](MetricResource.md) | The metric for the user&#39;s results, after the game is over | [optional] 
**status** | **str** | The current status of the user in the occurrence (default: present) | [optional] 
**user** | [**SimpleUserResource**](SimpleUserResource.md) | The user | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


