# swagger_client.UtilMaintenanceApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_maintenance**](UtilMaintenanceApi.md#delete_maintenance) | **DELETE** /maintenance | Delete maintenance info
[**get_maintenance**](UtilMaintenanceApi.md#get_maintenance) | **GET** /maintenance | Get current maintenance info
[**update_maintenance**](UtilMaintenanceApi.md#update_maintenance) | **POST** /maintenance | Set current maintenance info
[**update_maintenance1**](UtilMaintenanceApi.md#update_maintenance1) | **PUT** /maintenance | Set current maintenance info


# **delete_maintenance**
> delete_maintenance()

Delete maintenance info

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
    # Delete maintenance info
    api_instance.delete_maintenance()
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->delete_maintenance: %s\n" % e)
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

# **get_maintenance**
> Maintenance get_maintenance()

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
    api_response = api_instance.get_maintenance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->get_maintenance: %s\n" % e)
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

# **update_maintenance**
> update_maintenance(maintenance=maintenance)

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
maintenance = swagger_client.Maintenance() # Maintenance | The maintenance object (optional)

try: 
    # Set current maintenance info
    api_instance.update_maintenance(maintenance=maintenance)
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->update_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance** | [**Maintenance**](Maintenance.md)| The maintenance object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_maintenance1**
> update_maintenance1(maintenance=maintenance)

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
maintenance = swagger_client.Maintenance() # Maintenance | The maintenance object (optional)

try: 
    # Set current maintenance info
    api_instance.update_maintenance1(maintenance=maintenance)
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->update_maintenance1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance** | [**Maintenance**](Maintenance.md)| The maintenance object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

