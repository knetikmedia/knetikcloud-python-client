# swagger_client.ReportingSubscriptionsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_billing_reports_using_get**](ReportingSubscriptionsApi.md#list_billing_reports_using_get) | **GET** /reporting/subscription | Get a list of available subscription reports in most recent first order


# **list_billing_reports_using_get**
> PageResourceBillingReport list_billing_reports_using_get(size=size, page=page)

Get a list of available subscription reports in most recent first order

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
api_instance = swagger_client.ReportingSubscriptionsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Get a list of available subscription reports in most recent first order
    api_response = api_instance.list_billing_reports_using_get(size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingSubscriptionsApi->list_billing_reports_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceBillingReport**](PageResourceBillingReport.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

