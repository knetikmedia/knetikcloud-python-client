# swagger_client.BRERuleEngineExpressionsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bre_expressions**](BRERuleEngineExpressionsApi.md#get_bre_expressions) | **GET** /bre/expressions/lookup | Get a list of &#39;lookup&#39; type expressions


# **get_bre_expressions**
> list[LookupTypeResource] get_bre_expressions()

Get a list of 'lookup' type expressions

These are expression types that take a second expression as input and produce a value. These can be used in addition to the standard types, like parameter, global and constant (see BRE documentation for details).

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
api_instance = swagger_client.BRERuleEngineExpressionsApi()

try: 
    # Get a list of 'lookup' type expressions
    api_response = api_instance.get_bre_expressions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineExpressionsApi->get_bre_expressions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LookupTypeResource]**](LookupTypeResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

