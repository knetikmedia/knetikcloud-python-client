# swagger_client.AuthClientsApi

All URIs are relative to *https://integration.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_client_grant_types_using_put**](AuthClientsApi.md#assign_client_grant_types_using_put) | **PUT** /auth/clients/{client_key}/grant-types | Set grant types for a client
[**assign_client_redirect_uris_using_put**](AuthClientsApi.md#assign_client_redirect_uris_using_put) | **PUT** /auth/clients/{client_key}/redirect-uris | Set redirect uris for a client
[**create_client_using_post**](AuthClientsApi.md#create_client_using_post) | **POST** /auth/clients | Create a new client
[**delete_client_using_delete**](AuthClientsApi.md#delete_client_using_delete) | **DELETE** /auth/clients/{client_key} | Delete a client
[**get_client_using_get**](AuthClientsApi.md#get_client_using_get) | **GET** /auth/clients/{client_key} | Get a single client
[**get_clients_using_get**](AuthClientsApi.md#get_clients_using_get) | **GET** /auth/clients | List and search clients
[**list_available_grant_types_using_get**](AuthClientsApi.md#list_available_grant_types_using_get) | **GET** /auth/clients/grant-types | List available client grant types
[**update_client_using_put**](AuthClientsApi.md#update_client_using_put) | **PUT** /auth/clients/{client_key} | Update a client


# **assign_client_grant_types_using_put**
> assign_client_grant_types_using_put(client_key, grant_list=grant_list)

Set grant types for a client

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthClientsApi()
client_key = 'client_key_example' # str | The key of the client
grant_list = [swagger_client.list[str]()] # list[str] | A list of unique grant types (optional)

try: 
    # Set grant types for a client
    api_instance.assign_client_grant_types_using_put(client_key, grant_list=grant_list)
except ApiException as e:
    print("Exception when calling AuthClientsApi->assign_client_grant_types_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| The key of the client | 
 **grant_list** | **list[str]**| A list of unique grant types | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_client_redirect_uris_using_put**
> assign_client_redirect_uris_using_put(client_key, redirect_list=redirect_list)

Set redirect uris for a client

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthClientsApi()
client_key = 'client_key_example' # str | The key of the client
redirect_list = [swagger_client.list[str]()] # list[str] | A list of unique redirect uris (optional)

try: 
    # Set redirect uris for a client
    api_instance.assign_client_redirect_uris_using_put(client_key, redirect_list=redirect_list)
except ApiException as e:
    print("Exception when calling AuthClientsApi->assign_client_redirect_uris_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| The key of the client | 
 **redirect_list** | **list[str]**| A list of unique redirect uris | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client_using_post**
> ClientResource create_client_using_post(client_resource=client_resource)

Create a new client

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthClientsApi()
client_resource = swagger_client.ClientResource() # ClientResource | The client resource object (optional)

try: 
    # Create a new client
    api_response = api_instance.create_client_using_post(client_resource=client_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthClientsApi->create_client_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_resource** | [**ClientResource**](ClientResource.md)| The client resource object | [optional] 

### Return type

[**ClientResource**](ClientResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_using_delete**
> delete_client_using_delete(client_key)

Delete a client

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthClientsApi()
client_key = 'client_key_example' # str | The key of the client

try: 
    # Delete a client
    api_instance.delete_client_using_delete(client_key)
except ApiException as e:
    print("Exception when calling AuthClientsApi->delete_client_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| The key of the client | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_using_get**
> ClientResource get_client_using_get(client_key)

Get a single client

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthClientsApi()
client_key = 'client_key_example' # str | The key of the client

try: 
    # Get a single client
    api_response = api_instance.get_client_using_get(client_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthClientsApi->get_client_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| The key of the client | 

### Return type

[**ClientResource**](ClientResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients_using_get**
> PageResourceClientResource get_clients_using_get(size=size, page=page, order=order)

List and search clients

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthClientsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search clients
    api_response = api_instance.get_clients_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthClientsApi->get_clients_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceClientResource**](PageResourceClientResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_grant_types_using_get**
> list[GrantTypeResource] list_available_grant_types_using_get()

List available client grant types

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthClientsApi()

try: 
    # List available client grant types
    api_response = api_instance.list_available_grant_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthClientsApi->list_available_grant_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GrantTypeResource]**](GrantTypeResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_using_put**
> update_client_using_put(client_key, client_resource=client_resource)

Update a client

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: knetik_oauth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthClientsApi()
client_key = 'client_key_example' # str | The key of the client
client_resource = swagger_client.ClientResource() # ClientResource | The client resource object (optional)

try: 
    # Update a client
    api_instance.update_client_using_put(client_key, client_resource=client_resource)
except ApiException as e:
    print("Exception when calling AuthClientsApi->update_client_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_key** | **str**| The key of the client | 
 **client_resource** | [**ClientResource**](ClientResource.md)| The client resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

