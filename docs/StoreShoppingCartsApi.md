# knetik_cloud.StoreShoppingCartsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_discount**](StoreShoppingCartsApi.md#add_custom_discount) | **POST** /carts/{id}/custom-discounts | Adds a custom discount to the cart
[**add_discount_to_cart**](StoreShoppingCartsApi.md#add_discount_to_cart) | **POST** /carts/{id}/discounts | Adds a discount coupon to the cart
[**add_item_to_cart**](StoreShoppingCartsApi.md#add_item_to_cart) | **POST** /carts/{id}/items | Add an item to the cart
[**create_cart**](StoreShoppingCartsApi.md#create_cart) | **POST** /carts | Create a cart
[**get_cart**](StoreShoppingCartsApi.md#get_cart) | **GET** /carts/{id} | Returns the cart with the given GUID
[**get_carts**](StoreShoppingCartsApi.md#get_carts) | **GET** /carts | Get a list of carts
[**get_shippable**](StoreShoppingCartsApi.md#get_shippable) | **GET** /carts/{id}/shippable | Returns whether a cart requires shipping
[**get_shipping_countries**](StoreShoppingCartsApi.md#get_shipping_countries) | **GET** /carts/{id}/countries | Get the list of available shipping countries per vendor
[**remove_discount_from_cart**](StoreShoppingCartsApi.md#remove_discount_from_cart) | **DELETE** /carts/{id}/discounts/{code} | Removes a discount coupon from the cart
[**set_cart_currency**](StoreShoppingCartsApi.md#set_cart_currency) | **PUT** /carts/{id}/currency | Sets the currency to use for the cart
[**set_cart_owner**](StoreShoppingCartsApi.md#set_cart_owner) | **PUT** /carts/{id}/owner | Sets the owner of a cart if none is set already
[**update_item_in_cart**](StoreShoppingCartsApi.md#update_item_in_cart) | **PUT** /carts/{id}/items | Changes the quantity of an item already in the cart
[**update_shipping_address**](StoreShoppingCartsApi.md#update_shipping_address) | **PUT** /carts/{id}/shipping-address | Modifies or sets the order shipping address


# **add_custom_discount**
> add_custom_discount(id, custom_discount=custom_discount)

Adds a custom discount to the cart

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart
custom_discount = knetik_cloud.CouponDefinition() # CouponDefinition | The details of the discount to add (optional)

try: 
    # Adds a custom discount to the cart
    api_instance.add_custom_discount(id, custom_discount=custom_discount)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->add_custom_discount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **custom_discount** | [**CouponDefinition**](CouponDefinition.md)| The details of the discount to add | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_discount_to_cart**
> add_discount_to_cart(id, sku_request=sku_request)

Adds a discount coupon to the cart

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart
sku_request = knetik_cloud.SkuRequest() # SkuRequest | The request of the sku (optional)

try: 
    # Adds a discount coupon to the cart
    api_instance.add_discount_to_cart(id, sku_request=sku_request)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->add_discount_to_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **sku_request** | [**SkuRequest**](SkuRequest.md)| The request of the sku | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_item_to_cart**
> add_item_to_cart(id, cart_item_request=cart_item_request)

Add an item to the cart

Currently, carts cannot contain virtual and real currency items at the same time. Furthermore, the API only support a single virtual item at the moment

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart
cart_item_request = knetik_cloud.CartItemRequest() # CartItemRequest | The cart item request object (optional)

try: 
    # Add an item to the cart
    api_instance.add_item_to_cart(id, cart_item_request=cart_item_request)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->add_item_to_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **cart_item_request** | [**CartItemRequest**](CartItemRequest.md)| The cart item request object | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cart**
> str create_cart(owner=owner, currency_code=currency_code)

Create a cart

You don't have to have a user to create a cart but the API requires authentication to checkout

### Example 
```python
from __future__ import print_function
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.StoreShoppingCartsApi()
owner = 56 # int | Set the owner of a cart. If not specified, defaults to the calling user's id. If specified and is not the calling user's id, SHOPPING_CARTS_ADMIN permission is required (optional)
currency_code = 'currency_code_example' # str | Set the currency for the cart, by currency code. May be disallowed by site settings. (optional)

try: 
    # Create a cart
    api_response = api_instance.create_cart(owner=owner, currency_code=currency_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->create_cart: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cart**
> Cart get_cart(id)

Returns the cart with the given GUID

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart

try: 
    # Returns the cart with the given GUID
    api_response = api_instance.get_cart(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->get_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 

### Return type

[**Cart**](Cart.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_carts**
> PageResourceCartSummary get_carts(filter_owner_id=filter_owner_id, size=size, page=page, order=order)

Get a list of carts

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
filter_owner_id = 56 # int | Filter by the id of the owner (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # Get a list of carts
    api_response = api_instance.get_carts(filter_owner_id=filter_owner_id, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->get_carts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_owner_id** | **int**| Filter by the id of the owner | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceCartSummary**](PageResourceCartSummary.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shippable**
> CartShippableResponse get_shippable(id)

Returns whether a cart requires shipping

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart

try: 
    # Returns whether a cart requires shipping
    api_response = api_instance.get_shippable(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->get_shippable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 

### Return type

[**CartShippableResponse**](CartShippableResponse.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_countries**
> SampleCountriesResponse get_shipping_countries(id)

Get the list of available shipping countries per vendor

Since a cart can have multiple vendors with different shipping options, the countries are broken down by vendors. Please see notes about the response object as the fields are variable.

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart

try: 
    # Get the list of available shipping countries per vendor
    api_response = api_instance.get_shipping_countries(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->get_shipping_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 

### Return type

[**SampleCountriesResponse**](SampleCountriesResponse.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_discount_from_cart**
> remove_discount_from_cart(id, code)

Removes a discount coupon from the cart

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart
code = 'code_example' # str | The SKU code of the coupon to remove

try: 
    # Removes a discount coupon from the cart
    api_instance.remove_discount_from_cart(id, code)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->remove_discount_from_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **code** | **str**| The SKU code of the coupon to remove | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cart_currency**
> set_cart_currency(id, currency_code=currency_code)

Sets the currency to use for the cart

May be disallowed by site settings.

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart
currency_code = knetik_cloud.StringWrapper() # StringWrapper | The code of the currency (optional)

try: 
    # Sets the currency to use for the cart
    api_instance.set_cart_currency(id, currency_code=currency_code)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->set_cart_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **currency_code** | [**StringWrapper**](StringWrapper.md)| The code of the currency | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cart_owner**
> set_cart_owner(id, user_id=user_id)

Sets the owner of a cart if none is set already

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart
user_id = knetik_cloud.IntWrapper() # IntWrapper | The id of the user (optional)

try: 
    # Sets the owner of a cart if none is set already
    api_instance.set_cart_owner(id, user_id=user_id)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->set_cart_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **user_id** | [**IntWrapper**](IntWrapper.md)| The id of the user | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item_in_cart**
> update_item_in_cart(id, cart_item_request=cart_item_request)

Changes the quantity of an item already in the cart

A quantity of zero will remove the item from the cart altogether.

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart
cart_item_request = knetik_cloud.CartItemRequest() # CartItemRequest | The cart item request object (optional)

try: 
    # Changes the quantity of an item already in the cart
    api_instance.update_item_in_cart(id, cart_item_request=cart_item_request)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->update_item_in_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **cart_item_request** | [**CartItemRequest**](CartItemRequest.md)| The cart item request object | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipping_address**
> update_shipping_address(id, cart_shipping_address_request=cart_shipping_address_request)

Modifies or sets the order shipping address

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
api_instance = knetik_cloud.StoreShoppingCartsApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the cart
cart_shipping_address_request = knetik_cloud.CartShippingAddressRequest() # CartShippingAddressRequest | The cart shipping address request object (optional)

try: 
    # Modifies or sets the order shipping address
    api_instance.update_shipping_address(id, cart_shipping_address_request=cart_shipping_address_request)
except ApiException as e:
    print("Exception when calling StoreShoppingCartsApi->update_shipping_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the cart | 
 **cart_shipping_address_request** | [**CartShippingAddressRequest**](CartShippingAddressRequest.md)| The cart shipping address request object | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

