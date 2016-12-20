# swagger_client.LocationsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cities_using_get**](LocationsApi.md#cities_using_get) | **GET** /location/countries/{country_code_iso3}/states/{state_code}/cities | Get a list of a state&#39;s cities
[**countries_using_get**](LocationsApi.md#countries_using_get) | **GET** /location/countries | Get a list of countries
[**get_currency_by_geo_location_using_get**](LocationsApi.md#get_currency_by_geo_location_using_get) | **GET** /location/geolocation/currency | Get the currency information of your country
[**get_geo_location_country_using_get**](LocationsApi.md#get_geo_location_country_using_get) | **GET** /location/geolocation/country | Get the iso3 code of your country
[**states_using_get**](LocationsApi.md#states_using_get) | **GET** /location/countries/{country_code_iso3}/states | Get a list of a country&#39;s states


# **cities_using_get**
> list[CityResource] cities_using_get(country_code_iso3, state_code)

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
    api_response = api_instance.cities_using_get(country_code_iso3, state_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->cities_using_get: %s\n" % e)
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

# **countries_using_get**
> list[CountryResource] countries_using_get()

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
    api_response = api_instance.countries_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->countries_using_get: %s\n" % e)
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

# **get_currency_by_geo_location_using_get**
> CurrencyResource get_currency_by_geo_location_using_get()

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
    api_response = api_instance.get_currency_by_geo_location_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_currency_by_geo_location_using_get: %s\n" % e)
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

# **get_geo_location_country_using_get**
> str get_geo_location_country_using_get()

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
    api_response = api_instance.get_geo_location_country_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_geo_location_country_using_get: %s\n" % e)
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

# **states_using_get**
> list[StateResource] states_using_get(country_code_iso3)

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
    api_response = api_instance.states_using_get(country_code_iso3)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->states_using_get: %s\n" % e)
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

