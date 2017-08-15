# knetik_cloud.InvoicesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice**](InvoicesApi.md#create_invoice) | **POST** /invoices | Create an invoice
[**get_ful_fillment_statuses**](InvoicesApi.md#get_ful_fillment_statuses) | **GET** /invoices/fulfillment-statuses | Lists available fulfillment statuses
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /invoices/{id} | Retrieve an invoice
[**get_invoice_logs**](InvoicesApi.md#get_invoice_logs) | **GET** /invoices/{id}/logs | List invoice logs
[**get_invoices**](InvoicesApi.md#get_invoices) | **GET** /invoices | Retrieve invoices
[**get_payment_statuses**](InvoicesApi.md#get_payment_statuses) | **GET** /invoices/payment-statuses | Lists available payment statuses
[**pay_invoice**](InvoicesApi.md#pay_invoice) | **POST** /invoices/{id}/payments | Pay an invoice using a saved payment method
[**set_bundled_invoice_item_fulfillment_status**](InvoicesApi.md#set_bundled_invoice_item_fulfillment_status) | **PUT** /invoices/{id}/items/{bundleSku}/bundled-skus/{sku}/fulfillment-status | Set the fulfillment status of a bundled invoice item
[**set_external_ref**](InvoicesApi.md#set_external_ref) | **PUT** /invoices/{id}/external-ref | Set the external reference of an invoice
[**set_invoice_item_fulfillment_status**](InvoicesApi.md#set_invoice_item_fulfillment_status) | **PUT** /invoices/{id}/items/{sku}/fulfillment-status | Set the fulfillment status of an invoice item
[**set_order_notes**](InvoicesApi.md#set_order_notes) | **PUT** /invoices/{id}/order-notes | Set the order notes of an invoice
[**set_payment_status**](InvoicesApi.md#set_payment_status) | **PUT** /invoices/{id}/payment-status | Set the payment status of an invoice
[**update_billing_info**](InvoicesApi.md#update_billing_info) | **PUT** /invoices/{id}/billing-address | Set or update billing info


# **create_invoice**
> list[InvoiceResource] create_invoice(req=req)

Create an invoice

Create an invoice(s) by providing a cart GUID. Note that there may be multiple invoices created, one per vendor.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
req = knetik_cloud.InvoiceCreateRequest() # InvoiceCreateRequest | Invoice to be created (optional)

try: 
    # Create an invoice
    api_response = api_instance.create_invoice(req=req)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **req** | [**InvoiceCreateRequest**](InvoiceCreateRequest.md)| Invoice to be created | [optional] 

### Return type

[**list[InvoiceResource]**](InvoiceResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ful_fillment_statuses**
> list[str] get_ful_fillment_statuses()

Lists available fulfillment statuses

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()

try: 
    # Lists available fulfillment statuses
    api_response = api_instance.get_ful_fillment_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_ful_fillment_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> InvoiceResource get_invoice(id)

Retrieve an invoice

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice

try: 
    # Retrieve an invoice
    api_response = api_instance.get_invoice(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 

### Return type

[**InvoiceResource**](InvoiceResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_logs**
> PageResourceInvoiceLogEntry get_invoice_logs(id, size=size, page=page)

List invoice logs

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List invoice logs
    api_response = api_instance.get_invoice_logs(id, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoice_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceInvoiceLogEntry**](PageResourceInvoiceLogEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> PageResourceInvoiceResource get_invoices(filter_user=filter_user, filter_email=filter_email, filter_fulfillment_status=filter_fulfillment_status, filter_payment_status=filter_payment_status, filter_item_name=filter_item_name, filter_external_ref=filter_external_ref, filter_created_date=filter_created_date, filter_vendor_ids=filter_vendor_ids, filter_currency=filter_currency, filter_shipping_state_name=filter_shipping_state_name, filter_shipping_country_name=filter_shipping_country_name, filter_shipping=filter_shipping, filter_vendor_name=filter_vendor_name, filter_sku=filter_sku, size=size, page=page, order=order)

Retrieve invoices

Without INVOICES_ADMIN permission the results are automatically filtered for only the logged in user's invoices. It is recomended however that filter_user be added to avoid issues for admin users accidentally getting additional invoices.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
filter_user = 56 # int | The id of a user to get invoices for. Automtically added if not being called with admin permissions. (optional)
filter_email = 'filter_email_example' # str | Filters invoices by customer's email. Admins only. (optional)
filter_fulfillment_status = 'filter_fulfillment_status_example' # str | Filters invoices by fulfillment status type. Can be a comma separated list of statuses (optional)
filter_payment_status = 'filter_payment_status_example' # str | Filters invoices by payment status type. Can be a comma separated list of statuses (optional)
filter_item_name = 'filter_item_name_example' # str | Filters invoices by item name containing the given string (optional)
filter_external_ref = 'filter_external_ref_example' # str | Filters invoices by external reference. (optional)
filter_created_date = 'filter_created_date_example' # str | Filters invoices by creation date. Multiple values possible for range search. Format: filter_created_date=OP,ts&... where OP in (GT, LT, GOE, LOE, EQ) and ts is a unix timestamp in seconds. Ex: filter_created_date=GT,1452154258,LT,1554254874 (optional)
filter_vendor_ids = 'filter_vendor_ids_example' # str | Filters invoices for ones from one of the vendors whose id is in the given comma separated list (optional)
filter_currency = 'filter_currency_example' # str | Filters invoices by currency. ISO3 currency code (optional)
filter_shipping_state_name = 'filter_shipping_state_name_example' # str | Filters invoices by shipping address: Exact match state name (optional)
filter_shipping_country_name = 'filter_shipping_country_name_example' # str | Filters invoices by shipping address: Exact match country name (optional)
filter_shipping = 'filter_shipping_example' # str | Filters invoices by shipping price. Multiple values possible for range search. Format: filter_shipping=OP,ts&... where OP in (GT, LT, GOE, LOE, EQ). Ex: filter_shipping=GT,14.58,LT,15.54 (optional)
filter_vendor_name = 'filter_vendor_name_example' # str | Filters invoices by vendor name starting with given string (optional)
filter_sku = 'filter_sku_example' # str | Filters invoices by item sku (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # Retrieve invoices
    api_response = api_instance.get_invoices(filter_user=filter_user, filter_email=filter_email, filter_fulfillment_status=filter_fulfillment_status, filter_payment_status=filter_payment_status, filter_item_name=filter_item_name, filter_external_ref=filter_external_ref, filter_created_date=filter_created_date, filter_vendor_ids=filter_vendor_ids, filter_currency=filter_currency, filter_shipping_state_name=filter_shipping_state_name, filter_shipping_country_name=filter_shipping_country_name, filter_shipping=filter_shipping, filter_vendor_name=filter_vendor_name, filter_sku=filter_sku, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_user** | **int**| The id of a user to get invoices for. Automtically added if not being called with admin permissions. | [optional] 
 **filter_email** | **str**| Filters invoices by customer&#39;s email. Admins only. | [optional] 
 **filter_fulfillment_status** | **str**| Filters invoices by fulfillment status type. Can be a comma separated list of statuses | [optional] 
 **filter_payment_status** | **str**| Filters invoices by payment status type. Can be a comma separated list of statuses | [optional] 
 **filter_item_name** | **str**| Filters invoices by item name containing the given string | [optional] 
 **filter_external_ref** | **str**| Filters invoices by external reference. | [optional] 
 **filter_created_date** | **str**| Filters invoices by creation date. Multiple values possible for range search. Format: filter_created_date&#x3D;OP,ts&amp;... where OP in (GT, LT, GOE, LOE, EQ) and ts is a unix timestamp in seconds. Ex: filter_created_date&#x3D;GT,1452154258,LT,1554254874 | [optional] 
 **filter_vendor_ids** | **str**| Filters invoices for ones from one of the vendors whose id is in the given comma separated list | [optional] 
 **filter_currency** | **str**| Filters invoices by currency. ISO3 currency code | [optional] 
 **filter_shipping_state_name** | **str**| Filters invoices by shipping address: Exact match state name | [optional] 
 **filter_shipping_country_name** | **str**| Filters invoices by shipping address: Exact match country name | [optional] 
 **filter_shipping** | **str**| Filters invoices by shipping price. Multiple values possible for range search. Format: filter_shipping&#x3D;OP,ts&amp;... where OP in (GT, LT, GOE, LOE, EQ). Ex: filter_shipping&#x3D;GT,14.58,LT,15.54 | [optional] 
 **filter_vendor_name** | **str**| Filters invoices by vendor name starting with given string | [optional] 
 **filter_sku** | **str**| Filters invoices by item sku | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageResourceInvoiceResource**](PageResourceInvoiceResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_statuses**
> list[str] get_payment_statuses()

Lists available payment statuses

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()

try: 
    # Lists available payment statuses
    api_response = api_instance.get_payment_statuses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_payment_statuses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_invoice**
> pay_invoice(id, request=request)

Pay an invoice using a saved payment method

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice
request = knetik_cloud.PayBySavedMethodRequest() # PayBySavedMethodRequest | The payment method details. Will default to the appropriate user's wallet in the invoice currency if ommited. (optional)

try: 
    # Pay an invoice using a saved payment method
    api_instance.pay_invoice(id, request=request)
except ApiException as e:
    print("Exception when calling InvoicesApi->pay_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 
 **request** | [**PayBySavedMethodRequest**](PayBySavedMethodRequest.md)| The payment method details. Will default to the appropriate user&#39;s wallet in the invoice currency if ommited. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_bundled_invoice_item_fulfillment_status**
> set_bundled_invoice_item_fulfillment_status(id, bundle_sku, sku, status)

Set the fulfillment status of a bundled invoice item

This allows external fulfillment systems to report success or failure. Fulfillment status changes are restricted by a specific flow determining which status can lead to which.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice
bundle_sku = 'bundle_sku_example' # str | The sku of the bundle in the invoice that contains the given target
sku = 'sku_example' # str | The sku of an item in the bundle in the invoice
status = knetik_cloud.StringWrapper() # StringWrapper | The new fulfillment status for the item. Additional options may be available based on configuration.  Allowable values:  'unfulfilled', 'fulfilled', 'not fulfillable', 'failed', 'processing', 'failed_permanent', 'delayed'

try: 
    # Set the fulfillment status of a bundled invoice item
    api_instance.set_bundled_invoice_item_fulfillment_status(id, bundle_sku, sku, status)
except ApiException as e:
    print("Exception when calling InvoicesApi->set_bundled_invoice_item_fulfillment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 
 **bundle_sku** | **str**| The sku of the bundle in the invoice that contains the given target | 
 **sku** | **str**| The sku of an item in the bundle in the invoice | 
 **status** | [**StringWrapper**](StringWrapper.md)| The new fulfillment status for the item. Additional options may be available based on configuration.  Allowable values:  &#39;unfulfilled&#39;, &#39;fulfilled&#39;, &#39;not fulfillable&#39;, &#39;failed&#39;, &#39;processing&#39;, &#39;failed_permanent&#39;, &#39;delayed&#39; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_external_ref**
> set_external_ref(id, external_ref=external_ref)

Set the external reference of an invoice

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice
external_ref = knetik_cloud.StringWrapper() # StringWrapper | External reference info (optional)

try: 
    # Set the external reference of an invoice
    api_instance.set_external_ref(id, external_ref=external_ref)
except ApiException as e:
    print("Exception when calling InvoicesApi->set_external_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 
 **external_ref** | [**StringWrapper**](StringWrapper.md)| External reference info | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_invoice_item_fulfillment_status**
> set_invoice_item_fulfillment_status(id, sku, status)

Set the fulfillment status of an invoice item

This allows external fulfillment systems to report success or failure. Fulfillment status changes are restricted by a specific flow determining which status can lead to which.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice
sku = 'sku_example' # str | The sku of an item in the invoice
status = knetik_cloud.StringWrapper() # StringWrapper | The new fulfillment status for the item. Additional options may be available based on configuration.  Allowable values:  'unfulfilled', 'fulfilled', 'not fulfillable', 'failed', 'processing', 'failed_permanent', 'delayed'

try: 
    # Set the fulfillment status of an invoice item
    api_instance.set_invoice_item_fulfillment_status(id, sku, status)
except ApiException as e:
    print("Exception when calling InvoicesApi->set_invoice_item_fulfillment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 
 **sku** | **str**| The sku of an item in the invoice | 
 **status** | [**StringWrapper**](StringWrapper.md)| The new fulfillment status for the item. Additional options may be available based on configuration.  Allowable values:  &#39;unfulfilled&#39;, &#39;fulfilled&#39;, &#39;not fulfillable&#39;, &#39;failed&#39;, &#39;processing&#39;, &#39;failed_permanent&#39;, &#39;delayed&#39; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_order_notes**
> set_order_notes(id, order_notes=order_notes)

Set the order notes of an invoice

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice
order_notes = knetik_cloud.StringWrapper() # StringWrapper | Payment status info (optional)

try: 
    # Set the order notes of an invoice
    api_instance.set_order_notes(id, order_notes=order_notes)
except ApiException as e:
    print("Exception when calling InvoicesApi->set_order_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 
 **order_notes** | [**StringWrapper**](StringWrapper.md)| Payment status info | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_payment_status**
> set_payment_status(id, request=request)

Set the payment status of an invoice

This may trigger fulfillment if setting the status to 'paid'. This is mainly intended to support external payment systems that cannot be incorporated into the payment method system. Payment status changes are restricted by a specific flow determining which status can lead to which.

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice
request = knetik_cloud.InvoicePaymentStatusRequest() # InvoicePaymentStatusRequest | Payment status info (optional)

try: 
    # Set the payment status of an invoice
    api_instance.set_payment_status(id, request=request)
except ApiException as e:
    print("Exception when calling InvoicesApi->set_payment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 
 **request** | [**InvoicePaymentStatusRequest**](InvoicePaymentStatusRequest.md)| Payment status info | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_billing_info**
> update_billing_info(id, billing_info_request=billing_info_request)

Set or update billing info

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.InvoicesApi()
id = 56 # int | The id of the invoice
billing_info_request = knetik_cloud.AddressResource() # AddressResource | Address info (optional)

try: 
    # Set or update billing info
    api_instance.update_billing_info(id, billing_info_request=billing_info_request)
except ApiException as e:
    print("Exception when calling InvoicesApi->update_billing_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the invoice | 
 **billing_info_request** | [**AddressResource**](AddressResource.md)| Address info | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

