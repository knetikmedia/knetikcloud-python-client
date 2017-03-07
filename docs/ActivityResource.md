# ActivityResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **int** | The date/time this resource was created in seconds since unix epoch | [optional] 
**entitlements** | [**list[ActivityEntitlementResource]**](ActivityEntitlementResource.md) | The list of items that can be used for entitlement (wager amounts/etc) | [optional] 
**id** | **int** | The unique ID for that resource | [optional] 
**launch** | **str** | Details about how to launch the activity | [optional] 
**long_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**name** | **str** | The user friendly name of that resource | 
**reward_set** | [**RewardSetResource**](RewardSetResource.md) | The rewards to give at the end of each occurence of the activity. When creating/updating only id is used. Reward set must be pre-existing | [optional] 
**settings** | [**list[AvailableSettingResource]**](AvailableSettingResource.md) | The list of settings and their options available for this activity. Not populated when getting listing | [optional] 
**short_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**template** | **bool** | Whether this activity is a template for other activities. Default: false | [optional] 
**type** | **str** | The type of the activity | 
**unique_key** | **str** | The unique key (for static reference in code) of the activity | [optional] 
**updated_date** | **int** | The date/time this resource was last updated in seconds since unix epoch | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


