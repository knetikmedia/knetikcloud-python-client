# swagger_client.UsersRelationshipsApi

All URIs are relative to *https://sandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_relationship**](UsersRelationshipsApi.md#create_user_relationship) | **POST** /users/relationships | Create a user relationship
[**delete_user_relationship**](UsersRelationshipsApi.md#delete_user_relationship) | **DELETE** /users/relationships/{id} | Delete a user relationship
[**get_user_relationship**](UsersRelationshipsApi.md#get_user_relationship) | **GET** /users/relationships/{id} | Get a user relationship
[**get_user_relationships**](UsersRelationshipsApi.md#get_user_relationships) | **GET** /users/relationships | Get a list of user relationships
[**update_user_relationship**](UsersRelationshipsApi.md#update_user_relationship) | **PUT** /users/relationships/{id} | Update a user relationship


# **create_user_relationship**
> UserRelationshipResource create_user_relationship(relationship=relationship)

Create a user relationship

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersRelationshipsApi()
relationship = swagger_client.UserRelationshipResource() # UserRelationshipResource | The new relationship (optional)

try: 
    # Create a user relationship
    api_response = api_instance.create_user_relationship(relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->create_user_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relationship** | [**UserRelationshipResource**](UserRelationshipResource.md)| The new relationship | [optional] 

### Return type

[**UserRelationshipResource**](UserRelationshipResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_relationship**
> delete_user_relationship(id)

Delete a user relationship

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersRelationshipsApi()
id = 789 # int | The id of the relationship

try: 
    # Delete a user relationship
    api_instance.delete_user_relationship(id)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->delete_user_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the relationship | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_relationship**
> UserRelationshipResource get_user_relationship(id)

Get a user relationship

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersRelationshipsApi()
id = 789 # int | The id of the relationship

try: 
    # Get a user relationship
    api_response = api_instance.get_user_relationship(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->get_user_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the relationship | 

### Return type

[**UserRelationshipResource**](UserRelationshipResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_relationships**
> PageResourceUserRelationshipResource get_user_relationships()

Get a list of user relationships

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersRelationshipsApi()

try: 
    # Get a list of user relationships
    api_response = api_instance.get_user_relationships()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->get_user_relationships: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PageResourceUserRelationshipResource**](PageResourceUserRelationshipResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_relationship**
> UserRelationshipResource update_user_relationship(id, relationship=relationship)

Update a user relationship

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersRelationshipsApi()
id = 789 # int | The id of the relationship
relationship = swagger_client.UserRelationshipResource() # UserRelationshipResource | The new relationship (optional)

try: 
    # Update a user relationship
    api_response = api_instance.update_user_relationship(id, relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->update_user_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the relationship | 
 **relationship** | [**UserRelationshipResource**](UserRelationshipResource.md)| The new relationship | [optional] 

### Return type

[**UserRelationshipResource**](UserRelationshipResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

