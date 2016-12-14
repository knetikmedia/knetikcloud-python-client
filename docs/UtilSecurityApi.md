# swagger_client.UtilSecurityApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_location_log_using_get**](UtilSecurityApi.md#get_user_location_log_using_get) | **GET** /security/country-log | Returns the authentication log for a user
[**user_using_get**](UtilSecurityApi.md#user_using_get) | **GET** /me | Returns the authentication token details. Use /users endpoint for detailed user&#39;s info


# **get_user_location_log_using_get**
> PageLocationLogResource get_user_location_log_using_get(user_id=user_id)

Returns the authentication log for a user

A log entry is recorded everytime a user requests a new token. Standard pagination available

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilSecurityApi()
user_id = 56 # int | The user id (optional)

try: 
    # Returns the authentication log for a user
    api_response = api_instance.get_user_location_log_using_get(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilSecurityApi->get_user_location_log_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user id | [optional] 

### Return type

[**PageLocationLogResource**](PageLocationLogResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_using_get**
> TokenDetailsResource user_using_get(authentication=authentication)

Returns the authentication token details. Use /users endpoint for detailed user's info

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilSecurityApi()
authentication = swagger_client.Authentication() # Authentication | The Authentication Object (optional)

try: 
    # Returns the authentication token details. Use /users endpoint for detailed user's info
    api_response = api_instance.user_using_get(authentication=authentication)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilSecurityApi->user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication** | [**Authentication**](Authentication.md)| The Authentication Object | [optional] 

### Return type

[**TokenDetailsResource**](TokenDetailsResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

