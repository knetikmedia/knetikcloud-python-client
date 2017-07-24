# knetik_cloud.UsersAddressesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address**](UsersAddressesApi.md#create_address) | **POST** /users/{user_id}/addresses | Create a new address
[**delete_address**](UsersAddressesApi.md#delete_address) | **DELETE** /users/{user_id}/addresses/{id} | Delete an address
[**get_address**](UsersAddressesApi.md#get_address) | **GET** /users/{user_id}/addresses/{id} | Get a single address
[**get_addresses**](UsersAddressesApi.md#get_addresses) | **GET** /users/{user_id}/addresses | List and search addresses
[**update_address**](UsersAddressesApi.md#update_address) | **PUT** /users/{user_id}/addresses/{id} | Update an address


# **create_address**
> SavedAddressResource create_address(user_id, saved_address_resource=saved_address_resource)

Create a new address

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
saved_address_resource = knetik_cloud.SavedAddressResource() # SavedAddressResource | The new address (optional)

try: 
    # Create a new address
    api_response = api_instance.create_address(user_id, saved_address_resource=saved_address_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->create_address: %s\n" % e)
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

# **delete_address**
> delete_address(user_id, id)

Delete an address

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
id = 56 # int | The id of the address

try: 
    # Delete an address
    api_instance.delete_address(user_id, id)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->delete_address: %s\n" % e)
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

# **get_address**
> SavedAddressResource get_address(user_id, id)

Get a single address

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
id = 56 # int | The id of the address

try: 
    # Get a single address
    api_response = api_instance.get_address(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->get_address: %s\n" % e)
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

# **get_addresses**
> PageResourceSavedAddressResource get_addresses(user_id, size=size, page=page, order=order)

List and search addresses

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search addresses
    api_response = api_instance.get_addresses(user_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->get_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceSavedAddressResource**](PageResourceSavedAddressResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> SavedAddressResource update_address(user_id, id, saved_address_resource=saved_address_resource)

Update an address

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.UsersAddressesApi()
user_id = 'user_id_example' # str | The id of the user
id = 56 # int | The id of the address
saved_address_resource = knetik_cloud.SavedAddressResource() # SavedAddressResource | The saved address resource object (optional)

try: 
    # Update an address
    api_response = api_instance.update_address(user_id, id, saved_address_resource=saved_address_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersAddressesApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id of the user | 
 **id** | **int**| The id of the address | 
 **saved_address_resource** | [**SavedAddressResource**](SavedAddressResource.md)| The saved address resource object | [optional] 

### Return type

[**SavedAddressResource**](SavedAddressResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

