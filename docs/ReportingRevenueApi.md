# knetik_cloud.ReportingRevenueApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_revenue**](ReportingRevenueApi.md#get_item_revenue) | **GET** /reporting/revenue/item-sales/{currency_code} | Get item revenue info
[**get_refund_revenue**](ReportingRevenueApi.md#get_refund_revenue) | **GET** /reporting/revenue/refunds/{currency_code} | Get refund revenue info
[**get_revenue_by_country**](ReportingRevenueApi.md#get_revenue_by_country) | **GET** /reporting/revenue/countries/{currency_code} | Get revenue info by country
[**get_revenue_by_item**](ReportingRevenueApi.md#get_revenue_by_item) | **GET** /reporting/revenue/products/{currency_code} | Get revenue info by item
[**get_subscription_revenue**](ReportingRevenueApi.md#get_subscription_revenue) | **GET** /reporting/revenue/subscription-sales/{currency_code} | Get subscription revenue info


# **get_item_revenue**
> RevenueReportResource get_item_revenue(currency_code, start_date=start_date, end_date=end_date)

Get item revenue info

Get basic info about revenue from sales of items and bundles (not subscriptions, shipping, etc), summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN

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
api_instance = knetik_cloud.ReportingRevenueApi(knetik_cloud.ApiClient(configuration))
currency_code = 'currency_code_example' # str | The code for a currency to get sales data for
start_date = 789 # int | The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time (optional)
end_date = 789 # int | The end of the time range to aggregate, unix timestamp in seconds. Default is end of time (optional)

try: 
    # Get item revenue info
    api_response = api_instance.get_item_revenue(currency_code, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingRevenueApi->get_item_revenue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**| The code for a currency to get sales data for | 
 **start_date** | **int**| The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time | [optional] 
 **end_date** | **int**| The end of the time range to aggregate, unix timestamp in seconds. Default is end of time | [optional] 

### Return type

[**RevenueReportResource**](RevenueReportResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refund_revenue**
> RevenueReportResource get_refund_revenue(currency_code, start_date=start_date, end_date=end_date)

Get refund revenue info

Get basic info about revenue loss from refunds (for all item types), summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN

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
api_instance = knetik_cloud.ReportingRevenueApi(knetik_cloud.ApiClient(configuration))
currency_code = 'currency_code_example' # str | The code for a currency to get refund data for
start_date = 789 # int | The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time (optional)
end_date = 789 # int | The end of the time range to aggregate, unix timestamp in seconds. Default is end of time (optional)

try: 
    # Get refund revenue info
    api_response = api_instance.get_refund_revenue(currency_code, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingRevenueApi->get_refund_revenue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**| The code for a currency to get refund data for | 
 **start_date** | **int**| The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time | [optional] 
 **end_date** | **int**| The end of the time range to aggregate, unix timestamp in seconds. Default is end of time | [optional] 

### Return type

[**RevenueReportResource**](RevenueReportResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revenue_by_country**
> PageResourceRevenueCountryReportResource get_revenue_by_country(currency_code, start_date=start_date, end_date=end_date, size=size, page=page)

Get revenue info by country

Get basic info about revenue from sales of all types, summed up within a time range and split out by country. Sorted for largest revenue at the top. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN

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
api_instance = knetik_cloud.ReportingRevenueApi(knetik_cloud.ApiClient(configuration))
currency_code = 'currency_code_example' # str | The code for a currency to get sales data for
start_date = 789 # int | The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time (optional)
end_date = 789 # int | The end of the time range to aggregate, unix timestamp in seconds. Default is end of time (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Get revenue info by country
    api_response = api_instance.get_revenue_by_country(currency_code, start_date=start_date, end_date=end_date, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingRevenueApi->get_revenue_by_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**| The code for a currency to get sales data for | 
 **start_date** | **int**| The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time | [optional] 
 **end_date** | **int**| The end of the time range to aggregate, unix timestamp in seconds. Default is end of time | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceRevenueCountryReportResource**](PageResourceRevenueCountryReportResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_revenue_by_item**
> PageResourceRevenueProductReportResource get_revenue_by_item(currency_code, start_date=start_date, end_date=end_date, size=size, page=page)

Get revenue info by item

Get basic info about revenue from sales of all types, summed up within a time range and split out by specific item. Sorted for largest revenue at the top. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN

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
api_instance = knetik_cloud.ReportingRevenueApi(knetik_cloud.ApiClient(configuration))
currency_code = 'currency_code_example' # str | The code for a currency to get sales data for
start_date = 789 # int | The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time (optional)
end_date = 789 # int | The end of the time range to aggregate, unix timestamp in seconds. Default is end of time (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # Get revenue info by item
    api_response = api_instance.get_revenue_by_item(currency_code, start_date=start_date, end_date=end_date, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingRevenueApi->get_revenue_by_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**| The code for a currency to get sales data for | 
 **start_date** | **int**| The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time | [optional] 
 **end_date** | **int**| The end of the time range to aggregate, unix timestamp in seconds. Default is end of time | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceRevenueProductReportResource**](PageResourceRevenueProductReportResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_revenue**
> RevenueReportResource get_subscription_revenue(currency_code, start_date=start_date, end_date=end_date)

Get subscription revenue info

Get basic info about revenue from sales of new subscriptions as well as recurring payemnts, summed up within a time range. <br><br><b>Permissions Needed:</b> REPORTING_REVENUE_ADMIN

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
api_instance = knetik_cloud.ReportingRevenueApi(knetik_cloud.ApiClient(configuration))
currency_code = 'currency_code_example' # str | The code for a currency to get sales data for
start_date = 789 # int | The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time (optional)
end_date = 789 # int | The end of the time range to aggregate, unix timestamp in seconds. Default is end of time (optional)

try: 
    # Get subscription revenue info
    api_response = api_instance.get_subscription_revenue(currency_code, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingRevenueApi->get_subscription_revenue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**| The code for a currency to get sales data for | 
 **start_date** | **int**| The start of the time range to aggregate, unix timestamp in seconds. Default is beginning of time | [optional] 
 **end_date** | **int**| The end of the time range to aggregate, unix timestamp in seconds. Default is end of time | [optional] 

### Return type

[**RevenueReportResource**](RevenueReportResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

