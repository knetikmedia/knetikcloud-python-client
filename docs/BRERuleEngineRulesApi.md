# knetik_cloud.BRERuleEngineRulesApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bre_rule**](BRERuleEngineRulesApi.md#create_bre_rule) | **POST** /bre/rules | Create a rule
[**delete_bre_rule**](BRERuleEngineRulesApi.md#delete_bre_rule) | **DELETE** /bre/rules/{id} | Delete a rule
[**get_bre_expression_as_string**](BRERuleEngineRulesApi.md#get_bre_expression_as_string) | **POST** /bre/rules/expression-as-string | Returns a string representation of the provided expression
[**get_bre_rule**](BRERuleEngineRulesApi.md#get_bre_rule) | **GET** /bre/rules/{id} | Get a single rule
[**get_bre_rules**](BRERuleEngineRulesApi.md#get_bre_rules) | **GET** /bre/rules | List rules
[**set_bre_rule**](BRERuleEngineRulesApi.md#set_bre_rule) | **PUT** /bre/rules/{id}/enabled | Enable or disable a rule
[**update_bre_rule**](BRERuleEngineRulesApi.md#update_bre_rule) | **PUT** /bre/rules/{id} | Update a rule


# **create_bre_rule**
> BreRule create_bre_rule(bre_rule=bre_rule)

Create a rule

Rules define which actions to run when a given event verifies the specified condition. Full list of predicates and other type of expressions can be found at GET /bre/expressions/. <br><br><b>Permissions Needed:</b> BRE_RULE_ENGINE_RULES_ADMIN

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
api_instance = knetik_cloud.BRERuleEngineRulesApi(knetik_cloud.ApiClient(configuration))
bre_rule = knetik_cloud.BreRule() # BreRule | The BRE rule object (optional)

try: 
    # Create a rule
    api_response = api_instance.create_bre_rule(bre_rule=bre_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineRulesApi->create_bre_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bre_rule** | [**BreRule**](BreRule.md)| The BRE rule object | [optional] 

### Return type

[**BreRule**](BreRule.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bre_rule**
> delete_bre_rule(id)

Delete a rule

May fail if there are existing rules against it. Cannot delete core rules. <br><br><b>Permissions Needed:</b> BRE_RULE_ENGINE_RULES_ADMIN

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
api_instance = knetik_cloud.BRERuleEngineRulesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the rule

try: 
    # Delete a rule
    api_instance.delete_bre_rule(id)
except ApiException as e:
    print("Exception when calling BRERuleEngineRulesApi->delete_bre_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the rule | 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_expression_as_string**
> str get_bre_expression_as_string(expression=expression)

Returns a string representation of the provided expression

<b>Permissions Needed:</b> BRE_RULE_ENGINE_RULES_ADMIN

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
api_instance = knetik_cloud.BRERuleEngineRulesApi(knetik_cloud.ApiClient(configuration))
expression = knetik_cloud.Expressionobject() # Expressionobject | The expression (optional)

try: 
    # Returns a string representation of the provided expression
    api_response = api_instance.get_bre_expression_as_string(expression=expression)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineRulesApi->get_bre_expression_as_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | [**Expressionobject**](Expressionobject.md)| The expression | [optional] 

### Return type

**str**

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_rule**
> BreRule get_bre_rule(id)

Get a single rule

<b>Permissions Needed:</b> BRE_RULE_ENGINE_RULES_ADMIN

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
api_instance = knetik_cloud.BRERuleEngineRulesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the rule

try: 
    # Get a single rule
    api_response = api_instance.get_bre_rule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineRulesApi->get_bre_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the rule | 

### Return type

[**BreRule**](BreRule.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bre_rules**
> PageResourceBreRule get_bre_rules(filter_name=filter_name, filter_enabled=filter_enabled, filter_system=filter_system, filter_trigger=filter_trigger, filter_action=filter_action, filter_condition=filter_condition, size=size, page=page)

List rules

<b>Permissions Needed:</b> BRE_RULE_ENGINE_RULES_ADMIN

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
api_instance = knetik_cloud.BRERuleEngineRulesApi(knetik_cloud.ApiClient(configuration))
filter_name = 'filter_name_example' # str | Filter for rules containing the given name (optional)
filter_enabled = null # bool | Filter for rules by active status, null for both (optional) (default to null)
filter_system = true # bool | Filter for rules that are system rules when true, or not when false. Leave off for both mixed (optional)
filter_trigger = 'filter_trigger_example' # str | Filter for rules that are for the trigger with the given name (optional)
filter_action = 'filter_action_example' # str | Filter for rules that use the action with the given name (optional)
filter_condition = 'filter_condition_example' # str | Filter for rules that have a condition containing the given string (optional)
size = 25 # int | The number of objects returned per page (optional) (default to 25)
page = 1 # int | The number of the page returned, starting with 1 (optional) (default to 1)

try: 
    # List rules
    api_response = api_instance.get_bre_rules(filter_name=filter_name, filter_enabled=filter_enabled, filter_system=filter_system, filter_trigger=filter_trigger, filter_action=filter_action, filter_condition=filter_condition, size=size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineRulesApi->get_bre_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| Filter for rules containing the given name | [optional] 
 **filter_enabled** | **bool**| Filter for rules by active status, null for both | [optional] [default to null]
 **filter_system** | **bool**| Filter for rules that are system rules when true, or not when false. Leave off for both mixed | [optional] 
 **filter_trigger** | **str**| Filter for rules that are for the trigger with the given name | [optional] 
 **filter_action** | **str**| Filter for rules that use the action with the given name | [optional] 
 **filter_condition** | **str**| Filter for rules that have a condition containing the given string | [optional] 
 **size** | **int**| The number of objects returned per page | [optional] [default to 25]
 **page** | **int**| The number of the page returned, starting with 1 | [optional] [default to 1]

### Return type

[**PageResourceBreRule**](PageResourceBreRule.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_bre_rule**
> set_bre_rule(id, enabled=enabled)

Enable or disable a rule

This is helpful for turning off systems rules which cannot be deleted or modified otherwise. <br><br><b>Permissions Needed:</b> BRE_RULE_ENGINE_RULES_ADMIN

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
api_instance = knetik_cloud.BRERuleEngineRulesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the rule
enabled = knetik_cloud.BooleanResource() # BooleanResource | The boolean value (optional)

try: 
    # Enable or disable a rule
    api_instance.set_bre_rule(id, enabled=enabled)
except ApiException as e:
    print("Exception when calling BRERuleEngineRulesApi->set_bre_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the rule | 
 **enabled** | [**BooleanResource**](BooleanResource.md)| The boolean value | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bre_rule**
> BreRule update_bre_rule(id, bre_rule=bre_rule)

Update a rule

Cannot update system rules. <br><br><b>Permissions Needed:</b> BRE_RULE_ENGINE_RULES_ADMIN

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
api_instance = knetik_cloud.BRERuleEngineRulesApi(knetik_cloud.ApiClient(configuration))
id = 'id_example' # str | The id of the rule
bre_rule = knetik_cloud.BreRule() # BreRule | The BRE rule object (optional)

try: 
    # Update a rule
    api_response = api_instance.update_bre_rule(id, bre_rule=bre_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BRERuleEngineRulesApi->update_bre_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the rule | 
 **bre_rule** | [**BreRule**](BreRule.md)| The BRE rule object | [optional] 

### Return type

[**BreRule**](BreRule.md)

### Authorization

[oauth2_client_credentials_grant](../README.md#oauth2_client_credentials_grant), [oauth2_password_grant](../README.md#oauth2_password_grant)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

