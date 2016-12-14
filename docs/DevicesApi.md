# swagger_client.DevicesApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_using_post**](DevicesApi.md#create_device_using_post) | **POST** /devices | Create a device
[**delete_device_using_delete**](DevicesApi.md#delete_device_using_delete) | **DELETE** /devices/{id} | Delete a device
[**get_device_using_get**](DevicesApi.md#get_device_using_get) | **GET** /devices/{id} | Get a single device
[**get_devices_using_get**](DevicesApi.md#get_devices_using_get) | **GET** /devices | List and search devices
[**update_device_using_put**](DevicesApi.md#update_device_using_put) | **PUT** /devices/{id} | Update a device


# **create_device_using_post**
> DeviceResource create_device_using_post(device)

Create a device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device = swagger_client.DeviceResource() # DeviceResource | device

try: 
    # Create a device
    api_response = api_instance.create_device_using_post(device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DeviceResource**](DeviceResource.md)| device | 

### Return type

[**DeviceResource**](DeviceResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_using_delete**
> delete_device_using_delete(id)

Delete a device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 56 # int | id

try: 
    # Delete a device
    api_instance.delete_device_using_delete(id)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_using_get**
> DeviceResource get_device_using_get(id)

Get a single device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
id = 56 # int | id

try: 
    # Get a single device
    api_response = api_instance.get_device_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**DeviceResource**](DeviceResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_using_get**
> PageDeviceResource get_devices_using_get(filter_make=filter_make, filter_model=filter_model, size=size, page=page, order=order)

List and search devices

Get a list of devices with optional filtering

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
filter_make = 'filter_make_example' # str | Filter for devices with specified make (optional)
filter_model = 'filter_model_example' # str | Filter for devices with specified model (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List and search devices
    api_response = api_instance.get_devices_using_get(filter_make=filter_make, filter_model=filter_model, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_make** | **str**| Filter for devices with specified make | [optional] 
 **filter_model** | **str**| Filter for devices with specified model | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageDeviceResource**](PageDeviceResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_using_put**
> update_device_using_put(device, id)

Update a device

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DevicesApi()
device = swagger_client.DeviceResource() # DeviceResource | device
id = 56 # int | id

try: 
    # Update a device
    api_instance.update_device_using_put(device, id)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**DeviceResource**](DeviceResource.md)| device | 
 **id** | **int**| id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

