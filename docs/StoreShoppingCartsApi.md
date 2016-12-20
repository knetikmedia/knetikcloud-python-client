# swagger_client.StoreShoppingCartsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_discount_using_post**](StoreShoppingCartsApi.md#add_discount_using_post) | **POST** /carts/{id}/discounts | Adds a coupon to the cart
[**add_item_using_post**](StoreShoppingCartsApi.md#add_item_using_post) | **POST** /carts/{id}/items | Add an item to the cart
[**assign_cart_using_put**](StoreShoppingCartsApi.md#assign_cart_using_put) | **PUT** /carts/{id}/owner | Sets the owner of a cart if none is set already
[**check_shippable_using_get**](StoreShoppingCartsApi.md#check_shippable_using_get) | **GET** /carts/{id}/shippable | Returns whether a cart requires shipping
[**create_cart_using_post**](StoreShoppingCartsApi.md#create_cart_using_post) | **POST** /carts | Creates a new cart from scratch
[**get_cart_using_get**](StoreShoppingCartsApi.md#get_cart_using_get) | **GET** /carts/{id} | Returns the cart with the given GUID
[**get_countries_using_get**](StoreShoppingCartsApi.md#get_countries_using_get) | **GET** /carts/{id}/countries | Get the list of available shipping countries per vendor
[**modify_shipping_address_using_put**](StoreShoppingCartsApi.md#modify_shipping_address_using_put) | **PUT** /carts/{id}/shipping-address | Modifies or sets the order shipping address
[**remove_discount_using_delete**](StoreShoppingCartsApi.md#remove_discount_using_delete) | **DELETE** /carts/{id}/discounts/{code} | Removes a coupon from the cart
[**search_carts_using_get**](StoreShoppingCartsApi.md#search_carts_using_get) | **GET** /carts | Get a list of carts
[**set_cart_currency_using_put**](StoreShoppingCartsApi.md#set_cart_currency_using_put) | **PUT** /carts/{id}/currency | Sets the currency to use for the cart
[**update_item_using_put**](StoreShoppingCartsApi.md#update_item_using_put) | **PUT** /carts/{id}/items | Changes the quantity of an item already in the cart


# **add_discount_using_post**
> add_discount_using_post(id, sku_request=sku_request)

Adds a coupon to the cart

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart
sku_request = swagger_client.SkuRequest() # SkuRequest | The request of the sku (optional)

try: 
    # Adds a coupon to the cart
    api_instance.add_discount_using_post(id, sku_request=sku_request)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->add_discount_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **sku_request** | [**SkuRequest**](SkuRequest.md)| The request of the sku | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_using_post**
> add_item_using_post(id, cart_item_request=cart_item_request)

Add an item to the cart

Currently, carts cannot contain virtual and real currency items at the same time. Furthermore, the API only support a single virtual item at the moment

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart
cart_item_request = swagger_client.CartItemRequest() # CartItemRequest | The cart item request object (optional)

try: 
    # Add an item to the cart
    api_instance.add_item_using_post(id, cart_item_request=cart_item_request)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->add_item_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **cart_item_request** | [**CartItemRequest**](CartItemRequest.md)| The cart item request object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_cart_using_put**
> assign_cart_using_put(id, user_id=user_id)

Sets the owner of a cart if none is set already

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart
user_id = 56 # int | The id of the user (optional)

try: 
    # Sets the owner of a cart if none is set already
    api_instance.assign_cart_using_put(id, user_id=user_id)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->assign_cart_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **user_id** | **int**| The id of the user | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_shippable_using_get**
> CartShippableResponse check_shippable_using_get(id)

Returns whether a cart requires shipping

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart

try: 
    # Returns whether a cart requires shipping
    api_response = api_instance.check_shippable_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->check_shippable_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 

### Return type

[**CartShippableResponse**](CartShippableResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cart_using_post**
> str create_cart_using_post(owner=owner, currency_code=currency_code)

Creates a new cart from scratch

You don't have to have a user to create a cart but the API requires authentication to checkout

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreShoppingCartsApi()
owner = 56 # int | Set the owner of a cart. If not specified, defaults to the calling user's id. If specified and is not the calling user's id, SHOPPING_CARTS_ADMIN permission is required (optional)
currency_code = 'currency_code_example' # str | Set the currency for the cart, by currency code. May be disallowed by site settings. (optional)

try: 
    # Creates a new cart from scratch
    api_response = api_instance.create_cart_using_post(owner=owner, currency_code=currency_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->create_cart_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **int**| Set the owner of a cart. If not specified, defaults to the calling user&#39;s id. If specified and is not the calling user&#39;s id, SHOPPING_CARTS_ADMIN permission is required | [optional] 
 **currency_code** | **str**| Set the currency for the cart, by currency code. May be disallowed by site settings. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart_using_get**
> Cart get_cart_using_get(id)

Returns the cart with the given GUID

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart

try: 
    # Returns the cart with the given GUID
    api_response = api_instance.get_cart_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->get_cart_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 

### Return type

[**Cart**](Cart.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries_using_get**
> SampleCountriesResponse get_countries_using_get(id)

Get the list of available shipping countries per vendor

Since a cart can have multiple vendors with different shipping options, the countries are broken down by vendors. Please see notes about the response object as the fields are variable.

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart

try: 
    # Get the list of available shipping countries per vendor
    api_response = api_instance.get_countries_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->get_countries_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 

### Return type

[**SampleCountriesResponse**](SampleCountriesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_shipping_address_using_put**
> modify_shipping_address_using_put(id, cart_shipping_address_request=cart_shipping_address_request)

Modifies or sets the order shipping address

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart
cart_shipping_address_request = swagger_client.CartShippingAddressRequest() # CartShippingAddressRequest | The cart shipping address request object (optional)

try: 
    # Modifies or sets the order shipping address
    api_instance.modify_shipping_address_using_put(id, cart_shipping_address_request=cart_shipping_address_request)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->modify_shipping_address_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **cart_shipping_address_request** | [**CartShippingAddressRequest**](CartShippingAddressRequest.md)| The cart shipping address request object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_discount_using_delete**
> remove_discount_using_delete(id, code)

Removes a coupon from the cart

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart
code = 'code_example' # str | The SKU code of the coupon to remove

try: 
    # Removes a coupon from the cart
    api_instance.remove_discount_using_delete(id, code)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->remove_discount_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **code** | **str**| The SKU code of the coupon to remove | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_carts_using_get**
> PageCartSummary search_carts_using_get(filter_owner_id=filter_owner_id, size=size, page=page, order=order)

Get a list of carts

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
api_instance = swagger_client.StoreShoppingCartsApi()
filter_owner_id = 56 # int | Filter by the id of the owner (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get a list of carts
    api_response = api_instance.search_carts_using_get(filter_owner_id=filter_owner_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->search_carts_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owner_id** | **int**| Filter by the id of the owner | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageCartSummary**](PageCartSummary.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cart_currency_using_put**
> set_cart_currency_using_put(id, currency_code=currency_code)

Sets the currency to use for the cart

May be disallowed by site settings.

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart
currency_code = 'currency_code_example' # str | The code of the currency (optional)

try: 
    # Sets the currency to use for the cart
    api_instance.set_cart_currency_using_put(id, currency_code=currency_code)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->set_cart_currency_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **currency_code** | **str**| The code of the currency | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_using_put**
> update_item_using_put(id, cart_item_request=cart_item_request)

Changes the quantity of an item already in the cart

A quantity of zero will remove the item from the cart altogether.

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
api_instance = swagger_client.StoreShoppingCartsApi()
id = 'id_example' # str | The id of the cart
cart_item_request = swagger_client.CartItemRequest() # CartItemRequest | The cart item request object (optional)

try: 
    # Changes the quantity of an item already in the cart
    api_instance.update_item_using_put(id, cart_item_request=cart_item_request)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->update_item_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **cart_item_request** | [**CartItemRequest**](CartItemRequest.md)| The cart item request object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

