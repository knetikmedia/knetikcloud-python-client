# ArtistResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name.  Must match the names and types defined in the template for this item type | [optional] 
**born** | **str** | YYYY/MM/DD when this artist was born | [optional] 
**contribution_count** | **int** | The current number of contributions the artist has made | [optional] 
**contributions** | [**list[ContributionResource]**](ContributionResource.md) | The list of media this artist has contributed to as well as role(s) during contribution.  Use media endpoint to add contributions | [optional] 
**created_date** | **int** | The date/time this resource was created in seconds since unix epoch | [optional] 
**died** | **str** | YYYY/MM/DD when this artist died | [optional] 
**id** | **int** | The unique ID for that resource | [optional] 
**long_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**name** | **str** | The user friendly name of that resource | 
**priority** | **int** | The sort order priority ofr the artist.  Default 100 | [optional] 
**short_description** | **str** | The user friendly name of that resource. Defaults to blank string | [optional] 
**template** | **str** | An artist template this artist is validated against (private). May be null and no validation of additional_properties will be done | [optional] 
**updated_date** | **int** | The date/time this resource was last updated in seconds since unix epoch | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


