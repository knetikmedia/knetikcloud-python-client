# knetik_cloud.StoreSalesApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_catalog_sale**](StoreSalesApi.md#create_catalog_sale) | **POST** /store/sales | Create a sale
[**delete_catalog_sale**](StoreSalesApi.md#delete_catalog_sale) | **DELETE** /store/sales/{id} | Delete a sale
[**get_catalog_sale**](StoreSalesApi.md#get_catalog_sale) | **GET** /store/sales/{id} | Get a single sale
[**get_catalog_sales**](StoreSalesApi.md#get_catalog_sales) | **GET** /store/sales | List and search sales
[**update_catalog_sale**](StoreSalesApi.md#update_catalog_sale) | **PUT** /store/sales/{id} | Update a sale


# **create_catalog_sale**
> CatalogSale create_catalog_sale(catalog_sale=catalog_sale)

Create a sale

<b>Permissions Needed:</b> SALES_ADMIN

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
api_instance = knetik_cloud.StoreSalesApi(knetik_cloud.ApiClient(configuration))
catalog_sale = knetik_cloud.CatalogSale() # CatalogSale | The catalog sale object (optional)

try: 
    # Create a sale
    api_response = api_instance.create_catalog_sale(catalog_sale=catalog_sale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSalesApi->create_catalog_sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_sale** | [**CatalogSale**](CatalogSale.md)| The catalog sale object | [optional] 

### Return type

[**CatalogSale**](CatalogSale.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_catalog_sale**
> delete_catalog_sale(id)

Delete a sale

<b>Permissions Needed:</b> SALES_ADMIN

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
api_instance = knetik_cloud.StoreSalesApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the sale

try: 
    # Delete a sale
    api_instance.delete_catalog_sale(id)
except ApiException as e:
    print("Exception when calling StoreSalesApi->delete_catalog_sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the sale | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_sale**
> CatalogSale get_catalog_sale(id)

Get a single sale

<b>Permissions Needed:</b> SALES_USER or SALES_ADMIN

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
api_instance = knetik_cloud.StoreSalesApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the sale

try: 
    # Get a single sale
    api_response = api_instance.get_catalog_sale(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSalesApi->get_catalog_sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the sale | 

### Return type

[**CatalogSale**](CatalogSale.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_sales**
> PageResourceCatalogSale get_catalog_sales(size=size, page=page, order=order)

List and search sales

<b>Permissions Needed:</b> SALES_USER or SALES_ADMIN

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
api_instance = knetik_cloud.StoreSalesApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search sales
    api_response = api_instance.get_catalog_sales(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSalesApi->get_catalog_sales: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceCatalogSale**](PageResourceCatalogSale.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_sale**
> CatalogSale update_catalog_sale(id, catalog_sale=catalog_sale)

Update a sale

<b>Permissions Needed:</b> SALES_ADMIN

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
api_instance = knetik_cloud.StoreSalesApi(knetik_cloud.ApiClient(configuration))
id = 56 # int | The id of the sale
catalog_sale = knetik_cloud.CatalogSale() # CatalogSale | The catalog sale object (optional)

try: 
    # Update a sale
    api_response = api_instance.update_catalog_sale(id, catalog_sale=catalog_sale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSalesApi->update_catalog_sale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the sale | 
 **catalog_sale** | [**CatalogSale**](CatalogSale.md)| The catalog sale object | [optional] 

### Return type

[**CatalogSale**](CatalogSale.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

