# knetik_cloud.UtilMaintenanceApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_maintenance**](UtilMaintenanceApi.md#delete_maintenance) | **DELETE** /maintenance | Delete maintenance info
[**get_maintenance**](UtilMaintenanceApi.md#get_maintenance) | **GET** /maintenance | Get current maintenance info
[**set_maintenance**](UtilMaintenanceApi.md#set_maintenance) | **POST** /maintenance | Set current maintenance info
[**update_maintenance**](UtilMaintenanceApi.md#update_maintenance) | **PUT** /maintenance | Update current maintenance info


# **delete_maintenance**
> delete_maintenance()

Delete maintenance info

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UtilMaintenanceApi()

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

No authorization required

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
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UtilMaintenanceApi()

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

# **set_maintenance**
> set_maintenance(maintenance=maintenance)

Set current maintenance info

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UtilMaintenanceApi()
maintenance = knetik_cloud.Maintenance() # Maintenance | The maintenance object (optional)

try: 
    # Set current maintenance info
    api_instance.set_maintenance(maintenance=maintenance)
except ApiException as e:
    print("Exception when calling UtilMaintenanceApi->set_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance** | [**Maintenance**](Maintenance.md)| The maintenance object | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_maintenance**
> update_maintenance(maintenance=maintenance)

Update current maintenance info

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.UtilMaintenanceApi()
maintenance = knetik_cloud.Maintenance() # Maintenance | The maintenance object (optional)

try: 
    # Update current maintenance info
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

