# swagger_client.GamificationLevelingApi

All URIs are relative to *https://integration.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_level**](GamificationLevelingApi.md#create_level) | **POST** /leveling | Create a level schema
[**delete_level**](GamificationLevelingApi.md#delete_level) | **DELETE** /leveling/{name} | Delete a level
[**get_level**](GamificationLevelingApi.md#get_level) | **GET** /leveling/{name} | Retrieve a level
[**get_level_triggers**](GamificationLevelingApi.md#get_level_triggers) | **GET** /leveling/triggers | Get the list of triggers that can be used to trigger a leveling progress update
[**get_levels**](GamificationLevelingApi.md#get_levels) | **GET** /leveling | List and search levels
[**get_user_level**](GamificationLevelingApi.md#get_user_level) | **GET** /users/{user_id}/leveling/{name} | Get a user&#39;s progress for a given level schema
[**get_user_levels**](GamificationLevelingApi.md#get_user_levels) | **GET** /users/{user_id}/leveling | Get a user&#39;s progress for all level schemas
[**update_level**](GamificationLevelingApi.md#update_level) | **PUT** /leveling/{name} | Update a level
[**update_user_level**](GamificationLevelingApi.md#update_user_level) | **PUT** /users/{user_id}/leveling/{name} | Update or create a leveling progress record for a user


# **create_level**
> LevelingResource create_level(level=level)

Create a level schema

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
api_instance = swagger_client.GamificationLevelingApi()
level = swagger_client.LevelingResource() # LevelingResource | The level schema definition (optional)

try: 
    # Create a level schema
    api_response = api_instance.create_level(level=level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->create_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | [**LevelingResource**](LevelingResource.md)| The level schema definition | [optional] 

### Return type

[**LevelingResource**](LevelingResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_level**
> delete_level(name)

Delete a level

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
api_instance = swagger_client.GamificationLevelingApi()
name = 'name_example' # str | The level schema name

try: 
    # Delete a level
    api_instance.delete_level(name)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->delete_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The level schema name | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_level**
> LevelingResource get_level(name)

Retrieve a level

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
api_instance = swagger_client.GamificationLevelingApi()
name = 'name_example' # str | The level schema name

try: 
    # Retrieve a level
    api_response = api_instance.get_level(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The level schema name | 

### Return type

[**LevelingResource**](LevelingResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_level_triggers**
> list[BreTriggerResource] get_level_triggers()

Get the list of triggers that can be used to trigger a leveling progress update

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
api_instance = swagger_client.GamificationLevelingApi()

try: 
    # Get the list of triggers that can be used to trigger a leveling progress update
    api_response = api_instance.get_level_triggers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_level_triggers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BreTriggerResource]**](BreTriggerResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_levels**
> PageResourceLevelingResource get_levels(filter_name=filter_name, size=size, page=page, order=order)

List and search levels

Get a list of levels schemas with optional filtering

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
api_instance = swagger_client.GamificationLevelingApi()
filter_name = 'filter_name_example' # str | Filter for level schemas whose name contains a given string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'name:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to name:ASC)

try: 
    # List and search levels
    api_response = api_instance.get_levels(filter_name=filter_name, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_levels: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_level**
> UserLevelingResource get_user_level(user_id, name)

Get a user's progress for a given level schema

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
api_instance = swagger_client.GamificationLevelingApi()
user_id = 56 # int | The id of the user
name = 'name_example' # str | The level schema name

try: 
    # Get a user's progress for a given level schema
    api_response = api_instance.get_user_level(user_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_user_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 
 **name** | **str**| The level schema name | 

### Return type

[**UserLevelingResource**](UserLevelingResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_levels**
> PageResourceUserLevelingResource get_user_levels(user_id)

Get a user's progress for all level schemas

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
api_instance = swagger_client.GamificationLevelingApi()
user_id = 56 # int | The id of the user

try: 
    # Get a user's progress for all level schemas
    api_response = api_instance.get_user_levels(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->get_user_levels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The id of the user | 

### Return type

[**PageResourceUserLevelingResource**](PageResourceUserLevelingResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_level**
> update_level(name, new_level=new_level)

Update a level

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
api_instance = swagger_client.GamificationLevelingApi()
name = 'name_example' # str | The level schema name
new_level = swagger_client.LevelingResource() # LevelingResource | The level schema definition (optional)

try: 
    # Update a level
    api_instance.update_level(name, new_level=new_level)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->update_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The level schema name | 
 **new_level** | [**LevelingResource**](LevelingResource.md)| The level schema definition | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_level**
> update_user_level(user_id, name, progress=progress)

Update or create a leveling progress record for a user

If no progress record yet exists for the user, it will be created. Otherwise it will be updated. If progress meets or exceeds the level's max_value it will be marked as earned and a BRE event will be triggered for the <code>BreAchievementEarnedTrigger</code>.

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
api_instance = swagger_client.GamificationLevelingApi()
user_id = 56 # int | The id of the user
name = 'name_example' # str | The level schema name
progress = 56 # int | The current progress amount (optional)

try: 
    # Update or create a leveling progress record for a user
    api_instance.update_user_level(user_id, name, progress=progress)
except ApiException as e:
    print("Exception when calling GamificationLevelingApi->update_user_level: %s\n" % e)
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

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

