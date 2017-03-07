# swagger_client.ReportingOrdersApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_reports**](ReportingOrdersApi.md#get_invoice_reports) | **GET** /reporting/orders/count/{currency_code} | Retrieve invoice counts aggregated by time ranges


# **get_invoice_reports**
> PageResourceAggregateInvoiceReportResource get_invoice_reports(currency_code, granularity=granularity, filter_payment_status=filter_payment_status, filter_fulfillment_status=filter_fulfillment_status, start_date=start_date, end_date=end_date)

Retrieve invoice counts aggregated by time ranges

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
api_instance = swagger_client.ReportingOrdersApi()
currency_code = 'currency_code_example' # str | The code for a currency to get sales data for
granularity = 'day' # str | The time duration to aggregate by (optional) (default to day)
filter_payment_status = 'filter_payment_status_example' # str | A payment status to filter results by, can be a comma separated list (optional)
filter_fulfillment_status = 'filter_fulfillment_status_example' # str | An invoice fulfillment status to filter results by, can be a comma separated list (optional)
start_date = 789 # int | The start of the time range to return, unix timestamp in seconds. Default is beginning of time (optional)
end_date = 789 # int | The end of the time range to return, unix timestamp in seconds. Default is end of time (optional)

try: 
    # Retrieve invoice counts aggregated by time ranges
    api_response = api_instance.get_invoice_reports(currency_code, granularity=granularity, filter_payment_status=filter_payment_status, filter_fulfillment_status=filter_fulfillment_status, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingOrdersApi->get_invoice_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code** | **str**| The code for a currency to get sales data for | 
 **granularity** | **str**| The time duration to aggregate by | [optional] [default to day]
 **filter_payment_status** | **str**| A payment status to filter results by, can be a comma separated list | [optional] 
 **filter_fulfillment_status** | **str**| An invoice fulfillment status to filter results by, can be a comma separated list | [optional] 
 **start_date** | **int**| The start of the time range to return, unix timestamp in seconds. Default is beginning of time | [optional] 
 **end_date** | **int**| The end of the time range to return, unix timestamp in seconds. Default is end of time | [optional] 

### Return type

[**PageResourceAggregateInvoiceReportResource**](PageResourceAggregateInvoiceReportResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

