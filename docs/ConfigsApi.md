# swagger_client.ConfigsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_config_using_post**](ConfigsApi.md#create_config_using_post) | **POST** /configs | Create a new config
[**delete_config_using_delete**](ConfigsApi.md#delete_config_using_delete) | **DELETE** /configs/{name} | Delete an existing config.
[**get_config_using_get**](ConfigsApi.md#get_config_using_get) | **GET** /configs/{name} | Get a single config
[**get_configs_using_get**](ConfigsApi.md#get_configs_using_get) | **GET** /configs | List and search configs
[**update_config_using_put**](ConfigsApi.md#update_config_using_put) | **PUT** /configs/{name} | Update an existing config.


# **create_config_using_post**
> Config create_config_using_post(config=config)

Create a new config

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
api_instance = swagger_client.ConfigsApi()
config = swagger_client.Config() # Config | The config object (optional)

try: 
    # Create a new config
    api_response = api_instance.create_config_using_post(config=config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigsApi->create_config_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**Config**](Config.md)| The config object | [optional] 

### Return type

[**Config**](Config.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config_using_delete**
> delete_config_using_delete(name)

Delete an existing config.

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
api_instance = swagger_client.ConfigsApi()
name = 'name_example' # str | The config name

try: 
    # Delete an existing config.
    api_instance.delete_config_using_delete(name)
except ApiException as e:
    print("Exception when calling ConfigsApi->delete_config_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The config name | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_using_get**
> Config get_config_using_get(name)

Get a single config

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigsApi()
name = 'name_example' # str | The config name

try: 
    # Get a single config
    api_response = api_instance.get_config_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigsApi->get_config_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The config name | 

### Return type

[**Config**](Config.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configs_using_get**
> PageConfig get_configs_using_get(filter_search=filter_search, size=size, page=page, order=order)

List and search configs

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigsApi()
filter_search = 'filter_search_example' # str | Filter for configs whose name contains the given string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search configs
    api_response = api_instance.get_configs_using_get(filter_search=filter_search, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigsApi->get_configs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_search** | **str**| Filter for configs whose name contains the given string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageConfig**](PageConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_using_put**
> update_config_using_put(name, config=config)

Update an existing config.

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
api_instance = swagger_client.ConfigsApi()
name = 'name_example' # str | The config name
config = swagger_client.Config() # Config | The config object (optional)

try: 
    # Update an existing config.
    api_instance.update_config_using_put(name, config=config)
except ApiException as e:
    print("Exception when calling ConfigsApi->update_config_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The config name | 
 **config** | [**Config**](Config.md)| The config object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

