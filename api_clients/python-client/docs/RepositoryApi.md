# swagger_client.RepositoryApi

All URIs are relative to *http://localhost:3000/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org_repo**](RepositoryApi.md#create_org_repo) | **POST** /org/{orgname}/repos | Create in organization
[**create_repo**](RepositoryApi.md#create_repo) | **POST** /user/repos | Create
[**list_my_repos**](RepositoryApi.md#list_my_repos) | **GET** /user/repos | List your repositories
[**list_org_repos**](RepositoryApi.md#list_org_repos) | **GET** /orgs/{orgname}/repos | List organization repositories
[**list_user_repos**](RepositoryApi.md#list_user_repos) | **GET** /users/{username}/repos | List user repositories
[**migrate_repo**](RepositoryApi.md#migrate_repo) | **POST** /repos/migrate | Migrate repository
[**search**](RepositoryApi.md#search) | **GET** /repos/search | Search repositories

# **create_org_repo**
> create_org_repo(orgname, body=body)

Create in organization

Create a new repository in this organization. The authenticated user must be an **owner** of the specified organization.

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
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
orgname = 'orgname_example' # str | A DagsHub organization name
body = swagger_client.CreateRepo() # CreateRepo |  (optional)

try:
    # Create in organization
    api_instance.create_org_repo(orgname, body=body)
except ApiException as e:
    print("Exception when calling RepositoryApi->create_org_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| A DagsHub organization name | 
 **body** | [**CreateRepo**](CreateRepo.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repo**
> create_repo(body=body)

Create

Create a new repository for the authenticated user.

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
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRepo() # CreateRepo |  (optional)

try:
    # Create
    api_instance.create_repo(body=body)
except ApiException as e:
    print("Exception when calling RepositoryApi->create_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRepo**](CreateRepo.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_repos**
> object list_my_repos()

List your repositories

List repositories that are accessible to the authenticated user.  This includes repositories owned by the authenticated user, repositories where the authenticated user is a collaborator, and repositories that the authenticated user has access to through an organization membership. 

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
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))

try:
    # List your repositories
    api_response = api_instance.list_my_repos()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->list_my_repos: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_org_repos**
> list_org_repos(orgname)

List organization repositories

List repositories that are accessible to the authenticated user.

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
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
orgname = 'orgname_example' # str | A DagsHub organization name

try:
    # List organization repositories
    api_instance.list_org_repos(orgname)
except ApiException as e:
    print("Exception when calling RepositoryApi->list_org_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **str**| A DagsHub organization name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_repos**
> list_user_repos(username)

List user repositories

List public repositories for the specified user.

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
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | A DagsHub username

try:
    # List user repositories
    api_instance.list_user_repos(username)
except ApiException as e:
    print("Exception when calling RepositoryApi->list_user_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| A DagsHub username | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrate_repo**
> migrate_repo(body=body)

Migrate repository

Migrate a repository from other Git hosting sources for the authenticated user.  To migrate a repository for a organization, the authenticated user must be a **owner** of the specified organization. 

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
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.MigrateRepo() # MigrateRepo |  (optional)

try:
    # Migrate repository
    api_instance.migrate_repo(body=body)
except ApiException as e:
    print("Exception when calling RepositoryApi->migrate_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrateRepo**](MigrateRepo.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> object search(q, uid=uid, limit=limit, page=page)

Search repositories

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
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | 
uid = 0 # int | User ID to specify search whose repositories. Default is 0 and search all repositories (optional) (default to 0)
limit = 10 # int | Maximum number of repositories in search results. (optional) (default to 10)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)

try:
    # Search repositories
    api_response = api_instance.search(q, uid=uid, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | 
 **uid** | **int**| User ID to specify search whose repositories. Default is 0 and search all repositories | [optional] [default to 0]
 **limit** | **int**| Maximum number of repositories in search results. | [optional] [default to 10]
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

