# swagger_client.PaymentsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method**](PaymentsApi.md#create_payment_method) | **POST** /users/{user_id}/payment-methods | Create a new payment method for a user
[**delete_payment_method**](PaymentsApi.md#delete_payment_method) | **DELETE** /users/{user_id}/payment-methods/{id} | Delete an existing payment method for a user
[**get_payment_method**](PaymentsApi.md#get_payment_method) | **GET** /users/{user_id}/payment-methods/{id} | Get a single payment method for a user
[**get_payment_methods**](PaymentsApi.md#get_payment_methods) | **GET** /users/{user_id}/payment-methods | Get all payment methods for a user
[**payment_authorization**](PaymentsApi.md#payment_authorization) | **POST** /payment/authorizations | Authorize payment of an invoice for later capture
[**payment_capture**](PaymentsApi.md#payment_capture) | **POST** /payment/authorizations/{id}/capture | Capture an existing invoice payment authorization
[**update_payment_method**](PaymentsApi.md#update_payment_method) | **PUT** /users/{user_id}/payment-methods/{id} | Update an existing payment method for a user


# **create_payment_method**
> PaymentMethodResource create_payment_method(user_id, payment_method=payment_method)

Create a new payment method for a user

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
api_instance = swagger_client.PaymentsApi()
user_id = 56 # int | ID of the user for whom the payment method is being created
payment_method = swagger_client.PaymentMethodResource() # PaymentMethodResource | Payment method being created (optional)

try: 
    # Create a new payment method for a user
    api_response = api_instance.create_payment_method(user_id, payment_method=payment_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->create_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user for whom the payment method is being created | 
 **payment_method** | [**PaymentMethodResource**](PaymentMethodResource.md)| Payment method being created | [optional] 

### Return type

[**PaymentMethodResource**](PaymentMethodResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> delete_payment_method(user_id, id)

Delete an existing payment method for a user

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
api_instance = swagger_client.PaymentsApi()
user_id = 56 # int | ID of the user for whom the payment method is being updated
id = 56 # int | ID of the payment method being deleted

try: 
    # Delete an existing payment method for a user
    api_instance.delete_payment_method(user_id, id)
except ApiException as e:
    print("Exception when calling PaymentsApi->delete_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user for whom the payment method is being updated | 
 **id** | **int**| ID of the payment method being deleted | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> PaymentMethodResource get_payment_method(user_id, id)

Get a single payment method for a user

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
api_instance = swagger_client.PaymentsApi()
user_id = 56 # int | ID of the user for whom the payment method is being retrieved
id = 56 # int | ID of the payment method being retrieved

try: 
    # Get a single payment method for a user
    api_response = api_instance.get_payment_method(user_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user for whom the payment method is being retrieved | 
 **id** | **int**| ID of the payment method being retrieved | 

### Return type

[**PaymentMethodResource**](PaymentMethodResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_methods**
> list[PaymentMethodResource] get_payment_methods(user_id, size=size, page=page, order=order)

Get all payment methods for a user

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
api_instance = swagger_client.PaymentsApi()
user_id = 56 # int | ID of the user for whom the payment methods are being retrieved
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get all payment methods for a user
    api_response = api_instance.get_payment_methods(user_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user for whom the payment methods are being retrieved | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**list[PaymentMethodResource]**](PaymentMethodResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_authorization**
> PaymentAuthorizationResource payment_authorization(request=request)

Authorize payment of an invoice for later capture

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
api_instance = swagger_client.PaymentsApi()
request = swagger_client.PaymentAuthorizationResource() # PaymentAuthorizationResource | Payment authorization request (optional)

try: 
    # Authorize payment of an invoice for later capture
    api_response = api_instance.payment_authorization(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->payment_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PaymentAuthorizationResource**](PaymentAuthorizationResource.md)| Payment authorization request | [optional] 

### Return type

[**PaymentAuthorizationResource**](PaymentAuthorizationResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_capture**
> payment_capture(id)

Capture an existing invoice payment authorization

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
api_instance = swagger_client.PaymentsApi()
id = 56 # int | ID of the payment authorization to capture

try: 
    # Capture an existing invoice payment authorization
    api_instance.payment_capture(id)
except ApiException as e:
    print("Exception when calling PaymentsApi->payment_capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the payment authorization to capture | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_method**
> update_payment_method(user_id, id, payment_method=payment_method)

Update an existing payment method for a user

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
api_instance = swagger_client.PaymentsApi()
user_id = 56 # int | ID of the user for whom the payment method is being updated
id = 56 # int | ID of the payment method being updated
payment_method = swagger_client.PaymentMethodResource() # PaymentMethodResource | The updated payment method data (optional)

try: 
    # Update an existing payment method for a user
    api_instance.update_payment_method(user_id, id, payment_method=payment_method)
except ApiException as e:
    print("Exception when calling PaymentsApi->update_payment_method: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user for whom the payment method is being updated | 
 **id** | **int**| ID of the payment method being updated | 
 **payment_method** | [**PaymentMethodResource**](PaymentMethodResource.md)| The updated payment method data | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

