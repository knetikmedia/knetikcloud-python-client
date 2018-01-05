# knetik_cloud.TemplatesPropertiesApi

All URIs are relative to *https://devsandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_template_property_type**](TemplatesPropertiesApi.md#get_template_property_type) | **GET** /templates/properties/{type} | Get details for a template property type
[**get_template_property_types**](TemplatesPropertiesApi.md#get_template_property_types) | **GET** /templates/properties | List template property types


# **get_template_property_type**
> PropertyFieldListResource get_template_property_type(type)

Get details for a template property type

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
api_instance = knetik_cloud.TemplatesPropertiesApi(knetik_cloud.ApiClient(configuration))
type = 'type_example' # str | type

try: 
    # Get details for a template property type
    api_response = api_instance.get_template_property_type(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesPropertiesApi->get_template_property_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| type | 

### Return type

[**PropertyFieldListResource**](PropertyFieldListResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_property_types**
> list[PropertyFieldListResource] get_template_property_types()

List template property types

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
api_instance = knetik_cloud.TemplatesPropertiesApi(knetik_cloud.ApiClient(configuration))

try: 
    # List template property types
    api_response = api_instance.get_template_property_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesPropertiesApi->get_template_property_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PropertyFieldListResource]**](PropertyFieldListResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

