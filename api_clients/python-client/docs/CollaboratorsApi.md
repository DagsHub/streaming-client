# swagger_client.CollaboratorsApi

All URIs are relative to *http://localhost:3000/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_collaborator**](CollaboratorsApi.md#add_collaborator) | **PUT** /repos/{username}/{repo}/collaborators/{collaborator} | Add user as a collaborator
[**get_collaborators**](CollaboratorsApi.md#get_collaborators) | **GET** /repos/{username}/{repo}/collaborators | Get collaborators
[**remove_collaborator**](CollaboratorsApi.md#remove_collaborator) | **DELETE** /repos/{username}/{repo}/collaborators/{collaborator} | Delete collaborator

# **add_collaborator**
> add_collaborator(username, repo, collaborator, body=body)

Add user as a collaborator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CollaboratorsApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | A DagsHub username
repo = 'repo_example' # str | name of the repository
collaborator = 'collaborator_example' # str | collaborator username
body = swagger_client.CollaboratorsCollaboratorBody() # CollaboratorsCollaboratorBody |  (optional)

try:
    # Add user as a collaborator
    api_instance.add_collaborator(username, repo, collaborator, body=body)
except ApiException as e:
    print("Exception when calling CollaboratorsApi->add_collaborator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| A DagsHub username | 
 **repo** | **str**| name of the repository | 
 **collaborator** | **str**| collaborator username | 
 **body** | [**CollaboratorsCollaboratorBody**](CollaboratorsCollaboratorBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collaborators**
> get_collaborators(username, repo)

Get collaborators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CollaboratorsApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | A DagsHub username
repo = 'repo_example' # str | name of the repository

try:
    # Get collaborators
    api_instance.get_collaborators(username, repo)
except ApiException as e:
    print("Exception when calling CollaboratorsApi->get_collaborators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| A DagsHub username | 
 **repo** | **str**| name of the repository | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_collaborator**
> remove_collaborator()

Delete collaborator

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: tokenAuth
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CollaboratorsApi(swagger_client.ApiClient(configuration))

try:
    # Delete collaborator
    api_instance.remove_collaborator()
except ApiException as e:
    print("Exception when calling CollaboratorsApi->remove_collaborator: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

