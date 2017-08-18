# knetik_cloud.ReportingUsageApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_usage_by_day**](ReportingUsageApi.md#get_usage_by_day) | **GET** /reporting/usage/day | Returns aggregated endpoint usage information by day
[**get_usage_by_hour**](ReportingUsageApi.md#get_usage_by_hour) | **GET** /reporting/usage/hour | Returns aggregated endpoint usage information by hour
[**get_usage_by_minute**](ReportingUsageApi.md#get_usage_by_minute) | **GET** /reporting/usage/minute | Returns aggregated endpoint usage information by minute
[**get_usage_by_month**](ReportingUsageApi.md#get_usage_by_month) | **GET** /reporting/usage/month | Returns aggregated endpoint usage information by month
[**get_usage_by_year**](ReportingUsageApi.md#get_usage_by_year) | **GET** /reporting/usage/year | Returns aggregated endpoint usage information by year
[**get_usage_endpoints**](ReportingUsageApi.md#get_usage_endpoints) | **GET** /reporting/usage/endpoints | Returns list of endpoints called (method and url)


# **get_usage_by_day**
> PageResourceUsageInfo get_usage_by_day(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)

Returns aggregated endpoint usage information by day

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
api_instance = knetik_cloud.ReportingUsageApi(knetik_cloud.ApiClient(configuration))
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
method = 'method_example' # str | Filter for a certain endpoint method.  Must include url as well to work (optional)
url = 'url_example' # str | Filter for a certain endpoint.  Must include method as well to work (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by day
    api_response = api_instance.get_usage_by_day(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **method** | **str**| Filter for a certain endpoint method.  Must include url as well to work | [optional] 
 **url** | **str**| Filter for a certain endpoint.  Must include method as well to work | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_hour**
> PageResourceUsageInfo get_usage_by_hour(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)

Returns aggregated endpoint usage information by hour

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
api_instance = knetik_cloud.ReportingUsageApi(knetik_cloud.ApiClient(configuration))
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
method = 'method_example' # str | Filter for a certain endpoint method.  Must include url as well to work (optional)
url = 'url_example' # str | Filter for a certain endpoint.  Must include method as well to work (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by hour
    api_response = api_instance.get_usage_by_hour(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_hour: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **method** | **str**| Filter for a certain endpoint method.  Must include url as well to work | [optional] 
 **url** | **str**| Filter for a certain endpoint.  Must include method as well to work | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_minute**
> PageResourceUsageInfo get_usage_by_minute(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)

Returns aggregated endpoint usage information by minute

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
api_instance = knetik_cloud.ReportingUsageApi(knetik_cloud.ApiClient(configuration))
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
method = 'method_example' # str | Filter for a certain endpoint method.  Must include url as well to work (optional)
url = 'url_example' # str | Filter for a certain endpoint.  Must include method as well to work (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by minute
    api_response = api_instance.get_usage_by_minute(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_minute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **method** | **str**| Filter for a certain endpoint method.  Must include url as well to work | [optional] 
 **url** | **str**| Filter for a certain endpoint.  Must include method as well to work | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_month**
> PageResourceUsageInfo get_usage_by_month(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)

Returns aggregated endpoint usage information by month

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
api_instance = knetik_cloud.ReportingUsageApi(knetik_cloud.ApiClient(configuration))
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoint. Removes the url and method from the result object (optional) (default to false)
method = 'method_example' # str | Filter for a certain endpoint method.  Must include url as well to work (optional)
url = 'url_example' # str | Filter for a certain endpoint.  Must include method as well to work (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by month
    api_response = api_instance.get_usage_by_month(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_month: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoint. Removes the url and method from the result object | [optional] [default to false]
 **method** | **str**| Filter for a certain endpoint method.  Must include url as well to work | [optional] 
 **url** | **str**| Filter for a certain endpoint.  Must include method as well to work | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_by_year**
> PageResourceUsageInfo get_usage_by_year(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)

Returns aggregated endpoint usage information by year

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
api_instance = knetik_cloud.ReportingUsageApi(knetik_cloud.ApiClient(configuration))
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds
combine_endpoints = false # bool | Whether to combine counts from different endpoints. Removes the url and method from the result object (optional) (default to false)
method = 'method_example' # str | Filter for a certain endpoint method.  Must include url as well to work (optional)
url = 'url_example' # str | Filter for a certain endpoint.  Must include method as well to work (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Returns aggregated endpoint usage information by year
    api_response = api_instance.get_usage_by_year(start_date, end_date, combine_endpoints=combine_endpoints, method=method, url=url, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_by_year: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 
 **combine_endpoints** | **bool**| Whether to combine counts from different endpoints. Removes the url and method from the result object | [optional] [default to false]
 **method** | **str**| Filter for a certain endpoint method.  Must include url as well to work | [optional] 
 **url** | **str**| Filter for a certain endpoint.  Must include method as well to work | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceUsageInfo**](PageResourceUsageInfo.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage_endpoints**
> list[str] get_usage_endpoints(start_date, end_date)

Returns list of endpoints called (method and url)

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
api_instance = knetik_cloud.ReportingUsageApi(knetik_cloud.ApiClient(configuration))
start_date = 789 # int | The beginning of the range being requested, unix timestamp in seconds
end_date = 789 # int | The ending of the range being requested, unix timestamp in seconds

try: 
    # Returns list of endpoints called (method and url)
    api_response = api_instance.get_usage_endpoints(start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingUsageApi->get_usage_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| The beginning of the range being requested, unix timestamp in seconds | 
 **end_date** | **int**| The ending of the range being requested, unix timestamp in seconds | 

### Return type

**list[str]**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

