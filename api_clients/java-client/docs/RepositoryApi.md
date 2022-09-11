# RepositoryApi

All URIs are relative to *http://localhost:3000/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrgRepo**](RepositoryApi.md#createOrgRepo) | **POST** /org/{orgname}/repos | Create in organization
[**createRepo**](RepositoryApi.md#createRepo) | **POST** /user/repos | Create
[**listMyRepos**](RepositoryApi.md#listMyRepos) | **GET** /user/repos | List your repositories
[**listOrgRepos**](RepositoryApi.md#listOrgRepos) | **GET** /orgs/{orgname}/repos | List organization repositories
[**listUserRepos**](RepositoryApi.md#listUserRepos) | **GET** /users/{username}/repos | List user repositories
[**migrateRepo**](RepositoryApi.md#migrateRepo) | **POST** /repos/migrate | Migrate repository
[**search**](RepositoryApi.md#search) | **GET** /repos/search | Search repositories

<a name="createOrgRepo"></a>
# **createOrgRepo**
> createOrgRepo(orgname, body)

Create in organization

Create a new repository in this organization. The authenticated user must be an **owner** of the specified organization.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RepositoryApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

// Configure API key authorization: tokenAuth
ApiKeyAuth tokenAuth = (ApiKeyAuth) defaultClient.getAuthentication("tokenAuth");
tokenAuth.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.setApiKeyPrefix("Token");

RepositoryApi apiInstance = new RepositoryApi();
String orgname = "orgname_example"; // String | A DagsHub organization name
CreateRepo body = new CreateRepo(); // CreateRepo | 
try {
    apiInstance.createOrgRepo(orgname, body);
} catch (ApiException e) {
    System.err.println("Exception when calling RepositoryApi#createOrgRepo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **String**| A DagsHub organization name |
 **body** | [**CreateRepo**](CreateRepo.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="createRepo"></a>
# **createRepo**
> createRepo(body)

Create

Create a new repository for the authenticated user.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RepositoryApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

// Configure API key authorization: tokenAuth
ApiKeyAuth tokenAuth = (ApiKeyAuth) defaultClient.getAuthentication("tokenAuth");
tokenAuth.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.setApiKeyPrefix("Token");

RepositoryApi apiInstance = new RepositoryApi();
CreateRepo body = new CreateRepo(); // CreateRepo | 
try {
    apiInstance.createRepo(body);
} catch (ApiException e) {
    System.err.println("Exception when calling RepositoryApi#createRepo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRepo**](CreateRepo.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="listMyRepos"></a>
# **listMyRepos**
> Object listMyRepos()

List your repositories

List repositories that are accessible to the authenticated user.  This includes repositories owned by the authenticated user, repositories where the authenticated user is a collaborator, and repositories that the authenticated user has access to through an organization membership. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RepositoryApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

// Configure API key authorization: tokenAuth
ApiKeyAuth tokenAuth = (ApiKeyAuth) defaultClient.getAuthentication("tokenAuth");
tokenAuth.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.setApiKeyPrefix("Token");

RepositoryApi apiInstance = new RepositoryApi();
try {
    Object result = apiInstance.listMyRepos();
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RepositoryApi#listMyRepos");
    e.printStackTrace();
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listOrgRepos"></a>
# **listOrgRepos**
> listOrgRepos(orgname)

List organization repositories

List repositories that are accessible to the authenticated user.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RepositoryApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

// Configure API key authorization: tokenAuth
ApiKeyAuth tokenAuth = (ApiKeyAuth) defaultClient.getAuthentication("tokenAuth");
tokenAuth.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.setApiKeyPrefix("Token");

RepositoryApi apiInstance = new RepositoryApi();
String orgname = "orgname_example"; // String | A DagsHub organization name
try {
    apiInstance.listOrgRepos(orgname);
} catch (ApiException e) {
    System.err.println("Exception when calling RepositoryApi#listOrgRepos");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **String**| A DagsHub organization name |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="listUserRepos"></a>
# **listUserRepos**
> listUserRepos(username)

List user repositories

List public repositories for the specified user.

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RepositoryApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

// Configure API key authorization: tokenAuth
ApiKeyAuth tokenAuth = (ApiKeyAuth) defaultClient.getAuthentication("tokenAuth");
tokenAuth.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.setApiKeyPrefix("Token");

RepositoryApi apiInstance = new RepositoryApi();
String username = "username_example"; // String | A DagsHub username
try {
    apiInstance.listUserRepos(username);
} catch (ApiException e) {
    System.err.println("Exception when calling RepositoryApi#listUserRepos");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| A DagsHub username |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

<a name="migrateRepo"></a>
# **migrateRepo**
> migrateRepo(body)

Migrate repository

Migrate a repository from other Git hosting sources for the authenticated user.  To migrate a repository for a organization, the authenticated user must be a **owner** of the specified organization. 

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RepositoryApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

// Configure API key authorization: tokenAuth
ApiKeyAuth tokenAuth = (ApiKeyAuth) defaultClient.getAuthentication("tokenAuth");
tokenAuth.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.setApiKeyPrefix("Token");

RepositoryApi apiInstance = new RepositoryApi();
MigrateRepo body = new MigrateRepo(); // MigrateRepo | 
try {
    apiInstance.migrateRepo(body);
} catch (ApiException e) {
    System.err.println("Exception when calling RepositoryApi#migrateRepo");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrateRepo**](MigrateRepo.md)|  | [optional]

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a name="search"></a>
# **search**
> Object search(q, uid, limit, page)

Search repositories

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.RepositoryApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

// Configure API key authorization: tokenAuth
ApiKeyAuth tokenAuth = (ApiKeyAuth) defaultClient.getAuthentication("tokenAuth");
tokenAuth.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//tokenAuth.setApiKeyPrefix("Token");

RepositoryApi apiInstance = new RepositoryApi();
String q = "q_example"; // String | 
Integer uid = 0; // Integer | User ID to specify search whose repositories. Default is 0 and search all repositories
Integer limit = 10; // Integer | Maximum number of repositories in search results.
Integer page = 1; // Integer | Page number. Default is 1.
try {
    Object result = apiInstance.search(q, uid, limit, page);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RepositoryApi#search");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **String**|  |
 **uid** | **Integer**| User ID to specify search whose repositories. Default is 0 and search all repositories | [optional] [default to 0]
 **limit** | **Integer**| Maximum number of repositories in search results. | [optional] [default to 10]
 **page** | **Integer**| Page number. Default is 1. | [optional] [default to 1]

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

