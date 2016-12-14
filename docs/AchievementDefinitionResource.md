# AchievementDefinitionResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this resource type | [optional] 
**created_date** | **int** | The date/time this resource was created in seconds since unix epoch | [optional] 
**description** | **str** | The description of the achievement. Must be at least 2 characters in length. | [optional] 
**hidden** | **bool** | Whether the achievement is hidden from the user | 
**max_value** | **int** | The maximum value for the achievement definition. Must be greater than or equal to min_value. | 
**min_value** | **int** | The minimum value for the achievement definition. Must be greater than zero. | 
**name** | **str** | The name of the achievement. Must be at least 6 characters in length. IMMUTABLE | 
**rule_id** | **str** | The id of the rule generated for this achievement | [optional] 
**tags** | **list[str]** | The tags for the achievement definition | [optional] 
**template** | **str** | An achievement template this achievement is validated against (private). May be null and no validation of additional_properties will be done | [optional] 
**trigger_event_name** | **str** | The name of the trigger event associated with this achievement | [optional] 
**updated_date** | **int** | The date/time this resource was last updated in seconds since unix epoch | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


