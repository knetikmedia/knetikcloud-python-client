# UserResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | [**dict(str, ModelProperty)**](ModelProperty.md) | A map of additional properties, keyed on the property name (private). Must match the names and types defined in the template for this user type, or be an extra not from the template | [optional] 
**address** | **str** | The first line of the user&#39;s address (private) | [optional] 
**address2** | **str** | The second line of user&#39;s address (private) | [optional] 
**avatar_url** | **str** | The url of the user&#39;s avatar image | [optional] 
**city** | **str** | The user&#39;s city (private) | [optional] 
**country_code** | **str** | The ISO3 code for the country from the user&#39;s address (private). Will be filled in based on GeoIP country at registration if not provided. | [optional] 
**currency_code** | **str** | The code for the user&#39;s real money currency (private) | [optional] 
**date_of_birth** | **int** | The user&#39;s date of birth (private) as a unix timestamp | [optional] 
**description** | **str** | The user&#39;s self description (private) | [optional] 
**display_name** | **str** | The chosen display name of the user, defaults to username if not present | [optional] 
**email** | **str** | The user&#39;s email address (private). May be required and/or unique depending on system configuration (both on by default). Must match standard email requirements if provided (RFC 2822) | 
**first_name** | **str** | The user&#39;s first name (private) | [optional] 
**fullname** | **str** | The user&#39;s full name (private) | [optional] 
**gender** | **str** | The user&#39;s gender (private) | [optional] 
**id** | **int** | The id of the user | [optional] 
**language_code** | **str** | The ISO3 code for the user&#39;s currency (private) | [optional] 
**last_name** | **str** | The user&#39;s last name (private) | [optional] 
**mobile_number** | **str** | The user&#39;s mobile phone number (private) | [optional] 
**password** | **str** | The plain text password for the new user account. Required for registration; ignored on profile update.  Use password specific endpoints for editing | [optional] 
**postal_code** | **str** | The user&#39;s postal code (private) | [optional] 
**state** | **str** | The user&#39;s state (private) | [optional] 
**template** | **str** | A user template this user is validated against (private). May be null and no validation of properties will be done | [optional] 
**timezone_code** | **str** | The code for the user&#39;s timezone (private) | [optional] 
**username** | **str** | The login username for the user (private). May be set to match email if system does not require usernames separately. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


