# ActivityResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties keyed on the property name. Used to further describe an activity. While settings will vary from one activity occurrence (a game) to another, additional properties are shared by all the occurrences of this activity. Ex: Activity Logo, Disclaimer, Greeting, etc. Validated against template if one exists for activities | [optional] 
**core_settings** | [**CoreActivitySettings**](CoreActivitySettings.md) | Defines core settings about the activity that affect how it can be created/played by users. | [optional] 
**created_date** | **int** | The date/time this resource was created in seconds since unix epoch | [optional] 
**entitlements** | [**list[ActivityEntitlementResource]**](ActivityEntitlementResource.md) | The list of items that can be used for entitlement (wager amounts/etc) | [optional] 
**id** | **int** | The unique ID for that resource | [optional] 
**launch** | **str** | Details about how to launch the activity | [optional] 
**leaderboard_strategy** | **str** | The strategy for calculating the leaderboard. No strategy means no leaderboard for the top level context. Value MUST come from the list of available strategies from the Leaderboard Service | [optional] 
**long_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**name** | **str** | The user friendly name of that resource | 
**reward_set** | [**RewardSetResource**](RewardSetResource.md) | The rewards to give at the end of each occurence of the activity. When creating/updating only id is used. Reward set must be pre-existing | [optional] 
**settings** | [**list[AvailableSettingResource]**](AvailableSettingResource.md) | Define what parameters are required/available to start and run an activity. For example: Difficulty, Number of Questions, Character name, Avatar, Duration, etc. Not populated when getting listing | [optional] 
**short_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**template** | **bool** | Whether this activity is a template for other activities. Default: false | [optional] 
**template_id** | **str** | An activity template this activity is validated against (private). May be null and no validation of additional_properties will be done | [optional] 
**type** | **str** | The type of the activity | [optional] 
**unique_key** | **str** | The unique key (for static reference in code) of the activity | [optional] 
**updated_date** | **int** | The date/time this resource was last updated in seconds since unix epoch | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


