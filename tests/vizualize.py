import os

if __name__ == "__main__":
    # os.environ["DAGSHUB_CLIENT_HOST"] = "https://test.dagshub.com"
    os.environ["DAGSHUB_CLIENT_HOST"] = "http://localhost:3000"
    from dagshub.data_engine.model import datasources
    # import logging
    # logging.basicConfig(level=logging.DEBUG)

    repo = "simon/baby-yoda-segmentation-dataset"
    try:
        ds = datasources.get_datasource(repo=repo, name="images")
    except:
        ds = datasources.create_from_repo(repo=repo, name="images", path="images")
        # ds = datasources.create_from_bucket(repo=repo, name="s3-bucket", bucket_url="s3://baby-yoda-dvc-cache")


    voxel = ds.visualize()
    voxel.wait(-1)
