# swagger_client.GamificationMetricsApi

All URIs are relative to *https://integration.knetikcloud.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metric_using_post**](GamificationMetricsApi.md#add_metric_using_post) | **POST** /metrics | Add a metric


# **add_metric_using_post**
> add_metric_using_post(metric=metric)

Add a metric

Post a new score/stat for an activity occurrence without ending the occurrence itself

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
api_instance = swagger_client.GamificationMetricsApi()
metric = swagger_client.MetricResource() # MetricResource | The new metric (optional)

try: 
    # Add a metric
    api_instance.add_metric_using_post(metric=metric)
except ApiException as e:
    print("Exception when calling GamificationMetricsApi->add_metric_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | [**MetricResource**](MetricResource.md)| The new metric | [optional] 

### Return type

void (empty response body)

### Authorization

[knetik_oauth](../README.md#knetik_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

