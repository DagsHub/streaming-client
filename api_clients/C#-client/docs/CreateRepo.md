# IO.Swagger.Model.CreateRepo
## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | name of the repository | 
**Description** | **string** | A short description of the repository | [optional] 
**_Private** | **bool?** | Either true to create a private repository, or false to create a public one. | [optional] [default to false]
**AutoInit** | **bool?** | Pass true to create an initial commit with README, .gitignore and LICENSE. | [optional] [default to false]
**Gitignores** | **string** | Desired language .gitignore templates to apply. Use the name of the templates. | [optional] 
**License** | **string** | Desired LICENSE template to apply. Use the name of the template. | [optional] 
**Readme** | **string** | Desired README template to apply. Use the name of the template. | [optional] [default to "Default"]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

