# IO.Swagger.Api.RepositoryApi

All URIs are relative to *http://localhost:3000/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateOrgRepo**](RepositoryApi.md#createorgrepo) | **POST** /org/{orgname}/repos | Create in organization
[**CreateRepo**](RepositoryApi.md#createrepo) | **POST** /user/repos | Create
[**ListMyRepos**](RepositoryApi.md#listmyrepos) | **GET** /user/repos | List your repositories
[**ListOrgRepos**](RepositoryApi.md#listorgrepos) | **GET** /orgs/{orgname}/repos | List organization repositories
[**ListUserRepos**](RepositoryApi.md#listuserrepos) | **GET** /users/{username}/repos | List user repositories
[**MigrateRepo**](RepositoryApi.md#migraterepo) | **POST** /repos/migrate | Migrate repository
[**Search**](RepositoryApi.md#search) | **GET** /repos/search | Search repositories

<a name="createorgrepo"></a>
# **CreateOrgRepo**
> void CreateOrgRepo (string orgname, CreateRepo body = null)

Create in organization

Create a new repository in this organization. The authenticated user must be an **owner** of the specified organization.

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class CreateOrgRepoExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new RepositoryApi();
            var orgname = orgname_example;  // string | A DagsHub organization name
            var body = new CreateRepo(); // CreateRepo |  (optional) 

            try
            {
                // Create in organization
                apiInstance.CreateOrgRepo(orgname, body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling RepositoryApi.CreateOrgRepo: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **string**| A DagsHub organization name | 
 **body** | [**CreateRepo**](CreateRepo.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="createrepo"></a>
# **CreateRepo**
> void CreateRepo (CreateRepo body = null)

Create

Create a new repository for the authenticated user.

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class CreateRepoExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new RepositoryApi();
            var body = new CreateRepo(); // CreateRepo |  (optional) 

            try
            {
                // Create
                apiInstance.CreateRepo(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling RepositoryApi.CreateRepo: " + e.Message );
            }
        }
    }
}
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
<a name="listmyrepos"></a>
# **ListMyRepos**
> Object ListMyRepos ()

List your repositories

List repositories that are accessible to the authenticated user.  This includes repositories owned by the authenticated user, repositories where the authenticated user is a collaborator, and repositories that the authenticated user has access to through an organization membership. 

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ListMyReposExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new RepositoryApi();

            try
            {
                // List your repositories
                Object result = apiInstance.ListMyRepos();
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling RepositoryApi.ListMyRepos: " + e.Message );
            }
        }
    }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="listorgrepos"></a>
# **ListOrgRepos**
> void ListOrgRepos (string orgname)

List organization repositories

List repositories that are accessible to the authenticated user.

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ListOrgReposExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new RepositoryApi();
            var orgname = orgname_example;  // string | A DagsHub organization name

            try
            {
                // List organization repositories
                apiInstance.ListOrgRepos(orgname);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling RepositoryApi.ListOrgRepos: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgname** | **string**| A DagsHub organization name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="listuserrepos"></a>
# **ListUserRepos**
> void ListUserRepos (string username)

List user repositories

List public repositories for the specified user.

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ListUserReposExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new RepositoryApi();
            var username = username_example;  // string | A DagsHub username

            try
            {
                // List user repositories
                apiInstance.ListUserRepos(username);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling RepositoryApi.ListUserRepos: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **string**| A DagsHub username | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="migraterepo"></a>
# **MigrateRepo**
> void MigrateRepo (MigrateRepo body = null)

Migrate repository

Migrate a repository from other Git hosting sources for the authenticated user.  To migrate a repository for a organization, the authenticated user must be a **owner** of the specified organization. 

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class MigrateRepoExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new RepositoryApi();
            var body = new MigrateRepo(); // MigrateRepo |  (optional) 

            try
            {
                // Migrate repository
                apiInstance.MigrateRepo(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling RepositoryApi.MigrateRepo: " + e.Message );
            }
        }
    }
}
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
<a name="search"></a>
# **Search**
> Object Search (string q, int? uid = null, int? limit = null, int? page = null)

Search repositories

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class SearchExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";
            // Configure API key authorization: tokenAuth
            Configuration.Default.AddApiKey("token", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("token", "Bearer");

            var apiInstance = new RepositoryApi();
            var q = q_example;  // string | 
            var uid = 56;  // int? | User ID to specify search whose repositories. Default is 0 and search all repositories (optional)  (default to 0)
            var limit = 56;  // int? | Maximum number of repositories in search results. (optional)  (default to 10)
            var page = 56;  // int? | Page number. Default is 1. (optional)  (default to 1)

            try
            {
                // Search repositories
                Object result = apiInstance.Search(q, uid, limit, page);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling RepositoryApi.Search: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **string**|  | 
 **uid** | **int?**| User ID to specify search whose repositories. Default is 0 and search all repositories | [optional] [default to 0]
 **limit** | **int?**| Maximum number of repositories in search results. | [optional] [default to 10]
 **page** | **int?**| Page number. Default is 1. | [optional] [default to 1]

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
