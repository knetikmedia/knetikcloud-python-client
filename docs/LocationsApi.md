# knetik_cloud.LocationsApi

All URIs are relative to *https://jsapi-integration.us-east-1.elasticbeanstalk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](LocationsApi.md#get_countries) | **GET** /location/countries | Get a list of countries
[**get_country_by_geo_location**](LocationsApi.md#get_country_by_geo_location) | **GET** /location/geolocation/country | Get the iso3 code of your country
[**get_country_states**](LocationsApi.md#get_country_states) | **GET** /location/countries/{country_code_iso3}/states | Get a list of a country&#39;s states
[**get_currency_by_geo_location**](LocationsApi.md#get_currency_by_geo_location) | **GET** /location/geolocation/currency | Get the currency information of your country


# **get_countries**
> list[CountryResource] get_countries()

Get a list of countries

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
api_instance = knetik_cloud.LocationsApi(knetik_cloud.ApiClient(configuration))

try: 
    # Get a list of countries
    api_response = api_instance.get_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CountryResource]**](CountryResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_by_geo_location**
> str get_country_by_geo_location()

Get the iso3 code of your country

Determined by geo ip location. <br><br><b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.LocationsApi(knetik_cloud.ApiClient(configuration))

try: 
    # Get the iso3 code of your country
    api_response = api_instance.get_country_by_geo_location()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_country_by_geo_location: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_states**
> list[StateResource] get_country_states(country_code_iso3)

Get a list of a country's states

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
api_instance = knetik_cloud.LocationsApi(knetik_cloud.ApiClient(configuration))
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country

try: 
    # Get a list of a country's states
    api_response = api_instance.get_country_states(country_code_iso3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_country_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 

### Return type

[**list[StateResource]**](StateResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_by_geo_location**
> CurrencyResource get_currency_by_geo_location()

Get the currency information of your country

Determined by geo ip location, currency to country mapping and a fallback setting. <br><br><b>Permissions Needed:</b> ANY

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
api_instance = knetik_cloud.LocationsApi(knetik_cloud.ApiClient(configuration))

try: 
    # Get the currency information of your country
    api_response = api_instance.get_currency_by_geo_location()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_currency_by_geo_location: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrencyResource**](CurrencyResource.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

