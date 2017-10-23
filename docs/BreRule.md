# BreRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**list[ActionContextobject]**](ActionContextobject.md) | A list of actions to execute, and the mapping for their parameters, when the rule runs. Minimum 1 | 
**condition** | [**PredicateResource**](PredicateResource.md) | A condition expression that must be met in a given event for the rule to run. Null to always run. | [optional] 
**condition_text** | **str** | The condition as a readable string. Filled in by the system from the condition | [optional] 
**description** | **str** | The human readable description of the rule | [optional] 
**enabled** | **bool** | Whether the rule is enabled to run (in conjunction with dates). Default true | [optional] 
**end_date** | **int** | The date the rule ceases to take effect, or null if never. Unix timestamp in seconds | [optional] 
**event_name** | **str** | The event name of the trigger this rule runs for. Affects which parameters are available | 
**id** | **str** | The id of the rule for later references. If left null a random guid will be generated. Must be unique. Cannot be changed | [optional] 
**name** | **str** | The human readable name of the rule | 
**sort** | **int** | Used to sort rules to control the order they run in. Larger numbered sort values run first.  Default 500 | [optional] 
**start_date** | **int** | The date the rule begins to take effect, or null if always. Unix timestamp in seconds | [optional] 
**system_rule** | **bool** | Whether the rule is a default part of the system. System rules cannot be edited or deleted, but may be disabled | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


