# swagger_client.UsersSubscriptionsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subscription_details_using_get**](UsersSubscriptionsApi.md#get_subscription_details_using_get) | **GET** /users/{user_id}/subscriptions/{inventory_id} | Get details about a user&#39;s subscription
[**get_subscription_details_using_get1**](UsersSubscriptionsApi.md#get_subscription_details_using_get1) | **GET** /users/{user_id}/subscriptions | Get details about a user&#39;s subscriptions
[**reactivate_using_post**](UsersSubscriptionsApi.md#reactivate_using_post) | **POST** /users/{user_id}/subscriptions/{inventory_id}/reactivate | Reactivate a subscription and charge fee
[**set_bill_date_using_put**](UsersSubscriptionsApi.md#set_bill_date_using_put) | **PUT** /users/{user_id}/subscriptions/{inventory_id}/bill-date | Set a new date to bill a subscription on
[**set_payment_method_using_put**](UsersSubscriptionsApi.md#set_payment_method_using_put) | **PUT** /users/{user_id}/subscriptions/{inventory_id}/payment-method | Set the payment method to use for a subscription
[**set_status_using_put**](UsersSubscriptionsApi.md#set_status_using_put) | **PUT** /users/{user_id}/subscriptions/{inventory_id}/status | Set the status of a subscription
[**set_user_plan_using_put**](UsersSubscriptionsApi.md#set_user_plan_using_put) | **PUT** /users/{user_id}/subscriptions/{inventory_id}/plan | Set a new subscription plan for a user


# **get_subscription_details_using_get**
> InventorySubscriptionResource get_subscription_details_using_get(user_id, inventory_id)

Get details about a user's subscription

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
api_instance = swagger_client.UsersSubscriptionsApi()
user_id = 56 # int | The id of the user
inventory_id = 56 # int | The id of the user's inventory

try: 
    # Get details about a user's subscription
    api_response = api_instance.get_subscription_details_using_get(user_id, inventory_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersSubscriptionsApi->get_subscription_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **inventory_id** | **int**| The id of the user&#39;s inventory | 

### Return type

[**InventorySubscriptionResource**](InventorySubscriptionResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_details_using_get1**
> list[InventorySubscriptionResource] get_subscription_details_using_get1(user_id)

Get details about a user's subscriptions

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
api_instance = swagger_client.UsersSubscriptionsApi()
user_id = 56 # int | The id of the user

try: 
    # Get details about a user's subscriptions
    api_response = api_instance.get_subscription_details_using_get1(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersSubscriptionsApi->get_subscription_details_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

[**list[InventorySubscriptionResource]**](InventorySubscriptionResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_using_post**
> InvoiceResource reactivate_using_post(user_id, inventory_id, reactivate_subscription_request=reactivate_subscription_request)

Reactivate a subscription and charge fee

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
api_instance = swagger_client.UsersSubscriptionsApi()
user_id = 56 # int | The id of the user
inventory_id = 56 # int | The id of the user's inventory
reactivate_subscription_request = swagger_client.ReactivateSubscriptionRequest() # ReactivateSubscriptionRequest | The reactivate subscription request object inventory (optional)

try: 
    # Reactivate a subscription and charge fee
    api_response = api_instance.reactivate_using_post(user_id, inventory_id, reactivate_subscription_request=reactivate_subscription_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersSubscriptionsApi->reactivate_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **inventory_id** | **int**| The id of the user&#39;s inventory | 
 **reactivate_subscription_request** | [**ReactivateSubscriptionRequest**](ReactivateSubscriptionRequest.md)| The reactivate subscription request object inventory | [optional] 

### Return type

[**InvoiceResource**](InvoiceResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_bill_date_using_put**
> set_bill_date_using_put(user_id, inventory_id, bill_date)

Set a new date to bill a subscription on

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
api_instance = swagger_client.UsersSubscriptionsApi()
user_id = 56 # int | The id of the user
inventory_id = 56 # int | The id of the user's inventory
bill_date = 789 # int | The new bill date. Unix timestamp in seconds

try: 
    # Set a new date to bill a subscription on
    api_instance.set_bill_date_using_put(user_id, inventory_id, bill_date)
except ApiException as e:
    print("Exception when calling UsersSubscriptionsApi->set_bill_date_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **inventory_id** | **int**| The id of the user&#39;s inventory | 
 **bill_date** | **int**| The new bill date. Unix timestamp in seconds | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_payment_method_using_put**
> set_payment_method_using_put(user_id, inventory_id, payment_method_id=payment_method_id)

Set the payment method to use for a subscription

May send null to use floating default

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
api_instance = swagger_client.UsersSubscriptionsApi()
user_id = 56 # int | The id of the user
inventory_id = 56 # int | The id of the user's inventory
payment_method_id = 56 # int | The id of the payment method (optional)

try: 
    # Set the payment method to use for a subscription
    api_instance.set_payment_method_using_put(user_id, inventory_id, payment_method_id=payment_method_id)
except ApiException as e:
    print("Exception when calling UsersSubscriptionsApi->set_payment_method_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **inventory_id** | **int**| The id of the user&#39;s inventory | 
 **payment_method_id** | **int**| The id of the payment method | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_status_using_put**
> set_status_using_put(user_id, inventory_id, status)

Set the status of a subscription

The body is a json string (put in quotes) that should match a desired invoice status type. Note that the new status may be blocked if the system is not configured to allow the current status to be changed to the new, to enforce proper flow. The default options for statuses are shown below but may be altered for special use cases

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
api_instance = swagger_client.UsersSubscriptionsApi()
user_id = 56 # int | The id of the user
inventory_id = 56 # int | The id of the user's inventory
status = 'status_example' # str | The new status for the subscription. Actual options may differ from the indicated set if the invoice status type data has been altered.  Allowable values: ('current', 'canceled', 'stopped', 'payment_failed', 'suspended')

try: 
    # Set the status of a subscription
    api_instance.set_status_using_put(user_id, inventory_id, status)
except ApiException as e:
    print("Exception when calling UsersSubscriptionsApi->set_status_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **inventory_id** | **int**| The id of the user&#39;s inventory | 
 **status** | **str**| The new status for the subscription. Actual options may differ from the indicated set if the invoice status type data has been altered.  Allowable values: (&#39;current&#39;, &#39;canceled&#39;, &#39;stopped&#39;, &#39;payment_failed&#39;, &#39;suspended&#39;) | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_plan_using_put**
> set_user_plan_using_put(user_id, inventory_id, plan_id=plan_id)

Set a new subscription plan for a user

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
api_instance = swagger_client.UsersSubscriptionsApi()
user_id = 56 # int | The id of the user
inventory_id = 56 # int | The id of the user's inventory
plan_id = 'plan_id_example' # str | The id of the new plan. Must be from the same subscription (optional)

try: 
    # Set a new subscription plan for a user
    api_instance.set_user_plan_using_put(user_id, inventory_id, plan_id=plan_id)
except ApiException as e:
    print("Exception when calling UsersSubscriptionsApi->set_user_plan_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **inventory_id** | **int**| The id of the user&#39;s inventory | 
 **plan_id** | **str**| The id of the new plan. Must be from the same subscription | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

