# swagger_client.StoreSalesApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_catalog_sale_using_post**](StoreSalesApi.md#create_catalog_sale_using_post) | **POST** /store/sales | Create a sale
[**delete_catalog_sale_using_delete**](StoreSalesApi.md#delete_catalog_sale_using_delete) | **DELETE** /store/sales/{id} | Delete a sale
[**get_catalog_sale_using_get**](StoreSalesApi.md#get_catalog_sale_using_get) | **GET** /store/sales/{id} | Get a single sale
[**get_catalog_sales_using_get**](StoreSalesApi.md#get_catalog_sales_using_get) | **GET** /store/sales | List and search sales
[**update_catalog_sale_using_put**](StoreSalesApi.md#update_catalog_sale_using_put) | **PUT** /store/sales/{id} | Update a sale


# **create_catalog_sale_using_post**
> CatalogSale create_catalog_sale_using_post(catalog_sale=catalog_sale)

Create a sale

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
api_instance = swagger_client.StoreSalesApi()
catalog_sale = swagger_client.CatalogSale() # CatalogSale | The catalog sale object (optional)

try: 
    # Create a sale
    api_response = api_instance.create_catalog_sale_using_post(catalog_sale=catalog_sale)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSalesApi->create_catalog_sale_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_sale** | [**CatalogSale**](CatalogSale.md)| The catalog sale object | [optional] 

### Return type

[**CatalogSale**](CatalogSale.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_catalog_sale_using_delete**
> delete_catalog_sale_using_delete(id)

Delete a sale

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
api_instance = swagger_client.StoreSalesApi()
id = 56 # int | The id of the sale

try: 
    # Delete a sale
    api_instance.delete_catalog_sale_using_delete(id)
except ApiException as e:
    print("Exception when calling StoreSalesApi->delete_catalog_sale_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the sale | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_sale_using_get**
> CatalogSale get_catalog_sale_using_get(id)

Get a single sale

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
api_instance = swagger_client.StoreSalesApi()
id = 56 # int | The id of the sale

try: 
    # Get a single sale
    api_response = api_instance.get_catalog_sale_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSalesApi->get_catalog_sale_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the sale | 

### Return type

[**CatalogSale**](CatalogSale.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_sales_using_get**
> PageResourceCatalogSale get_catalog_sales_using_get(size=size, page=page, order=order)

List and search sales

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
api_instance = swagger_client.StoreSalesApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search sales
    api_response = api_instance.get_catalog_sales_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreSalesApi->get_catalog_sales_using_get: %s\n" % e)
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

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_sale_using_put**
> update_catalog_sale_using_put(id, catalog_sale=catalog_sale)

Update a sale

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
api_instance = swagger_client.StoreSalesApi()
id = 56 # int | The id of the sale
catalog_sale = swagger_client.CatalogSale() # CatalogSale | The catalog sale object (optional)

try: 
    # Update a sale
    api_instance.update_catalog_sale_using_put(id, catalog_sale=catalog_sale)
except ApiException as e:
    print("Exception when calling StoreSalesApi->update_catalog_sale_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the sale | 
 **catalog_sale** | [**CatalogSale**](CatalogSale.md)| The catalog sale object | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

