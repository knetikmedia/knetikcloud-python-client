# swagger_client.GamificationLevelingApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_level_experience_using_put**](GamificationLevelingApi.md#change_user_level_experience_using_put) | **PUT** /users/{user_id}/leveling/{name} | Update or create a leveling progress record for a user
[**create_level_using_post**](GamificationLevelingApi.md#create_level_using_post) | **POST** /leveling | Create a level schema
[**delete_level_using_delete**](GamificationLevelingApi.md#delete_level_using_delete) | **DELETE** /leveling/{name} | Delete a level
[**get_available_triggers_using_get1**](GamificationLevelingApi.md#get_available_triggers_using_get1) | **GET** /leveling/triggers | Get the list of triggers that can be used to trigger a leveling progress update
[**get_level_using_get**](GamificationLevelingApi.md#get_level_using_get) | **GET** /leveling/{name} | Retrieve a particular level
[**get_levels_using_get**](GamificationLevelingApi.md#get_levels_using_get) | **GET** /leveling | List and search levels
[**get_user_level_using_get**](GamificationLevelingApi.md#get_user_level_using_get) | **GET** /users/{user_id}/leveling/{name} | Get a user&#39;s progress for a given level schema
[**get_user_levels_using_get**](GamificationLevelingApi.md#get_user_levels_using_get) | **GET** /users/{user_id}/leveling | Get a user&#39;s progress for all level schemas
[**update_level_using_put**](GamificationLevelingApi.md#update_level_using_put) | **PUT** /leveling/{name} | Update a level


# **change_user_level_experience_using_put**
> change_user_level_experience_using_put(user_id, name, progress=progress)

Update or create a leveling progress record for a user

If no progress record yet exists for the user, it will be created. Otherwise it will be updated. If progress meets or exceeds the level's max_value it will be marked as earned and a BRE event will be triggered for the <code>BreAchievementEarnedTrigger</code>.

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
api_instance = swagger_client.GamificationLevelingApi()
user_id = 56 # int | The id of the user
name = 'name_example' # str | The level schema name
progress = 56 # int | The current progress amount (optional)

try: 
    # Update or create a leveling progress record for a user
    api_instance.change_user_level_experience_using_put(user_id, name, progress=progress)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->change_user_level_experience_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **name** | **str**| The level schema name | 
 **progress** | **int**| The current progress amount | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_level_using_post**
> LevelingResource create_level_using_post(level=level)

Create a level schema

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
api_instance = swagger_client.GamificationLevelingApi()
level = swagger_client.LevelingResource() # LevelingResource | The level schema definition (optional)

try: 
    # Create a level schema
    api_response = api_instance.create_level_using_post(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->create_level_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**LevelingResource**](LevelingResource.md)| The level schema definition | [optional] 

### Return type

[**LevelingResource**](LevelingResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_level_using_delete**
> delete_level_using_delete(name)

Delete a level

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
api_instance = swagger_client.GamificationLevelingApi()
name = 'name_example' # str | The level schema name

try: 
    # Delete a level
    api_instance.delete_level_using_delete(name)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->delete_level_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The level schema name | 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_triggers_using_get1**
> list[BreTriggerResource] get_available_triggers_using_get1()

Get the list of triggers that can be used to trigger a leveling progress update

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
api_instance = swagger_client.GamificationLevelingApi()

try: 
    # Get the list of triggers that can be used to trigger a leveling progress update
    api_response = api_instance.get_available_triggers_using_get1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_available_triggers_using_get1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BreTriggerResource]**](BreTriggerResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_level_using_get**
> LevelingResource get_level_using_get(name)

Retrieve a particular level

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
api_instance = swagger_client.GamificationLevelingApi()
name = 'name_example' # str | The level schema name

try: 
    # Retrieve a particular level
    api_response = api_instance.get_level_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_level_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The level schema name | 

### Return type

[**LevelingResource**](LevelingResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_levels_using_get**
> PageResourceLevelingResource get_levels_using_get(filter_name=filter_name, size=size, page=page, order=order)

List and search levels

Get a list of levels schemas with optional filtering

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
api_instance = swagger_client.GamificationLevelingApi()
filter_name = 'filter_name_example' # str | Filter for level schemas whose name contains a given string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)

try: 
    # List and search levels
    api_response = api_instance.get_levels_using_get(filter_name=filter_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_levels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| Filter for level schemas whose name contains a given string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to name:ASC]

### Return type

[**PageResourceLevelingResource**](PageResourceLevelingResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_level_using_get**
> UserLevelingResource get_user_level_using_get(user_id, name)

Get a user's progress for a given level schema

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
api_instance = swagger_client.GamificationLevelingApi()
user_id = 56 # int | The id of the user
name = 'name_example' # str | The level schema name

try: 
    # Get a user's progress for a given level schema
    api_response = api_instance.get_user_level_using_get(user_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_user_level_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **name** | **str**| The level schema name | 

### Return type

[**UserLevelingResource**](UserLevelingResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_levels_using_get**
> PageResourceUserLevelingResource get_user_levels_using_get(user_id)

Get a user's progress for all level schemas

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
api_instance = swagger_client.GamificationLevelingApi()
user_id = 56 # int | The id of the user

try: 
    # Get a user's progress for all level schemas
    api_response = api_instance.get_user_levels_using_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_user_levels_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

[**PageResourceUserLevelingResource**](PageResourceUserLevelingResource.md)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_level_using_put**
> update_level_using_put(name, new_level=new_level)

Update a level

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
api_instance = swagger_client.GamificationLevelingApi()
name = 'name_example' # str | The level schema name
new_level = swagger_client.LevelingResource() # LevelingResource | The level schema definition (optional)

try: 
    # Update a level
    api_instance.update_level_using_put(name, new_level=new_level)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->update_level_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The level schema name | 
 **new_level** | [**LevelingResource**](LevelingResource.md)| The level schema definition | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

