# Download current stable 3.x.x branch (OpenAPI version 3)
wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.35/swagger-codegen-cli-3.0.35.jar -O swagger-codegen-cli.jar

java -jar swagger-codegen-cli.jar generate \
-i https://dagshub.com/DAGsHub-Official/dagshub-docs/raw/openapi-spec-and-swagger-ui/theme/openapi/spec.yaml \
-l python \
-o python-client

# TODO: generate more SDKs