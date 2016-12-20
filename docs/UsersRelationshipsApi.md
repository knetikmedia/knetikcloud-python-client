# swagger_client.UsersRelationshipsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relationship_using_post**](UsersRelationshipsApi.md#add_relationship_using_post) | **POST** /users/relationships | Create a user relationship
[**delete_relationship_using_delete**](UsersRelationshipsApi.md#delete_relationship_using_delete) | **DELETE** /users/relationships/{id} | Delete a user relationship
[**get_relationship_using_get**](UsersRelationshipsApi.md#get_relationship_using_get) | **GET** /users/relationships/{id} | Get a user relationship
[**get_relationships_using_get**](UsersRelationshipsApi.md#get_relationships_using_get) | **GET** /users/relationships | Get a list of user relationships
[**update_relationship_using_put**](UsersRelationshipsApi.md#update_relationship_using_put) | **PUT** /users/relationships/{id} | Update a user relationship


# **add_relationship_using_post**
> UserRelationshipResource add_relationship_using_post(relationship=relationship)

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
    api_response = api_instance.add_relationship_using_post(relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->add_relationship_using_post: %s\n" % e)
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

# **delete_relationship_using_delete**
> delete_relationship_using_delete(id)

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
    api_instance.delete_relationship_using_delete(id)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->delete_relationship_using_delete: %s\n" % e)
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

# **get_relationship_using_get**
> UserRelationshipResource get_relationship_using_get(id)

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
    api_response = api_instance.get_relationship_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->get_relationship_using_get: %s\n" % e)
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

# **get_relationships_using_get**
> PageUserRelationshipResource get_relationships_using_get()

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
    api_response = api_instance.get_relationships_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->get_relationships_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PageUserRelationshipResource**](PageUserRelationshipResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_relationship_using_put**
> UserRelationshipResource update_relationship_using_put(id, relationship=relationship)

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
    api_response = api_instance.update_relationship_using_put(id, relationship=relationship)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersRelationshipsApi->update_relationship_using_put: %s\n" % e)
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

