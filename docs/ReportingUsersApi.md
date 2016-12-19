# swagger_client.ReportingUsersApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executive_revenue_item_sales_using_get1**](ReportingUsersApi.md#executive_revenue_item_sales_using_get1) | **GET** /reporting/users/registrations | Get user registration info


# **executive_revenue_item_sales_using_get1**
> PageAggregateCountResource executive_revenue_item_sales_using_get1(granularity=granularity, start_date=start_date, end_date=end_date)

Get user registration info

Get user registration counts grouped by time range

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
api_instance = swagger_client.ReportingUsersApi()
granularity = 'day' # str | The time duration to aggregate by (optional) (default to day)
start_date = 789 # int | The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time (optional)
end_date = 789 # int | The end of the time range to aggregate, unix timestamp in seconds. Default is end of time (optional)

try: 
    # Get user registration info
    api_response = api_instance.executive_revenue_item_sales_using_get1(granularity=granularity, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsersApi->executive_revenue_item_sales_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **granularity** | **str**| The time duration to aggregate by | [optional] [default to day]
 **start_date** | **int**| The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time | [optional] 
 **end_date** | **int**| The end of the time range to aggregate, unix timestamp in seconds. Default is end of time | [optional] 

### Return type

[**PageAggregateCountResource**](PageAggregateCountResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

