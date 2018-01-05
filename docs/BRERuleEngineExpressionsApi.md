# knetik_cloud.BRERuleEngineExpressionsApi

All URIs are relative to *https://devsandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bre_expression**](BRERuleEngineExpressionsApi.md#get_bre_expression) | **GET** /bre/expressions/{type} | Lookup a specific expression
[**get_bre_expressions**](BRERuleEngineExpressionsApi.md#get_bre_expressions) | **GET** /bre/expressions | Get a list of supported expressions to use in conditions or actions.
[**get_expression_as_text**](BRERuleEngineExpressionsApi.md#get_expression_as_text) | **POST** /bre/expressions | Returns the textual representation of an expression


# **get_bre_expression**
> ExpressionResource get_bre_expression(type)

Lookup a specific expression

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
api_instance = knetik_cloud.BRERuleEngineExpressionsApi(knetik_cloud.ApiClient(configuration))
type = 'type_example' # str | Specifiy the type of expression as returned by the listing endpoint

try: 
    # Lookup a specific expression
    api_response = api_instance.get_bre_expression(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineExpressionsApi->get_bre_expression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Specifiy the type of expression as returned by the listing endpoint | 

### Return type

[**ExpressionResource**](ExpressionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_expressions**
> list[ExpressionResource] get_bre_expressions(filter_type_group=filter_type_group)

Get a list of supported expressions to use in conditions or actions.

Each resource contains a type and a definition that are read-only, all the other fields must be provided when using the expression in a rule.

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
api_instance = knetik_cloud.BRERuleEngineExpressionsApi(knetik_cloud.ApiClient(configuration))
filter_type_group = 'filter_type_group_example' # str | Filter for expressions by type group (optional)

try: 
    # Get a list of supported expressions to use in conditions or actions.
    api_response = api_instance.get_bre_expressions(filter_type_group=filter_type_group)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineExpressionsApi->get_bre_expressions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_type_group** | **str**| Filter for expressions by type group | [optional] 

### Return type

[**list[ExpressionResource]**](ExpressionResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expression_as_text**
> StringWrapper get_expression_as_text(expression=expression)

Returns the textual representation of an expression

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
api_instance = knetik_cloud.BRERuleEngineExpressionsApi(knetik_cloud.ApiClient(configuration))
expression = knetik_cloud.ExpressionResource() # ExpressionResource | The expression resource to be converted (optional)

try: 
    # Returns the textual representation of an expression
    api_response = api_instance.get_expression_as_text(expression=expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineExpressionsApi->get_expression_as_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | [**ExpressionResource**](ExpressionResource.md)| The expression resource to be converted | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

