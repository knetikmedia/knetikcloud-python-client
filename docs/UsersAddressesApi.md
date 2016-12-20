# swagger_client.UsersAddressesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address_using_post**](UsersAddressesApi.md#create_address_using_post) | **POST** /users/{user_id}/addresses | Save a new address
[**delete_address_using_delete**](UsersAddressesApi.md#delete_address_using_delete) | **DELETE** /users/{user_id}/addresses/{id} | Delete an address
[**get_address_using_get**](UsersAddressesApi.md#get_address_using_get) | **GET** /users/{user_id}/addresses/{id} | Get a single address
[**get_addresses_using_get**](UsersAddressesApi.md#get_addresses_using_get) | **GET** /users/{user_id}/addresses | List and search addresses
[**update_address_using_put**](UsersAddressesApi.md#update_address_using_put) | **PUT** /users/{user_id}/addresses/{id} | Update an address


# **create_address_using_post**
> SavedAddressResource create_address_using_post(user_id, saved_address_resource=saved_address_resource)

Save a new address

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
api_instance = swagger_client.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
saved_address_resource = swagger_client.SavedAddressResource() # SavedAddressResource | The new address (optional)

try: 
    # Save a new address
    api_response = api_instance.create_address_using_post(user_id, saved_address_resource=saved_address_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->create_address_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 
 **saved_address_resource** | [**SavedAddressResource**](SavedAddressResource.md)| The new address | [optional] 

### Return type

[**SavedAddressResource**](SavedAddressResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_address_using_delete**
> delete_address_using_delete(user_id, id)

Delete an address

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
api_instance = swagger_client.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
id = 56 # int | The id of the address

try: 
    # Delete an address
    api_instance.delete_address_using_delete(user_id, id)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->delete_address_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 
 **id** | **int**| The id of the address | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_address_using_get**
> SavedAddressResource get_address_using_get(user_id, id)

Get a single address

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
api_instance = swagger_client.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
id = 56 # int | The id of the address

try: 
    # Get a single address
    api_response = api_instance.get_address_using_get(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->get_address_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 
 **id** | **int**| The id of the address | 

### Return type

[**SavedAddressResource**](SavedAddressResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addresses_using_get**
> PageSavedAddressResource get_addresses_using_get(user_id, size=size, page=page, order=order)

List and search addresses

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
api_instance = swagger_client.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search addresses
    api_response = api_instance.get_addresses_using_get(user_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->get_addresses_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageSavedAddressResource**](PageSavedAddressResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address_using_put**
> update_address_using_put(user_id, id, saved_address_resource=saved_address_resource)

Update an address

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
api_instance = swagger_client.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
id = 56 # int | The id of the address
saved_address_resource = swagger_client.SavedAddressResource() # SavedAddressResource | The saved address resource object (optional)

try: 
    # Update an address
    api_instance.update_address_using_put(user_id, id, saved_address_resource=saved_address_resource)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->update_address_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 
 **id** | **int**| The id of the address | 
 **saved_address_resource** | [**SavedAddressResource**](SavedAddressResource.md)| The saved address resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

