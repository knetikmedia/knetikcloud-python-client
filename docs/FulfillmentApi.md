# knetik_cloud.FulfillmentApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fulfillment_type**](FulfillmentApi.md#create_fulfillment_type) | **POST** /store/fulfillment/types | Create a fulfillment type
[**delete_fulfillment_type**](FulfillmentApi.md#delete_fulfillment_type) | **DELETE** /store/fulfillment/types/{id} | Delete a fulfillment type
[**get_fulfillment_type**](FulfillmentApi.md#get_fulfillment_type) | **GET** /store/fulfillment/types/{id} | Get a single fulfillment type
[**get_fulfillment_types**](FulfillmentApi.md#get_fulfillment_types) | **GET** /store/fulfillment/types | List and search fulfillment types
[**update_fulfillment_type**](FulfillmentApi.md#update_fulfillment_type) | **PUT** /store/fulfillment/types/{id} | Update a fulfillment type


# **create_fulfillment_type**
> FulfillmentType create_fulfillment_type(type=type)

Create a fulfillment type

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.FulfillmentApi(knetik_cloud.ApiClient(configuration))
type = knetik_cloud.FulfillmentType() # FulfillmentType | The fulfillment type (optional)

try: 
    # Create a fulfillment type
    api_response = api_instance.create_fulfillment_type(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentApi->create_fulfillment_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**FulfillmentType**](FulfillmentType.md)| The fulfillment type | [optional] 

### Return type

[**FulfillmentType**](FulfillmentType.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fulfillment_type**
> delete_fulfillment_type(id)

Delete a fulfillment type

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.FulfillmentApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id

try: 
    # Delete a fulfillment type
    api_instance.delete_fulfillment_type(id)
except ApiException as e:
    print("Exception when calling FulfillmentApi->delete_fulfillment_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_type**
> FulfillmentType get_fulfillment_type(id)

Get a single fulfillment type

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.FulfillmentApi()
id = 56 # int | The id

try: 
    # Get a single fulfillment type
    api_response = api_instance.get_fulfillment_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentApi->get_fulfillment_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id | 

### Return type

[**FulfillmentType**](FulfillmentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_types**
> PageResourceFulfillmentType get_fulfillment_types(size=size, page=page, order=order)

List and search fulfillment types

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.FulfillmentApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search fulfillment types
    api_response = api_instance.get_fulfillment_types(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FulfillmentApi->get_fulfillment_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceFulfillmentType**](PageResourceFulfillmentType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fulfillment_type**
> update_fulfillment_type(id, fulfillment_type=fulfillment_type)

Update a fulfillment type

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2_client_credentials_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2_password_grant
configuration = knetik_cloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.FulfillmentApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id
fulfillment_type = knetik_cloud.FulfillmentType() # FulfillmentType | The fulfillment type (optional)

try: 
    # Update a fulfillment type
    api_instance.update_fulfillment_type(id, fulfillment_type=fulfillment_type)
except ApiException as e:
    print("Exception when calling FulfillmentApi->update_fulfillment_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id | 
 **fulfillment_type** | [**FulfillmentType**](FulfillmentType.md)| The fulfillment type | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

