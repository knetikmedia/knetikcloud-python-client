# ClientResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_validity_seconds** | **int** | The expiration time of an initial oauth token in seconds | [optional] 
**client_key** | **str** | The client_id field of the oauth token request | 
**grant_types** | **list[str]** | The oauth grant type as in: password (username/password auth), client_credentials (server-to-server, private clients), refresh_token (to allow clients to refresh their initial token), facebook, google, etc) See documentation for a complete list. Use dedicated endpoint PUT /grant-types to edit this list | [optional] 
**id** | **int** | Generated unique ID for the client | [optional] 
**is_public** | **bool** | Set to true if the client is public i.e the secret key can be secured | [optional] 
**locked** | **bool** | Used to flag system clients that are not meant to be tinkered with | [optional] 
**name** | **str** | The friendly name of the client | 
**redirect_uris** | **list[str]** | A redirection URL to use when granting access to third-parties (seldomly used) | [optional] 
**refresh_token_validity_seconds** | **int** | The expiration time of a refresh oauth token in seconds | [optional] 
**secret** | **str** | The client-secret field of the oauth request when creating a private client | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


