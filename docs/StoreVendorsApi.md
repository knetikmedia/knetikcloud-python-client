# knetik_cloud.StoreVendorsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vendor**](StoreVendorsApi.md#create_vendor) | **POST** /vendors | Create a vendor
[**create_vendor_template**](StoreVendorsApi.md#create_vendor_template) | **POST** /vendors/templates | Create a vendor template
[**delete_vendor**](StoreVendorsApi.md#delete_vendor) | **DELETE** /vendors/{id} | Delete a vendor
[**delete_vendor_template**](StoreVendorsApi.md#delete_vendor_template) | **DELETE** /vendors/templates/{id} | Delete a vendor template
[**get_vendor**](StoreVendorsApi.md#get_vendor) | **GET** /vendors/{id} | Get a single vendor
[**get_vendor_template**](StoreVendorsApi.md#get_vendor_template) | **GET** /vendors/templates/{id} | Get a single vendor template
[**get_vendor_templates**](StoreVendorsApi.md#get_vendor_templates) | **GET** /vendors/templates | List and search vendor templates
[**get_vendors**](StoreVendorsApi.md#get_vendors) | **GET** /vendors | List and search vendors
[**update_vendor**](StoreVendorsApi.md#update_vendor) | **PUT** /vendors/{id} | Update a vendor
[**update_vendor_template**](StoreVendorsApi.md#update_vendor_template) | **PUT** /vendors/templates/{id} | Update a vendor template


# **create_vendor**
> VendorResource create_vendor(vendor=vendor)

Create a vendor

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
vendor = knetik_cloud.VendorResource() # VendorResource | The vendor (optional)

try: 
    # Create a vendor
    api_response = api_instance.create_vendor(vendor=vendor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->create_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor** | [**VendorResource**](VendorResource.md)| The vendor | [optional] 

### Return type

[**VendorResource**](VendorResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vendor_template**
> ItemTemplateResource create_vendor_template(vendor_template_resource=vendor_template_resource)

Create a vendor template

Vendor Templates define a type of vendor and the properties they have.

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
vendor_template_resource = knetik_cloud.ItemTemplateResource() # ItemTemplateResource | The new vendor template (optional)

try: 
    # Create a vendor template
    api_response = api_instance.create_vendor_template(vendor_template_resource=vendor_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->create_vendor_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_template_resource** | [**ItemTemplateResource**](ItemTemplateResource.md)| The new vendor template | [optional] 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor**
> delete_vendor(id)

Delete a vendor

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
id = 56 # int | The id of the vendor

try: 
    # Delete a vendor
    api_instance.delete_vendor(id)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->delete_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the vendor | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vendor_template**
> delete_vendor_template(id, cascade=cascade)

Delete a vendor template

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | force deleting the template if it's attached to other objects, cascade = detach (optional)

try: 
    # Delete a vendor template
    api_instance.delete_vendor_template(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->delete_vendor_template: %s\n" % e)
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

# **get_vendor**
> VendorResource get_vendor(id)

Get a single vendor

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
id = 56 # int | The id of the vendor

try: 
    # Get a single vendor
    api_response = api_instance.get_vendor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->get_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the vendor | 

### Return type

[**VendorResource**](VendorResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_template**
> ItemTemplateResource get_vendor_template(id)

Get a single vendor template

Vendor Templates define a type of vendor and the properties they have.

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single vendor template
    api_response = api_instance.get_vendor_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->get_vendor_template: %s\n" % e)
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

# **get_vendor_templates**
> PageResourceItemTemplateResource get_vendor_templates(size=size, page=page, order=order)

List and search vendor templates

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = '1' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to 1)

try: 
    # List and search vendor templates
    api_response = api_instance.get_vendor_templates(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->get_vendor_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to 1]

### Return type

[**PageResourceItemTemplateResource**](PageResourceItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendors**
> PageResourceVendorResource get_vendors(filter_name=filter_name, size=size, page=page, order=order)

List and search vendors

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
filter_name = 'filter_name_example' # str | Filters vendors by name starting with the text provided in the filter (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search vendors
    api_response = api_instance.get_vendors(filter_name=filter_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->get_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| Filters vendors by name starting with the text provided in the filter | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceVendorResource**](PageResourceVendorResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vendor**
> VendorResource update_vendor(id, vendor=vendor)

Update a vendor

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
id = 56 # int | The id of the vendor
vendor = knetik_cloud.VendorResource() # VendorResource | The vendor (optional)

try: 
    # Update a vendor
    api_response = api_instance.update_vendor(id, vendor=vendor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->update_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the vendor | 
 **vendor** | [**VendorResource**](VendorResource.md)| The vendor | [optional] 

### Return type

[**VendorResource**](VendorResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vendor_template**
> ItemTemplateResource update_vendor_template(id, vendor_template_resource=vendor_template_resource)

Update a vendor template

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.StoreVendorsApi()
id = 'id_example' # str | The id of the template
vendor_template_resource = knetik_cloud.ItemTemplateResource() # ItemTemplateResource | The vendor template resource object (optional)

try: 
    # Update a vendor template
    api_response = api_instance.update_vendor_template(id, vendor_template_resource=vendor_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreVendorsApi->update_vendor_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **vendor_template_resource** | [**ItemTemplateResource**](ItemTemplateResource.md)| The vendor template resource object | [optional] 

### Return type

[**ItemTemplateResource**](ItemTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

