# swagger_client.PaymentsTransactionsApi

All URIs are relative to *https://devsandbox.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction_using_get**](PaymentsTransactionsApi.md#get_transaction_using_get) | **GET** /transactions/{id} | Get the details for a single transaction
[**get_transactions_using_get**](PaymentsTransactionsApi.md#get_transactions_using_get) | **GET** /transactions | List and search transactions
[**refund_transaction_using_post**](PaymentsTransactionsApi.md#refund_transaction_using_post) | **POST** /transactions/{id}/refunds | Refund a payment transaction, in full or in part


# **get_transaction_using_get**
> TransactionResource get_transaction_using_get(id)

Get the details for a single transaction

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsTransactionsApi()
id = 56 # int | id

try: 
    # Get the details for a single transaction
    api_response = api_instance.get_transaction_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsTransactionsApi->get_transaction_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**TransactionResource**](TransactionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_using_get**
> PageTransactionResource get_transactions_using_get(filter_invoice=filter_invoice, size=size, page=page, order=order)

List and search transactions

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsTransactionsApi()
filter_invoice = 56 # int | Filter for transactions from a specific invoice (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List and search transactions
    api_response = api_instance.get_transactions_using_get(filter_invoice=filter_invoice, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsTransactionsApi->get_transactions_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_invoice** | **int**| Filter for transactions from a specific invoice | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageTransactionResource**](PageTransactionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_transaction_using_post**
> RefundResource refund_transaction_using_post(id, request=request)

Refund a payment transaction, in full or in part

Will not allow for refunding more than the full amount even with multiple partial refunds. Money is refunded to the payment method used to make the original payment. Payment method must support refunds.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsTransactionsApi()
id = 56 # int | The id of the transaction to refund
request = swagger_client.RefundRequest() # RefundRequest | Request containing refund details (optional)

try: 
    # Refund a payment transaction, in full or in part
    api_response = api_instance.refund_transaction_using_post(id, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsTransactionsApi->refund_transaction_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the transaction to refund | 
 **request** | [**RefundRequest**](RefundRequest.md)| Request containing refund details | [optional] 

### Return type

[**RefundResource**](RefundResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

