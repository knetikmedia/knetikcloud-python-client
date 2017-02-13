# swagger_client.StoreShippingApi

All URIs are relative to *https://integration.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_item**](StoreShippingApi.md#create_shipping_item) | **POST** /store/shipping | Create a shipping item
[**create_shipping_template**](StoreShippingApi.md#create_shipping_template) | **POST** /store/shipping/templates | Create a shipping template
[**delete_shipping_item**](StoreShippingApi.md#delete_shipping_item) | **DELETE** /store/shipping/{id} | Delete a shipping item
[**delete_shipping_template**](StoreShippingApi.md#delete_shipping_template) | **DELETE** /store/shipping/templates/{id} | Delete a shipping template
[**get_shipping_item**](StoreShippingApi.md#get_shipping_item) | **GET** /store/shipping/{id} | Get a single shipping item
[**get_shipping_template**](StoreShippingApi.md#get_shipping_template) | **GET** /store/shipping/templates/{id} | Get a single shipping template
[**get_shipping_templates**](StoreShippingApi.md#get_shipping_templates) | **GET** /store/shipping/templates | List and search shipping templates
[**update_shipping_item**](StoreShippingApi.md#update_shipping_item) | **PUT** /store/shipping/{id} | Update a shipping item
[**update_shipping_template**](StoreShippingApi.md#update_shipping_template) | **PUT** /store/shipping/templates/{id} | Update a shipping template


# **create_shipping_item**
> ShippingItem create_shipping_item(shipping_item=shipping_item)

Create a shipping item

A shipping item represents a shipping option and cost. SKUs have to be unique in the entire store.

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
api_instance = swagger_client.StoreShippingApi()
shipping_item = swagger_client.ShippingItem() # ShippingItem | The shipping item object (optional)

try: 
    # Create a shipping item
    api_response = api_instance.create_shipping_item(shipping_item=shipping_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShippingApi->create_shipping_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_item** | [**ShippingItem**](ShippingItem.md)| The shipping item object | [optional] 

### Return type

[**ShippingItem**](ShippingItem.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shipping_template**
> ItemTemplateResource create_shipping_template(shipping_template_resource=shipping_template_resource)

Create a shipping template

Shipping Templates define a type of shipping and the properties they have.

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
api_instance = swagger_client.StoreShippingApi()
shipping_template_resource = swagger_client.ItemTemplateResource() # ItemTemplateResource | The new shipping template (optional)

try: 
    # Create a shipping template
    api_response = api_instance.create_shipping_template(shipping_template_resource=shipping_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShippingApi->create_shipping_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_template_resource** | [**ItemTemplateResource**](ItemTemplateResource.md)| The new shipping template | [optional] 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shipping_item**
> delete_shipping_item(id)

Delete a shipping item

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
api_instance = swagger_client.StoreShippingApi()
id = 56 # int | The id of the shipping item

try: 
    # Delete a shipping item
    api_instance.delete_shipping_item(id)
except ApiException as e:
    print("Exception when calling StoreShippingApi->delete_shipping_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the shipping item | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shipping_template**
> delete_shipping_template(id, cascade=cascade)

Delete a shipping template

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
api_instance = swagger_client.StoreShippingApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | force deleting the template if it's attached to other objects, cascade = detach (optional)

try: 
    # Delete a shipping template
    api_instance.delete_shipping_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling StoreShippingApi->delete_shipping_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| force deleting the template if it&#39;s attached to other objects, cascade &#x3D; detach | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_item**
> ShippingItem get_shipping_item(id)

Get a single shipping item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreShippingApi()
id = 56 # int | The id of the shipping item

try: 
    # Get a single shipping item
    api_response = api_instance.get_shipping_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShippingApi->get_shipping_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the shipping item | 

### Return type

[**ShippingItem**](ShippingItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_template**
> ItemTemplateResource get_shipping_template(id)

Get a single shipping template

Shipping Templates define a type of shipping and the properties they have.

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
api_instance = swagger_client.StoreShippingApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single shipping template
    api_response = api_instance.get_shipping_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShippingApi->get_shipping_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_templates**
> PageResourceItemTemplateResource get_shipping_templates(size=size, page=page, order=order)

List and search shipping templates

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
api_instance = swagger_client.StoreShippingApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search shipping templates
    api_response = api_instance.get_shipping_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreShippingApi->get_shipping_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceItemTemplateResource**](PageResourceItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipping_item**
> update_shipping_item(id, shipping_item=shipping_item)

Update a shipping item

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
api_instance = swagger_client.StoreShippingApi()
id = 56 # int | The id of the shipping item
shipping_item = swagger_client.ShippingItem() # ShippingItem | The shipping item object (optional)

try: 
    # Update a shipping item
    api_instance.update_shipping_item(id, shipping_item=shipping_item)
except ApiException as e:
    print("Exception when calling StoreShippingApi->update_shipping_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the shipping item | 
 **shipping_item** | [**ShippingItem**](ShippingItem.md)| The shipping item object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipping_template**
> update_shipping_template(id, shipping_template_resource=shipping_template_resource)

Update a shipping template

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
api_instance = swagger_client.StoreShippingApi()
id = 'id_example' # str | The id of the template
shipping_template_resource = swagger_client.ItemTemplateResource() # ItemTemplateResource | The shipping template resource object (optional)

try: 
    # Update a shipping template
    api_instance.update_shipping_template(id, shipping_template_resource=shipping_template_resource)
except ApiException as e:
    print("Exception when calling StoreShippingApi->update_shipping_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **shipping_template_resource** | [**ItemTemplateResource**](ItemTemplateResource.md)| The shipping template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

