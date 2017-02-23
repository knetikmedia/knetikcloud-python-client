# swagger_client.UtilSecurityApi

All URIs are relative to *https://sandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_location_log**](UtilSecurityApi.md#get_user_location_log) | **GET** /security/country-log | Returns the authentication log for a user
[**get_user_token_details**](UtilSecurityApi.md#get_user_token_details) | **GET** /me | Returns the authentication token details. Use /users endpoint for detailed user&#39;s info


# **get_user_location_log**
> PageResourceLocationLogResource get_user_location_log(user_id=user_id)

Returns the authentication log for a user

A log entry is recorded everytime a user requests a new token. Standard pagination available

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
api_instance = swagger_client.UtilSecurityApi()
user_id = 56 # int | The user id (optional)

try: 
    # Returns the authentication log for a user
    api_response = api_instance.get_user_location_log(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilSecurityApi->get_user_location_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The user id | [optional] 

### Return type

[**PageResourceLocationLogResource**](PageResourceLocationLogResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_token_details**
> TokenDetailsResource get_user_token_details()

Returns the authentication token details. Use /users endpoint for detailed user's info

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
api_instance = swagger_client.UtilSecurityApi()

try: 
    # Returns the authentication token details. Use /users endpoint for detailed user's info
    api_response = api_instance.get_user_token_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilSecurityApi->get_user_token_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenDetailsResource**](TokenDetailsResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

