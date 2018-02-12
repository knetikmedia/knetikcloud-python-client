# knetik_cloud.TaxesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_country_tax**](TaxesApi.md#create_country_tax) | **POST** /tax/countries | Create a country tax
[**create_state_tax**](TaxesApi.md#create_state_tax) | **POST** /tax/countries/{country_code_iso3}/states | Create a state tax
[**delete_country_tax**](TaxesApi.md#delete_country_tax) | **DELETE** /tax/countries/{country_code_iso3} | Delete an existing tax
[**delete_state_tax**](TaxesApi.md#delete_state_tax) | **DELETE** /tax/countries/{country_code_iso3}/states/{state_code} | Delete an existing state tax
[**get_country_tax**](TaxesApi.md#get_country_tax) | **GET** /tax/countries/{country_code_iso3} | Get a single tax
[**get_country_taxes**](TaxesApi.md#get_country_taxes) | **GET** /tax/countries | List and search taxes
[**get_state_tax**](TaxesApi.md#get_state_tax) | **GET** /tax/countries/{country_code_iso3}/states/{state_code} | Get a single state tax
[**get_state_taxes_for_countries**](TaxesApi.md#get_state_taxes_for_countries) | **GET** /tax/states | List and search taxes across all countries
[**get_state_taxes_for_country**](TaxesApi.md#get_state_taxes_for_country) | **GET** /tax/countries/{country_code_iso3}/states | List and search taxes within a country
[**update_country_tax**](TaxesApi.md#update_country_tax) | **PUT** /tax/countries/{country_code_iso3} | Create or update a tax
[**update_state_tax**](TaxesApi.md#update_state_tax) | **PUT** /tax/countries/{country_code_iso3}/states/{state_code} | Create or update a state tax


# **create_country_tax**
> CountryTaxResource create_country_tax(tax_resource=tax_resource)

Create a country tax

<b>Permissions Needed:</b> TAX_ADMIN

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
tax_resource = knetik_cloud.CountryTaxResource() # CountryTaxResource | The tax object (optional)

try: 
    # Create a country tax
    api_response = api_instance.create_country_tax(tax_resource=tax_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->create_country_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_resource** | [**CountryTaxResource**](CountryTaxResource.md)| The tax object | [optional] 

### Return type

[**CountryTaxResource**](CountryTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_state_tax**
> StateTaxResource create_state_tax(country_code_iso3, tax_resource=tax_resource)

Create a state tax

<b>Permissions Needed:</b> TAX_ADMIN

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country
tax_resource = knetik_cloud.StateTaxResource() # StateTaxResource | The tax object (optional)

try: 
    # Create a state tax
    api_response = api_instance.create_state_tax(country_code_iso3, tax_resource=tax_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->create_state_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 
 **tax_resource** | [**StateTaxResource**](StateTaxResource.md)| The tax object | [optional] 

### Return type

[**StateTaxResource**](StateTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_country_tax**
> delete_country_tax(country_code_iso3)

Delete an existing tax

<b>Permissions Needed:</b> TAX_ADMIN

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country

try: 
    # Delete an existing tax
    api_instance.delete_country_tax(country_code_iso3)
except ApiException as e:
    print("Exception when calling TaxesApi->delete_country_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_state_tax**
> delete_state_tax(country_code_iso3, state_code)

Delete an existing state tax

<b>Permissions Needed:</b> TAX_ADMIN

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country
state_code = 'state_code_example' # str | The code of the state

try: 
    # Delete an existing state tax
    api_instance.delete_state_tax(country_code_iso3, state_code)
except ApiException as e:
    print("Exception when calling TaxesApi->delete_state_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 
 **state_code** | **str**| The code of the state | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_tax**
> CountryTaxResource get_country_tax(country_code_iso3)

Get a single tax

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country

try: 
    # Get a single tax
    api_response = api_instance.get_country_tax(country_code_iso3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_country_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 

### Return type

[**CountryTaxResource**](CountryTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_taxes**
> PageResourceCountryTaxResource get_country_taxes(size=size, page=page, order=order)

List and search taxes

<b>Permissions Needed:</b> TAX_ADMIN

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)

try: 
    # List and search taxes
    api_response = api_instance.get_country_taxes(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_country_taxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to name:ASC]

### Return type

[**PageResourceCountryTaxResource**](PageResourceCountryTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_tax**
> StateTaxResource get_state_tax(country_code_iso3, state_code)

Get a single state tax

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country
state_code = 'state_code_example' # str | The code of the state

try: 
    # Get a single state tax
    api_response = api_instance.get_state_tax(country_code_iso3, state_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_state_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 
 **state_code** | **str**| The code of the state | 

### Return type

[**StateTaxResource**](StateTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_taxes_for_countries**
> PageResourceStateTaxResource get_state_taxes_for_countries(size=size, page=page, order=order)

List and search taxes across all countries

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # List and search taxes across all countries
    api_response = api_instance.get_state_taxes_for_countries(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_state_taxes_for_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceStateTaxResource**](PageResourceStateTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_state_taxes_for_country**
> PageResourceStateTaxResource get_state_taxes_for_country(country_code_iso3, size=size, page=page, order=order)

List and search taxes within a country

<b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned (optional) (default to 1)
order = 'order_example' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional)

try: 
    # List and search taxes within a country
    api_response = api_instance.get_state_taxes_for_country(country_code_iso3, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_state_taxes_for_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] 

### Return type

[**PageResourceStateTaxResource**](PageResourceStateTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_country_tax**
> CountryTaxResource update_country_tax(country_code_iso3, tax_resource=tax_resource)

Create or update a tax

<b>Permissions Needed:</b> TAX_ADMIN

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country
tax_resource = knetik_cloud.CountryTaxResource() # CountryTaxResource | The tax object (optional)

try: 
    # Create or update a tax
    api_response = api_instance.update_country_tax(country_code_iso3, tax_resource=tax_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->update_country_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 
 **tax_resource** | [**CountryTaxResource**](CountryTaxResource.md)| The tax object | [optional] 

### Return type

[**CountryTaxResource**](CountryTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_state_tax**
> StateTaxResource update_state_tax(country_code_iso3, state_code, tax_resource=tax_resource)

Create or update a state tax

<b>Permissions Needed:</b> TAX_ADMIN

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
api_instance = knetik_cloud.TaxesApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country
state_code = 'state_code_example' # str | The code of the state
tax_resource = knetik_cloud.StateTaxResource() # StateTaxResource | The tax object (optional)

try: 
    # Create or update a state tax
    api_response = api_instance.update_state_tax(country_code_iso3, state_code, tax_resource=tax_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->update_state_tax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 
 **state_code** | **str**| The code of the state | 
 **tax_resource** | [**StateTaxResource**](StateTaxResource.md)| The tax object | [optional] 

### Return type

[**StateTaxResource**](StateTaxResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

