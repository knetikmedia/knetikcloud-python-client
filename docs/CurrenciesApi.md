# swagger_client.CurrenciesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_currency_using_post**](CurrenciesApi.md#create_currency_using_post) | **POST** /currencies | Create a currency
[**delete_currency_using_delete**](CurrenciesApi.md#delete_currency_using_delete) | **DELETE** /currencies/{code} | Delete a currency
[**get_currencies_using_get**](CurrenciesApi.md#get_currencies_using_get) | **GET** /currencies | List and search currencies
[**get_currency_using_get**](CurrenciesApi.md#get_currency_using_get) | **GET** /currencies/{code} | Get a single currency
[**update_currency_using_put**](CurrenciesApi.md#update_currency_using_put) | **PUT** /currencies/{code} | Update a currency


# **create_currency_using_post**
> CurrencyResource create_currency_using_post(currency=currency)

Create a currency

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
api_instance = swagger_client.CurrenciesApi()
currency = swagger_client.CurrencyResource() # CurrencyResource | The currency object (optional)

try: 
    # Create a currency
    api_response = api_instance.create_currency_using_post(currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->create_currency_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | [**CurrencyResource**](CurrencyResource.md)| The currency object | [optional] 

### Return type

[**CurrencyResource**](CurrencyResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_currency_using_delete**
> delete_currency_using_delete(code)

Delete a currency

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
api_instance = swagger_client.CurrenciesApi()
code = 'code_example' # str | The currency code

try: 
    # Delete a currency
    api_instance.delete_currency_using_delete(code)
except ApiException as e:
    print("Exception when calling CurrenciesApi->delete_currency_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies_using_get**
> PageCurrencyResource get_currencies_using_get(filter_enabled_currencies=filter_enabled_currencies, filter_type=filter_type, size=size, page=page, order=order)

List and search currencies

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CurrenciesApi()
filter_enabled_currencies = true # bool | Filter for alternate currencies setup explicitely in system config (optional)
filter_type = 'filter_type_example' # str | Filter currencies by type.  Allowable values: ('virtual', 'real') (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)

try: 
    # List and search currencies
    api_response = api_instance.get_currencies_using_get(filter_enabled_currencies=filter_enabled_currencies, filter_type=filter_type, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->get_currencies_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_enabled_currencies** | **bool**| Filter for alternate currencies setup explicitely in system config | [optional] 
 **filter_type** | **str**| Filter currencies by type.  Allowable values: (&#39;virtual&#39;, &#39;real&#39;) | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to name:ASC]

### Return type

[**PageCurrencyResource**](PageCurrencyResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_using_get**
> CurrencyResource get_currency_using_get(code)

Get a single currency

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CurrenciesApi()
code = 'code_example' # str | The currency code

try: 
    # Get a single currency
    api_response = api_instance.get_currency_using_get(code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->get_currency_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code | 

### Return type

[**CurrencyResource**](CurrencyResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currency_using_put**
> update_currency_using_put(code, currency=currency)

Update a currency

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
api_instance = swagger_client.CurrenciesApi()
code = 'code_example' # str | The currency code
currency = swagger_client.CurrencyResource() # CurrencyResource | The currency object (optional)

try: 
    # Update a currency
    api_instance.update_currency_using_put(code, currency=currency)
except ApiException as e:
    print("Exception when calling CurrenciesApi->update_currency_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The currency code | 
 **currency** | [**CurrencyResource**](CurrencyResource.md)| The currency object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

