# DagsHubApi.CreateRepo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | name of the repository | 
**description** | **String** | A short description of the repository | [optional] 
**_private** | **Boolean** | Either true to create a private repository, or false to create a public one. | [optional] [default to false]
**autoInit** | **Boolean** | Pass true to create an initial commit with README, .gitignore and LICENSE. | [optional] [default to false]
**gitignores** | **String** | Desired language .gitignore templates to apply. Use the name of the templates. | [optional] 
**license** | **String** | Desired LICENSE template to apply. Use the name of the template. | [optional] 
**readme** | **String** | Desired README template to apply. Use the name of the template. | [optional] [default to &#x27;Default&#x27;]

<a name="LicenseEnum"></a>
## Enum: LicenseEnum

* `apacheLicense20` (value: `"Apache License 2.0"`)
* `mITLicense` (value: `"MIT License"`)
* `abstylesLicense` (value: `"Abstyles License"`)
* `academicFreeLicenseV11` (value: `"Academic Free License v1.1"`)
* `academicFreeLicenseV12` (value: `"Academic Free License v1.2"`)
* `academicFreeLicenseV20` (value: `"Academic Free License v2.0"`)
* `academicFreeLicenseV21` (value: `"Academic Free License v2.1"`)
* `academicFreeLicenseV30` (value: `"Academic Free License v3.0"`)
* `afferoGeneralPublicLicenseV10` (value: `"Affero General Public License v1.0"`)
* `apacheLicense10` (value: `"Apache License 1.0"`)
* `apacheLicense11` (value: `"Apache License 1.1"`)
* `artisticLicense10` (value: `"Artistic License 1.0"`)
* `artisticLicense20` (value: `"Artistic License 2.0"`)
* `bSD2ClauseLicense` (value: `"BSD 2-clause License"`)
* `bSD3ClauseLicense` (value: `"BSD 3-clause License"`)
* `bSD4ClauseLicense` (value: `"BSD 4-clause License"`)
* `creativeCommonsCC010Universal` (value: `"Creative Commons CC0 1.0 Universal"`)
* `eclipsePublicLicense10` (value: `"Eclipse Public License 1.0"`)
* `educationalCommunityLicenseV10` (value: `"Educational Community License v1.0"`)
* `educationalCommunityLicenseV20` (value: `"Educational Community License v2.0"`)
* `gNUAfferoGeneralPublicLicenseV30` (value: `"GNU Affero General Public License v3.0"`)
* `gNUFreeDocumentationLicenseV11` (value: `"GNU Free Documentation License v1.1"`)
* `gNUFreeDocumentationLicenseV12` (value: `"GNU Free Documentation License v1.2"`)
* `gNUFreeDocumentationLicenseV13` (value: `"GNU Free Documentation License v1.3"`)
* `gNUGeneralPublicLicenseV10` (value: `"GNU General Public License v1.0"`)
* `gNUGeneralPublicLicenseV20` (value: `"GNU General Public License v2.0"`)
* `gNUGeneralPublicLicenseV30` (value: `"GNU General Public License v3.0"`)
* `gNULesserGeneralPublicLicenseV21` (value: `"GNU Lesser General Public License v2.1"`)
* `gNULesserGeneralPublicLicenseV30` (value: `"GNU Lesser General Public License v3.0"`)
* `gNULibraryGeneralPublicLicenseV20` (value: `"GNU Library General Public License v2.0"`)
* `iSCLicense` (value: `"ISC license"`)
* `mozillaPublicLicense10` (value: `"Mozilla Public License 1.0"`)
* `mozillaPublicLicense11` (value: `"Mozilla Public License 1.1"`)
* `mozillaPublicLicense203` (value: `"Mozilla Public License 2.03"`)

