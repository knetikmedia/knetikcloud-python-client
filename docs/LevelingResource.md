# LevelingResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type | [optional] 
**created_date** | **int** | The date the leveling schema was created | [optional] 
**description** | **str** | The description of the leveling schema | [optional] 
**name** | **str** | The name of the leveling schema.  IMMUTABLE | 
**tiers** | [**list[TierResource]**](TierResource.md) | A set of tiers that contain experience boundaries | [optional] 
**trigger_event_name** | **str** | The name of an event that will add one progress to this level when fired | [optional] 
**updated_date** | **int** | The date the leveling schema was updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


