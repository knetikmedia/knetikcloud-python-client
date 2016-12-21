# swagger_client.StoreBundlesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bundle_item_using_post**](StoreBundlesApi.md#create_bundle_item_using_post) | **POST** /store/bundles | Create a bundle item
[**create_bundle_template_using_post**](StoreBundlesApi.md#create_bundle_template_using_post) | **POST** /store/bundles/templates | Create a bundle template
[**delete_bundle_template_using_delete**](StoreBundlesApi.md#delete_bundle_template_using_delete) | **DELETE** /store/bundles/templates/{id} | Delete a bundle template
[**delete_store_item_using_delete**](StoreBundlesApi.md#delete_store_item_using_delete) | **DELETE** /store/bundles/{id} | Delete a bundle item
[**get_bundle_template_using_get**](StoreBundlesApi.md#get_bundle_template_using_get) | **GET** /store/bundles/templates/{id} | Get a single bundle template
[**get_bundle_templates_using_get**](StoreBundlesApi.md#get_bundle_templates_using_get) | **GET** /store/bundles/templates | List and search bundle templates
[**get_store_item_using_get**](StoreBundlesApi.md#get_store_item_using_get) | **GET** /store/bundles/{id} | Get a single bundle item
[**update_bundle_item_using_put**](StoreBundlesApi.md#update_bundle_item_using_put) | **PUT** /store/bundles/{id} | Update a bundle item
[**update_bundle_template_using_put**](StoreBundlesApi.md#update_bundle_template_using_put) | **PUT** /store/bundles/templates/{id} | Update a bundle template


# **create_bundle_item_using_post**
> BundleItem create_bundle_item_using_post(bundle_item=bundle_item)

Create a bundle item

The SKU for the bundle itself must be unique and there can only be one SKU.  Extra notes for price_override:  The price of all the items (multiplied by the quantity) must equal the price of the bundle.  With individual prices set, items will be processed individually and can be refunded as such.  However, if all prices are set to null, the price of the bundle will be used and will be treated as one item.

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
api_instance = swagger_client.StoreBundlesApi()
bundle_item = swagger_client.BundleItem() # BundleItem | The bundle item object (optional)

try: 
    # Create a bundle item
    api_response = api_instance.create_bundle_item_using_post(bundle_item=bundle_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->create_bundle_item_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_item** | [**BundleItem**](BundleItem.md)| The bundle item object | [optional] 

### Return type

[**BundleItem**](BundleItem.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bundle_template_using_post**
> ItemTemplateResource create_bundle_template_using_post(bundle_template_resource=bundle_template_resource)

Create a bundle template

Bundle Templates define a type of bundle and the properties they have.

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
api_instance = swagger_client.StoreBundlesApi()
bundle_template_resource = swagger_client.ItemTemplateResource() # ItemTemplateResource | The new bundle template (optional)

try: 
    # Create a bundle template
    api_response = api_instance.create_bundle_template_using_post(bundle_template_resource=bundle_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->create_bundle_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_template_resource** | [**ItemTemplateResource**](ItemTemplateResource.md)| The new bundle template | [optional] 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bundle_template_using_delete**
> delete_bundle_template_using_delete(id, cascade=cascade)

Delete a bundle template

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
api_instance = swagger_client.StoreBundlesApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | force deleting the template if it's attached to other objects, cascade = detach (optional)

try: 
    # Delete a bundle template
    api_instance.delete_bundle_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->delete_bundle_template_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| force deleting the template if it&#39;s attached to other objects, cascade &#x3D; detach | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_store_item_using_delete**
> delete_store_item_using_delete(id)

Delete a bundle item

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
api_instance = swagger_client.StoreBundlesApi()
id = 56 # int | The id of the bundle

try: 
    # Delete a bundle item
    api_instance.delete_store_item_using_delete(id)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->delete_store_item_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the bundle | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_template_using_get**
> ItemTemplateResource get_bundle_template_using_get(id)

Get a single bundle template

Bundle Templates define a type of bundle and the properties they have.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreBundlesApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single bundle template
    api_response = api_instance.get_bundle_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->get_bundle_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_templates_using_get**
> PageResourceItemTemplateResource get_bundle_templates_using_get(size=size, page=page, order=order)

List and search bundle templates

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreBundlesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search bundle templates
    api_response = api_instance.get_bundle_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->get_bundle_templates_using_get: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_store_item_using_get**
> BundleItem get_store_item_using_get(id)

Get a single bundle item

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreBundlesApi()
id = 56 # int | The id of the bundle

try: 
    # Get a single bundle item
    api_response = api_instance.get_store_item_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->get_store_item_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the bundle | 

### Return type

[**BundleItem**](BundleItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bundle_item_using_put**
> update_bundle_item_using_put(id, bundle_item=bundle_item)

Update a bundle item

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
api_instance = swagger_client.StoreBundlesApi()
id = 56 # int | The id of the bundle
bundle_item = swagger_client.BundleItem() # BundleItem | The bundle item object (optional)

try: 
    # Update a bundle item
    api_instance.update_bundle_item_using_put(id, bundle_item=bundle_item)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->update_bundle_item_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the bundle | 
 **bundle_item** | [**BundleItem**](BundleItem.md)| The bundle item object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bundle_template_using_put**
> update_bundle_template_using_put(id, bundle_template_resource=bundle_template_resource)

Update a bundle template

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
api_instance = swagger_client.StoreBundlesApi()
id = 'id_example' # str | The id of the template
bundle_template_resource = swagger_client.ItemTemplateResource() # ItemTemplateResource | The bundle template resource object (optional)

try: 
    # Update a bundle template
    api_instance.update_bundle_template_using_put(id, bundle_template_resource=bundle_template_resource)
except ApiException as e:
    print("Exception when calling StoreBundlesApi->update_bundle_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **bundle_template_resource** | [**ItemTemplateResource**](ItemTemplateResource.md)| The bundle template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
