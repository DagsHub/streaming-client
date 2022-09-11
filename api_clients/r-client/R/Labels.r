# DagsHub API
#
# This API is used to interact with DagsHub. 
#
# OpenAPI spec version: 1.0.0
# 
# Generated by: https://github.com/swagger-api/swagger-codegen.git

#' Labels Class
#'
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
Labels <- R6::R6Class(
  'Labels',
  public = list(
    initialize = function(){
    },
    toJSON = function() {
      LabelsObject <- list()

      LabelsObject
    },
    fromJSON = function(LabelsJson) {
      LabelsObject <- jsonlite::fromJSON(LabelsJson)
    },
    toJSONString = function() {
       sprintf(
        '{
        }',
      )
    },
    fromJSONString = function(LabelsJson) {
      LabelsObject <- jsonlite::fromJSON(LabelsJson)
    }
  )
)