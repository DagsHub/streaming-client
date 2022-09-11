# CreateRepo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | name of the repository | 
**description** | **String** | A short description of the repository |  [optional]
**_private** | **Boolean** | Either true to create a private repository, or false to create a public one. |  [optional]
**autoInit** | **Boolean** | Pass true to create an initial commit with README, .gitignore and LICENSE. |  [optional]
**gitignores** | **String** | Desired language .gitignore templates to apply. Use the name of the templates. |  [optional]
**license** | [**LicenseEnum**](#LicenseEnum) | Desired LICENSE template to apply. Use the name of the template. |  [optional]
**readme** | **String** | Desired README template to apply. Use the name of the template. |  [optional]

<a name="LicenseEnum"></a>
## Enum: LicenseEnum
Name | Value
---- | -----
APACHE_LICENSE_2_0 | &quot;Apache License 2.0&quot;
MIT_LICENSE | &quot;MIT License&quot;
ABSTYLES_LICENSE | &quot;Abstyles License&quot;
ACADEMIC_FREE_LICENSE_V1_1 | &quot;Academic Free License v1.1&quot;
ACADEMIC_FREE_LICENSE_V1_2 | &quot;Academic Free License v1.2&quot;
ACADEMIC_FREE_LICENSE_V2_0 | &quot;Academic Free License v2.0&quot;
ACADEMIC_FREE_LICENSE_V2_1 | &quot;Academic Free License v2.1&quot;
ACADEMIC_FREE_LICENSE_V3_0 | &quot;Academic Free License v3.0&quot;
AFFERO_GENERAL_PUBLIC_LICENSE_V1_0 | &quot;Affero General Public License v1.0&quot;
APACHE_LICENSE_1_0 | &quot;Apache License 1.0&quot;
APACHE_LICENSE_1_1 | &quot;Apache License 1.1&quot;
ARTISTIC_LICENSE_1_0 | &quot;Artistic License 1.0&quot;
ARTISTIC_LICENSE_2_0 | &quot;Artistic License 2.0&quot;
BSD_2_CLAUSE_LICENSE | &quot;BSD 2-clause License&quot;
BSD_3_CLAUSE_LICENSE | &quot;BSD 3-clause License&quot;
BSD_4_CLAUSE_LICENSE | &quot;BSD 4-clause License&quot;
CREATIVE_COMMONS_CC0_1_0_UNIVERSAL | &quot;Creative Commons CC0 1.0 Universal&quot;
ECLIPSE_PUBLIC_LICENSE_1_0 | &quot;Eclipse Public License 1.0&quot;
EDUCATIONAL_COMMUNITY_LICENSE_V1_0 | &quot;Educational Community License v1.0&quot;
EDUCATIONAL_COMMUNITY_LICENSE_V2_0 | &quot;Educational Community License v2.0&quot;
GNU_AFFERO_GENERAL_PUBLIC_LICENSE_V3_0 | &quot;GNU Affero General Public License v3.0&quot;
GNU_FREE_DOCUMENTATION_LICENSE_V1_1 | &quot;GNU Free Documentation License v1.1&quot;
GNU_FREE_DOCUMENTATION_LICENSE_V1_2 | &quot;GNU Free Documentation License v1.2&quot;
GNU_FREE_DOCUMENTATION_LICENSE_V1_3 | &quot;GNU Free Documentation License v1.3&quot;
GNU_GENERAL_PUBLIC_LICENSE_V1_0 | &quot;GNU General Public License v1.0&quot;
GNU_GENERAL_PUBLIC_LICENSE_V2_0 | &quot;GNU General Public License v2.0&quot;
GNU_GENERAL_PUBLIC_LICENSE_V3_0 | &quot;GNU General Public License v3.0&quot;
GNU_LESSER_GENERAL_PUBLIC_LICENSE_V2_1 | &quot;GNU Lesser General Public License v2.1&quot;
GNU_LESSER_GENERAL_PUBLIC_LICENSE_V3_0 | &quot;GNU Lesser General Public License v3.0&quot;
GNU_LIBRARY_GENERAL_PUBLIC_LICENSE_V2_0 | &quot;GNU Library General Public License v2.0&quot;
ISC_LICENSE | &quot;ISC license&quot;
MOZILLA_PUBLIC_LICENSE_1_0 | &quot;Mozilla Public License 1.0&quot;
MOZILLA_PUBLIC_LICENSE_1_1 | &quot;Mozilla Public License 1.1&quot;
MOZILLA_PUBLIC_LICENSE_2_03 | &quot;Mozilla Public License 2.03&quot;
