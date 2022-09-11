# Download current stable 3.x.x branch (OpenAPI version 3)
wget https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.35/swagger-codegen-cli-3.0.35.jar -O swagger-codegen-cli.jar

rm -rf python-client r-client java-client C#-client go-client javascript-client

java -jar swagger-codegen-cli.jar generate \
-i https://dagshub.com/DAGsHub-Official/dagshub-docs/raw/main/theme/openapi/spec.yaml \
-l python \
-o python-client

java -jar swagger-codegen-cli.jar generate \
-i https://dagshub.com/DAGsHub-Official/dagshub-docs/raw/main/theme/openapi/spec.yaml \
-l r \
-o r-client

java -jar swagger-codegen-cli.jar generate \
-i https://dagshub.com/DAGsHub-Official/dagshub-docs/raw/main/theme/openapi/spec.yaml \
-l java \
-o java-client

java -jar swagger-codegen-cli.jar generate \
-i https://dagshub.com/DAGsHub-Official/dagshub-docs/raw/main/theme/openapi/spec.yaml \
-l csharp \
-o C#-client

java -jar swagger-codegen-cli.jar generate \
-i https://dagshub.com/DAGsHub-Official/dagshub-docs/raw/main/theme/openapi/spec.yaml \
-l go \
-o go-client

java -jar swagger-codegen-cli.jar generate \
-i https://dagshub.com/DAGsHub-Official/dagshub-docs/raw/main/theme/openapi/spec.yaml \
-l javascript \
-o javascript-client
