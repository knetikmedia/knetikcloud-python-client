# swagger_client.StoreVendorsApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vendor_using_post**](StoreVendorsApi.md#create_vendor_using_post) | **POST** /vendors | Create a vendor
[**delete_vendor_using_delete**](StoreVendorsApi.md#delete_vendor_using_delete) | **DELETE** /vendors/{id} | Delete a vendor
[**get_vendor_using_get**](StoreVendorsApi.md#get_vendor_using_get) | **GET** /vendors/{id} | Get a single vendor
[**get_vendors_using_get**](StoreVendorsApi.md#get_vendors_using_get) | **GET** /vendors | List and search vendors
[**update_vendor_using_put**](StoreVendorsApi.md#update_vendor_using_put) | **PUT** /vendors/{id} | Update a vendor


# **create_vendor_using_post**
> VendorResource create_vendor_using_post(vendor=vendor)

Create a vendor

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreVendorsApi()
vendor = swagger_client.VendorResource() # VendorResource | The vendor (optional)

try: 
    # Create a vendor
    api_response = api_instance.create_vendor_using_post(vendor=vendor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->create_vendor_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor** | [**VendorResource**](VendorResource.md)| The vendor | [optional] 

### Return type

[**VendorResource**](VendorResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_using_delete**
> delete_vendor_using_delete(id)

Delete a vendor

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreVendorsApi()
id = 56 # int | The id of the vendor

try: 
    # Delete a vendor
    api_instance.delete_vendor_using_delete(id)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->delete_vendor_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the vendor | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_using_get**
> VendorResource get_vendor_using_get(id)

Get a single vendor

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreVendorsApi()
id = 56 # int | The id of the vendor

try: 
    # Get a single vendor
    api_response = api_instance.get_vendor_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->get_vendor_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the vendor | 

### Return type

[**VendorResource**](VendorResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendors_using_get**
> PageVendorResource get_vendors_using_get(filter_name=filter_name, size=size, page=page, order=order)

List and search vendors

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreVendorsApi()
filter_name = 'filter_name_example' # str | Filters vendors by name starting with the text provided in the filter (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List and search vendors
    api_response = api_instance.get_vendors_using_get(filter_name=filter_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->get_vendors_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| Filters vendors by name starting with the text provided in the filter | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageVendorResource**](PageVendorResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vendor_using_put**
> update_vendor_using_put(id, vendor=vendor)

Update a vendor

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreVendorsApi()
id = 56 # int | The id of the vendor
vendor = swagger_client.VendorResource() # VendorResource | The vendor (optional)

try: 
    # Update a vendor
    api_instance.update_vendor_using_put(id, vendor=vendor)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->update_vendor_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the vendor | 
 **vendor** | [**VendorResource**](VendorResource.md)| The vendor | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

