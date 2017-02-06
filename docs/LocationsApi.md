# swagger_client.LocationsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cities**](LocationsApi.md#get_cities) | **GET** /location/countries/{country_code_iso3}/states/{state_code}/cities | Get a list of a state&#39;s cities
[**get_countries1**](LocationsApi.md#get_countries1) | **GET** /location/countries | Get a list of countries
[**get_countries2**](LocationsApi.md#get_countries2) | **GET** /location/countries/{country_code_iso3}/states | Get a list of a country&#39;s states
[**get_country_by_geo_location**](LocationsApi.md#get_country_by_geo_location) | **GET** /location/geolocation/country | Get the iso3 code of your country
[**get_currency_by_geo_location**](LocationsApi.md#get_currency_by_geo_location) | **GET** /location/geolocation/currency | Get the currency information of your country


# **get_cities**
> list[CityResource] get_cities(country_code_iso3, state_code)

Get a list of a state's cities

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationsApi()
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country
state_code = 'state_code_example' # str | The code of the state

try: 
    # Get a list of a state's cities
    api_response = api_instance.get_cities(country_code_iso3, state_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_cities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 
 **state_code** | **str**| The code of the state | 

### Return type

[**list[CityResource]**](CityResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries1**
> list[CountryResource] get_countries1()

Get a list of countries

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationsApi()

try: 
    # Get a list of countries
    api_response = api_instance.get_countries1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_countries1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CountryResource]**](CountryResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries2**
> list[StateResource] get_countries2(country_code_iso3)

Get a list of a country's states

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationsApi()
country_code_iso3 = 'country_code_iso3_example' # str | The iso3 code of the country

try: 
    # Get a list of a country's states
    api_response = api_instance.get_countries2(country_code_iso3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_countries2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code_iso3** | **str**| The iso3 code of the country | 

### Return type

[**list[StateResource]**](StateResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_by_geo_location**
> str get_country_by_geo_location()

Get the iso3 code of your country

Determined by geo ip location

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationsApi()

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_by_geo_location**
> CurrencyResource get_currency_by_geo_location()

Get the currency information of your country

Determined by geo ip location, currency to country mapping and a fallback setting

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationsApi()

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

