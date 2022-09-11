# DagsHub API
#
# This API is used to interact with DagsHub. 
#
# OpenAPI spec version: 1.0.0
# 
# Generated by: https://github.com/swagger-api/swagger-codegen.git

#' State Class
#'
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
State <- R6::R6Class(
  'State',
  public = list(
    initialize = function(){
    },
    toJSON = function() {
      StateObject <- list()

      StateObject
    },
    fromJSON = function(StateJson) {
      StateObject <- jsonlite::fromJSON(StateJson)
    },
    toJSONString = function() {
       sprintf(
        '{
        }',
      )
    },
    fromJSONString = function(StateJson) {
      StateObject <- jsonlite::fromJSON(StateJson)
    }
  )
)
