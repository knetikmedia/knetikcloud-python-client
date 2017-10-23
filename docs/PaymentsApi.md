# knetik_cloud.PaymentsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method**](PaymentsApi.md#create_payment_method) | **POST** /users/{user_id}/payment-methods | Create a new payment method for a user
[**delete_payment_method**](PaymentsApi.md#delete_payment_method) | **DELETE** /users/{user_id}/payment-methods/{id} | Delete an existing payment method for a user
[**get_payment_method**](PaymentsApi.md#get_payment_method) | **GET** /users/{user_id}/payment-methods/{id} | Get a single payment method for a user
[**get_payment_method_type**](PaymentsApi.md#get_payment_method_type) | **GET** /payment/types/{id} | Get a single payment method type
[**get_payment_method_types**](PaymentsApi.md#get_payment_method_types) | **GET** /payment/types | Get all payment method types
[**get_payment_methods**](PaymentsApi.md#get_payment_methods) | **GET** /users/{user_id}/payment-methods | Get all payment methods for a user
[**payment_authorization**](PaymentsApi.md#payment_authorization) | **POST** /payment/authorizations | Authorize payment of an invoice for later capture
[**payment_capture**](PaymentsApi.md#payment_capture) | **POST** /payment/authorizations/{id}/capture | Capture an existing invoice payment authorization
[**update_payment_method**](PaymentsApi.md#update_payment_method) | **PUT** /users/{user_id}/payment-methods/{id} | Update an existing payment method for a user


# **create_payment_method**
> PaymentMethodResource create_payment_method(user_id, payment_method=payment_method)

Create a new payment method for a user

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
api_instance = knetik_cloud.PaymentsApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | ID of the user for whom the payment method is being created
payment_method = knetik_cloud.PaymentMethodResource() # PaymentMethodResource | Payment method being created (optional)

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

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> delete_payment_method(user_id, id)

Delete an existing payment method for a user

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
api_instance = knetik_cloud.PaymentsApi(knetik_cloud.ApiClient(configuration))
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

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> PaymentMethodResource get_payment_method(user_id, id)

Get a single payment method for a user

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
api_instance = knetik_cloud.PaymentsApi(knetik_cloud.ApiClient(configuration))
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

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_type**
> PaymentMethodTypeResource get_payment_method_type(id)

Get a single payment method type

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.PaymentsApi()
id = 56 # int | ID of the payment method type being retrieved

try: 
    # Get a single payment method type
    api_response = api_instance.get_payment_method_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_method_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the payment method type being retrieved | 

### Return type

[**PaymentMethodTypeResource**](PaymentMethodTypeResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_types**
> PageResourcePaymentMethodTypeResource get_payment_method_types(filter_name=filter_name, size=size, page=page, order=order)

Get all payment method types

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.PaymentsApi()
filter_name = 'filter_name_example' # str | Filter for payment method types whose name matches a given string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get all payment method types
    api_response = api_instance.get_payment_method_types(filter_name=filter_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_method_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| Filter for payment method types whose name matches a given string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourcePaymentMethodTypeResource**](PageResourcePaymentMethodTypeResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_methods**
> list[PaymentMethodResource] get_payment_methods(user_id, filter_name=filter_name, filter_payment_type=filter_payment_type, filter_payment_method_type_id=filter_payment_method_type_id, filter_payment_method_type_name=filter_payment_method_type_name, size=size, page=page, order=order)

Get all payment methods for a user

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
api_instance = knetik_cloud.PaymentsApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | ID of the user for whom the payment methods are being retrieved
filter_name = 'filter_name_example' # str | Filter for payment methods whose name starts with a given string (optional)
filter_payment_type = 'filter_payment_type_example' # str | Filter for payment methods with a specific payment type (optional)
filter_payment_method_type_id = 56 # int | Filter for payment methods with a specific payment method type by id (optional)
filter_payment_method_type_name = 'filter_payment_method_type_name_example' # str | Filter for payment methods whose payment method type name starts with a given string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get all payment methods for a user
    api_response = api_instance.get_payment_methods(user_id, filter_name=filter_name, filter_payment_type=filter_payment_type, filter_payment_method_type_id=filter_payment_method_type_id, filter_payment_method_type_name=filter_payment_method_type_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of the user for whom the payment methods are being retrieved | 
 **filter_name** | **str**| Filter for payment methods whose name starts with a given string | [optional] 
 **filter_payment_type** | **str**| Filter for payment methods with a specific payment type | [optional] 
 **filter_payment_method_type_id** | **int**| Filter for payment methods with a specific payment method type by id | [optional] 
 **filter_payment_method_type_name** | **str**| Filter for payment methods whose payment method type name starts with a given string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| a comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**list[PaymentMethodResource]**](PaymentMethodResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_authorization**
> PaymentAuthorizationResource payment_authorization(request=request)

Authorize payment of an invoice for later capture

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
api_instance = knetik_cloud.PaymentsApi(knetik_cloud.ApiClient(configuration))
request = knetik_cloud.PaymentAuthorizationResource() # PaymentAuthorizationResource | Payment authorization request (optional)

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

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_capture**
> payment_capture(id)

Capture an existing invoice payment authorization

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
api_instance = knetik_cloud.PaymentsApi(knetik_cloud.ApiClient(configuration))
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

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_method**
> PaymentMethodResource update_payment_method(user_id, id, payment_method=payment_method)

Update an existing payment method for a user

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
api_instance = knetik_cloud.PaymentsApi(knetik_cloud.ApiClient(configuration))
user_id = 56 # int | ID of the user for whom the payment method is being updated
id = 56 # int | ID of the payment method being updated
payment_method = knetik_cloud.PaymentMethodResource() # PaymentMethodResource | The updated payment method data (optional)

try: 
    # Update an existing payment method for a user
    api_response = api_instance.update_payment_method(user_id, id, payment_method=payment_method)
    pprint(api_response)
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

[**PaymentMethodResource**](PaymentMethodResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

