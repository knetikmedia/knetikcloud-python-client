# CategoryResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the category is currently active. If not, it and its questions will be filtered out. | [optional] 
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type | [optional] 
**id** | **str** | The unique ID for this category | [optional] 
**name** | **str** | The name of this category. Cannot be blank | 
**template** | **str** | A category template this category is validated against (private). May be null and no validation of additional_properties will be done | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


