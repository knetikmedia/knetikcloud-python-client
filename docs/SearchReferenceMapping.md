# SearchReferenceMapping

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the mapping to protect against duplicates | 
**ref_id_field** | **str** | The field within the type that contains the id from the refType | 
**ref_type** | **str** | The index type that the mapping pulls data from | 
**source_field_to_destination_field** | **dict(str, str)** | A map whose keys are the field names in the refType and values are the field name in the type | 
**type** | **str** | The index type that the mapping is for | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


