# swagger_client.CampaignsApi

All URIs are relative to *https://localhost:8080/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_challenges_using_post**](CampaignsApi.md#add_challenges_using_post) | **POST** /campaigns/{id}/challenges | Add a challenge to a campaign
[**create_campaign_template_using_post**](CampaignsApi.md#create_campaign_template_using_post) | **POST** /campaigns/templates | Create a campaign template
[**create_campaign_using_post**](CampaignsApi.md#create_campaign_using_post) | **POST** /campaigns | Create a campaign
[**delete_campaign_template_using_delete**](CampaignsApi.md#delete_campaign_template_using_delete) | **DELETE** /campaigns/templates/{id} | Delete a campaign template
[**delete_campaign_using_delete**](CampaignsApi.md#delete_campaign_using_delete) | **DELETE** /campaigns/{id} | Delete a campaign
[**get_campaign_template_using_get**](CampaignsApi.md#get_campaign_template_using_get) | **GET** /campaigns/templates/{id} | Get a single campaign template
[**get_campaign_templates_using_get**](CampaignsApi.md#get_campaign_templates_using_get) | **GET** /campaigns/templates | List and search campaign templates
[**get_campaign_using_get**](CampaignsApi.md#get_campaign_using_get) | **GET** /campaigns/{id} | Returns a single campaign
[**get_campaigns_using_get**](CampaignsApi.md#get_campaigns_using_get) | **GET** /campaigns | List and search campaigns
[**get_challenges_using_get**](CampaignsApi.md#get_challenges_using_get) | **GET** /campaigns/{id}/challenges | List the challenges associated with a campaign
[**remove_challenge_using_delete**](CampaignsApi.md#remove_challenge_using_delete) | **DELETE** /campaigns/{campaign_id}/challenges/{id} | Remove a challenge from a campaign
[**update_campaign_template_using_put**](CampaignsApi.md#update_campaign_template_using_put) | **PUT** /campaigns/templates/{id} | Update an campaign template
[**update_campaign_using_put**](CampaignsApi.md#update_campaign_using_put) | **PUT** /campaigns/{id} | Update a campaign


# **add_challenges_using_post**
> add_challenges_using_post(id, challenge_id=challenge_id)

Add a challenge to a campaign

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
api_instance = swagger_client.CampaignsApi()
id = 789 # int | The id of the campaign
challenge_id = 789 # int | The id of the challenge (optional)

try: 
    # Add a challenge to a campaign
    api_instance.add_challenges_using_post(id, challenge_id=challenge_id)
except ApiException as e:
    print("Exception when calling CampaignsApi->add_challenges_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the campaign | 
 **challenge_id** | **int**| The id of the challenge | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign_template_using_post**
> TemplateResource create_campaign_template_using_post(campaign_template_resource=campaign_template_resource)

Create a campaign template

Campaign Templates define a type of campaign and the properties they have

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
api_instance = swagger_client.CampaignsApi()
campaign_template_resource = swagger_client.TemplateResource() # TemplateResource | The campaign template resource object (optional)

try: 
    # Create a campaign template
    api_response = api_instance.create_campaign_template_using_post(campaign_template_resource=campaign_template_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->create_campaign_template_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_template_resource** | [**TemplateResource**](TemplateResource.md)| The campaign template resource object | [optional] 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_campaign_using_post**
> CampaignResource create_campaign_using_post(campaign_resource=campaign_resource)

Create a campaign

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
api_instance = swagger_client.CampaignsApi()
campaign_resource = swagger_client.CampaignResource() # CampaignResource | The campaign resource object (optional)

try: 
    # Create a campaign
    api_response = api_instance.create_campaign_using_post(campaign_resource=campaign_resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->create_campaign_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_resource** | [**CampaignResource**](CampaignResource.md)| The campaign resource object | [optional] 

### Return type

[**CampaignResource**](CampaignResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_template_using_delete**
> delete_campaign_template_using_delete(id, cascade=cascade)

Delete a campaign template

If cascade = 'detach', it will force delete the template even if it's attached to other objects

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
api_instance = swagger_client.CampaignsApi()
id = 'id_example' # str | The id of the template
cascade = 'cascade_example' # str | The value needed to delete used templates (optional)

try: 
    # Delete a campaign template
    api_instance.delete_campaign_template_using_delete(id, cascade=cascade)
except ApiException as e:
    print("Exception when calling CampaignsApi->delete_campaign_template_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **cascade** | **str**| The value needed to delete used templates | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign_using_delete**
> delete_campaign_using_delete(id)

Delete a campaign

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
api_instance = swagger_client.CampaignsApi()
id = 789 # int | The campaign id

try: 
    # Delete a campaign
    api_instance.delete_campaign_using_delete(id)
except ApiException as e:
    print("Exception when calling CampaignsApi->delete_campaign_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The campaign id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_template_using_get**
> TemplateResource get_campaign_template_using_get(id)

Get a single campaign template

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
api_instance = swagger_client.CampaignsApi()
id = 'id_example' # str | The id of the template

try: 
    # Get a single campaign template
    api_response = api_instance.get_campaign_template_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaign_template_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 

### Return type

[**TemplateResource**](TemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_templates_using_get**
> PageResourceTemplateResource get_campaign_templates_using_get(size=size, page=page, order=order)

List and search campaign templates

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
api_instance = swagger_client.CampaignsApi()
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search campaign templates
    api_response = api_instance.get_campaign_templates_using_get(size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaign_templates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceTemplateResource**](PageResourceTemplateResource.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_using_get**
> CampaignResource get_campaign_using_get(id)

Returns a single campaign

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsApi()
id = 789 # int | The campaign id

try: 
    # Returns a single campaign
    api_response = api_instance.get_campaign_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaign_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The campaign id | 

### Return type

[**CampaignResource**](CampaignResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaigns_using_get**
> PageResourceCampaignResource get_campaigns_using_get(filter_active=filter_active, size=size, page=page, order=order)

List and search campaigns

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsApi()
filter_active = true # bool | Filter for campaigns that are active (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)
order = 'id:ASC' # str | A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] (optional) (default to id:ASC)

try: 
    # List and search campaigns
    api_response = api_instance.get_campaigns_using_get(filter_active=filter_active, size=size, page=page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_campaigns_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_active** | **bool**| Filter for campaigns that are active | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]
 **order** | **str**| A comma separated list of sorting requirements in priority order, each entry matching PROPERTY_NAME:[ASC|DESC] | [optional] [default to id:ASC]

### Return type

[**PageResourceCampaignResource**](PageResourceCampaignResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_challenges_using_get**
> PageResourceChallengeResource get_challenges_using_get(id)

List the challenges associated with a campaign

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CampaignsApi()
id = 789 # int | The campaign id

try: 
    # List the challenges associated with a campaign
    api_response = api_instance.get_challenges_using_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->get_challenges_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The campaign id | 

### Return type

[**PageResourceChallengeResource**](PageResourceChallengeResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_challenge_using_delete**
> remove_challenge_using_delete(campaign_id, id)

Remove a challenge from a campaign

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
api_instance = swagger_client.CampaignsApi()
campaign_id = 789 # int | The campaign id
id = 789 # int | The challenge id

try: 
    # Remove a challenge from a campaign
    api_instance.remove_challenge_using_delete(campaign_id, id)
except ApiException as e:
    print("Exception when calling CampaignsApi->remove_challenge_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **int**| The campaign id | 
 **id** | **int**| The challenge id | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_template_using_put**
> update_campaign_template_using_put(id, campaign_template_resource=campaign_template_resource)

Update an campaign template

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
api_instance = swagger_client.CampaignsApi()
id = 'id_example' # str | The id of the template
campaign_template_resource = swagger_client.TemplateResource() # TemplateResource | The campaign template resource object (optional)

try: 
    # Update an campaign template
    api_instance.update_campaign_template_using_put(id, campaign_template_resource=campaign_template_resource)
except ApiException as e:
    print("Exception when calling CampaignsApi->update_campaign_template_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template | 
 **campaign_template_resource** | [**TemplateResource**](TemplateResource.md)| The campaign template resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign_using_put**
> update_campaign_using_put(id, campaign_resource=campaign_resource)

Update a campaign

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
api_instance = swagger_client.CampaignsApi()
id = 789 # int | The campaign id
campaign_resource = swagger_client.CampaignResource() # CampaignResource | The campaign resource object (optional)

try: 
    # Update a campaign
    api_instance.update_campaign_using_put(id, campaign_resource=campaign_resource)
except ApiException as e:
    print("Exception when calling CampaignsApi->update_campaign_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The campaign id | 
 **campaign_resource** | [**CampaignResource**](CampaignResource.md)| The campaign resource object | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

