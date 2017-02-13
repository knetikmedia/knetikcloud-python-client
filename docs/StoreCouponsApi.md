# swagger_client.StoreCouponsApi

All URIs are relative to *https://integration.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_coupon_item**](StoreCouponsApi.md#create_coupon_item) | **POST** /store/coupons | Create a coupon item
[**create_coupon_template**](StoreCouponsApi.md#create_coupon_template) | **POST** /store/coupons/templates | Create a coupon template
[**delete_coupon_item**](StoreCouponsApi.md#delete_coupon_item) | **DELETE** /store/coupons/{id} | Delete a coupon item
[**delete_coupon_template**](StoreCouponsApi.md#delete_coupon_template) | **DELETE** /store/coupons/templates/{id} | Delete a coupon template
[**get_coupon_item**](StoreCouponsApi.md#get_coupon_item) | **GET** /store/coupons/{id} | Get a single coupon item
[**get_coupon_template**](StoreCouponsApi.md#get_coupon_template) | **GET** /store/coupons/templates/{id} | Get a single coupon template
[**get_coupon_templates**](StoreCouponsApi.md#get_coupon_templates) | **GET** /store/coupons/templates | List and search coupon templates
[**update_coupon_item**](StoreCouponsApi.md#update_coupon_item) | **PUT** /store/coupons/{id} | Update a coupon item
[**update_coupon_template**](StoreCouponsApi.md#update_coupon_template) | **PUT** /store/coupons/templates/{id} | Update a coupon template


# **create_coupon_item**
> CouponItem create_coupon_item(coupon_item=coupon_item)

Create a coupon item

SKUs have to be unique in the entire store.

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
api_instance = swagger_client.StoreCouponsApi()
coupon_item = swagger_client.CouponItem() # CouponItem | The coupon item object (optional)

try: 
    # Create a coupon item
    api_response = api_instance.create_coupon_item(coupon_item=coupon_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->create_coupon_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_item** | [**CouponItem**](CouponItem.md)| The coupon item object | [optional] 

### Return type

[**CouponItem**](CouponItem.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupon_template**
> ItemTemplateResource create_coupon_template(coupon_template_resource=coupon_template_resource)

Create a coupon template

Coupon Templates define a type of coupon and the properties they have.

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
api_instance = swagger_client.StoreCouponsApi()
coupon_template_resource = swagger_client.ItemTemplateResource() # ItemTemplateResource | The new coupon template (optional)

try: 
    # Create a coupon template
    api_response = api_instance.create_coupon_template(coupon_template_resource=coupon_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->create_coupon_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_template_resource** | [**ItemTemplateResource**](ItemTemplateResource.md)| The new coupon template | [optional] 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_item**
> delete_coupon_item(id)

Delete a coupon item

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
api_instance = swagger_client.StoreCouponsApi()
id = 56 # int | The id of the coupon

try: 
    # Delete a coupon item
    api_instance.delete_coupon_item(id)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->delete_coupon_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the coupon | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_coupon_template**
> delete_coupon_template(id, cascade=cascade)

Delete a coupon template

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
api_instance = swagger_client.StoreCouponsApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | force deleting the template if it's attached to other objects, cascade = detach (optional)

try: 
    # Delete a coupon template
    api_instance.delete_coupon_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->delete_coupon_template: %s\n" % e)
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

# **get_coupon_item**
> CouponItem get_coupon_item(id)

Get a single coupon item

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
api_instance = swagger_client.StoreCouponsApi()
id = 56 # int | The id of the coupon

try: 
    # Get a single coupon item
    api_response = api_instance.get_coupon_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->get_coupon_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the coupon | 

### Return type

[**CouponItem**](CouponItem.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_template**
> ItemTemplateResource get_coupon_template(id)

Get a single coupon template

Coupon Templates define a type of coupon and the properties they have.

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
api_instance = swagger_client.StoreCouponsApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single coupon template
    api_response = api_instance.get_coupon_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->get_coupon_template: %s\n" % e)
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

# **get_coupon_templates**
> PageResourceItemTemplateResource get_coupon_templates(size=size, page=page, order=order)

List and search coupon templates

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
api_instance = swagger_client.StoreCouponsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search coupon templates
    api_response = api_instance.get_coupon_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->get_coupon_templates: %s\n" % e)
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

# **update_coupon_item**
> update_coupon_item(id, coupon_item=coupon_item)

Update a coupon item

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
api_instance = swagger_client.StoreCouponsApi()
id = 56 # int | The id of the coupon
coupon_item = swagger_client.CouponItem() # CouponItem | The coupon item object (optional)

try: 
    # Update a coupon item
    api_instance.update_coupon_item(id, coupon_item=coupon_item)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->update_coupon_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the coupon | 
 **coupon_item** | [**CouponItem**](CouponItem.md)| The coupon item object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coupon_template**
> update_coupon_template(id, coupon_template_resource=coupon_template_resource)

Update a coupon template

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
api_instance = swagger_client.StoreCouponsApi()
id = 'id_example' # str | The id of the template
coupon_template_resource = swagger_client.ItemTemplateResource() # ItemTemplateResource | The coupon template resource object (optional)

try: 
    # Update a coupon template
    api_instance.update_coupon_template(id, coupon_template_resource=coupon_template_resource)
except ApiException as e:
    print("Exception when calling StoreCouponsApi->update_coupon_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **coupon_template_resource** | [**ItemTemplateResource**](ItemTemplateResource.md)| The coupon template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

