# knetik_cloud.GamificationMetricsApi

All URIs are relative to *https://sandbox.knetikcloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_metric**](GamificationMetricsApi.md#add_metric) | **POST** /metrics | Add a metric


# **add_metric**
> add_metric(metric=metric)

Add a metric

Post a new score/stat for an activity occurrence without ending the occurrence itself

### Example 
```python
from __future__ import print_statement
import time
import knetik_cloud
from knetik_cloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
knetik_cloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = knetik_cloud.GamificationMetricsApi()
metric = knetik_cloud.MetricResource() # MetricResource | The new metric (optional)

try: 
    # Add a metric
    api_instance.add_metric(metric=metric)
except ApiException as e:
    print("Exception when calling GamificationMetricsApi->add_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | [**MetricResource**](MetricResource.md)| The new metric | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

