# swagger_client.ReportingUsageApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_by_day_using_get**](ReportingUsageApi.md#get_usage_by_day_using_get) | **GET** /reporting/usage/day | Returns aggregated endpoint usage information by the day
[**get_usage_by_hour_using_get**](ReportingUsageApi.md#get_usage_by_hour_using_get) | **GET** /reporting/usage/hour | Returns aggregated endpoint usage information by hour
[**get_usage_by_minute_using_get**](ReportingUsageApi.md#get_usage_by_minute_using_get) | **GET** /reporting/usage/minute | Returns aggregated endpoint usage information by minute
[**get_usage_by_month_using_get**](ReportingUsageApi.md#get_usage_by_month_using_get) | **GET** /reporting/usage/month | Returns aggregated endpoint usage information by month
[**get_usage_by_year_using_get**](ReportingUsageApi.md#get_usage_by_year_using_get) | **GET** /reporting/usage/year | Returns aggregated endpoint usage information by year


# **get_usage_by_day_using_get**
> PageResourceUsageInfo get_usage_by_day_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)

Returns aggregated endpoint usage information by the day

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
api_instance = swagger_client.ReportingUsageApi()
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by the day
    api_response = api_instance.get_usage_by_day_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_day_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_hour_using_get**
> PageResourceUsageInfo get_usage_by_hour_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)

Returns aggregated endpoint usage information by hour

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
api_instance = swagger_client.ReportingUsageApi()
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by hour
    api_response = api_instance.get_usage_by_hour_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_hour_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_minute_using_get**
> PageResourceUsageInfo get_usage_by_minute_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)

Returns aggregated endpoint usage information by minute

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
api_instance = swagger_client.ReportingUsageApi()
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by minute
    api_response = api_instance.get_usage_by_minute_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_minute_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_month_using_get**
> PageResourceUsageInfo get_usage_by_month_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)

Returns aggregated endpoint usage information by month

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
api_instance = swagger_client.ReportingUsageApi()
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by month
    api_response = api_instance.get_usage_by_month_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_month_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_year_using_get**
> PageResourceUsageInfo get_usage_by_year_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)

Returns aggregated endpoint usage information by year

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
api_instance = swagger_client.ReportingUsageApi()
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by year
    api_response = api_instance.get_usage_by_year_using_get(start_date, end_date, combine_endpoints=combine_endpoints, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_year_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

