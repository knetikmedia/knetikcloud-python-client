# swagger_client.UtilMaintenanceApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_using_delete1**](UtilMaintenanceApi.md#delete_using_delete1) | **DELETE** /maintenance | Remove maintenance info
[**get_using_get1**](UtilMaintenanceApi.md#get_using_get1) | **GET** /maintenance | Get current maintenance info
[**post_using_post**](UtilMaintenanceApi.md#post_using_post) | **POST** /maintenance | Set current maintenance info
[**post_using_put**](UtilMaintenanceApi.md#post_using_put) | **PUT** /maintenance | Set current maintenance info


# **delete_using_delete1**
> delete_using_delete1()

Remove maintenance info

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
api_instance = swagger_client.UtilMaintenanceApi()

try: 
    # Remove maintenance info
    api_instance.delete_using_delete1()
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->delete_using_delete1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get1**
> Maintenance get_using_get1()

Get current maintenance info

Get current maintenance info. 404 if no maintenance.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilMaintenanceApi()

try: 
    # Get current maintenance info
    api_response = api_instance.get_using_get1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->get_using_get1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Maintenance**](Maintenance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_using_post**
> post_using_post(maintenance=maintenance)

Set current maintenance info

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
api_instance = swagger_client.UtilMaintenanceApi()
maintenance = swagger_client.Maintenance() # Maintenance | The Maintenance Object (optional)

try: 
    # Set current maintenance info
    api_instance.post_using_post(maintenance=maintenance)
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->post_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance** | [**Maintenance**](Maintenance.md)| The Maintenance Object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_using_put**
> post_using_put(maintenance=maintenance)

Set current maintenance info

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
api_instance = swagger_client.UtilMaintenanceApi()
maintenance = swagger_client.Maintenance() # Maintenance | The Maintenance Object (optional)

try: 
    # Set current maintenance info
    api_instance.post_using_put(maintenance=maintenance)
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->post_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance** | [**Maintenance**](Maintenance.md)| The Maintenance Object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

