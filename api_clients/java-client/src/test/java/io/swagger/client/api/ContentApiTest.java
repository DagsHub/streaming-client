/*
 * DagsHub API
 * This API is used to interact with DagsHub. 
 *
 * OpenAPI spec version: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.api;

import io.swagger.client.model.Files;
import org.junit.Test;
import org.junit.Ignore;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * API tests for ContentApi
 */
@Ignore
public class ContentApiTest {

    private final ContentApi api = new ContentApi();

    /**
     * Download archive
     *
     * This method returns archive by given format.
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void getArchiveTest() throws Exception {
        String username = null;
        String repo = null;
        String ref = null;
        String format = null;
        api.getArchive(username, repo, ref, format);

        // TODO: test validations
    }
    /**
     * Get data from a folder in repository
     *
     * 
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void getContentTest() throws Exception {
        String owner = null;
        String repo = null;
        String branch = null;
        String treePath = null;
        Boolean includeSize = null;
        Files response = api.getContent(owner, repo, branch, treePath, includeSize);

        // TODO: test validations
    }
    /**
     * Download raw content
     *
     * This method returns the raw content of a file.
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void getRawTest() throws Exception {
        String username = null;
        String repo = null;
        String ref = null;
        String path = null;
        api.getRaw(username, repo, ref, path);

        // TODO: test validations
    }
    /**
     * Upload data to a repository
     *
     * last_commit - If the tip of the branch differs on the server at the moment of processing the request, the request is denied.
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void uploadContentTest() throws Exception {
        String owner = null;
        String repo = null;
        String branch = null;
        String treePath = null;
        String commitSummary = null;
        String commitMessage = null;
        String commitChoice = null;
        String lastCommit = null;
        String newBranchName = null;
        String versioning = null;
        List<Object> files = null;
        Object response = api.uploadContent(owner, repo, branch, treePath, commitSummary, commitMessage, commitChoice, lastCommit, newBranchName, versioning, files);

        // TODO: test validations
    }
}