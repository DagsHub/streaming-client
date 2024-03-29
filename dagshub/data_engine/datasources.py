import logging
import urllib.parse
from typing import Optional, Union, List

from dagshub.common.api.repo import RepoAPI
from dagshub.data_engine.client.data_client import DataClient
from dagshub.data_engine.client.models import DatasourceType
from dagshub.data_engine.model.datasource import Datasource
from dagshub.data_engine.model.datasource_state import DatasourceState
from dagshub.data_engine.model.errors import DatasourceNotFoundError

logger = logging.getLogger(__name__)


def create_datasource(repo: str, name: str, path: str, revision: Optional[str] = None) -> Datasource:
    """
    Create a datasource from a path in the repo, or a storage bucket URL.

    :param repo: The full repo name in <owner>/<reponame> format
    :param name: The name of the datasource to be created
    :param path: Either a path to a directory inside the Git/DVC repo on DagsHub, e.g. "path/to/dir"
                 or else a URL pointing
                 to a storage bucket which is connected to the DagsHub repo - e.g. "s3://bucketname/path/in/bucket"
    :param revision: Only valid when using a Git/DVC path inside the DagsHub repo, not when using a bucket URL.
                     Allows you to define the branch name where the referenced directory exists.
                     The default repo branch is used if this is left blank.
    :return The created datasource
    """

    parsed = urllib.parse.urlparse(path)

    if parsed.scheme == "" \
        and parsed.hostname == "" \
        and parsed.query == "" \
        and parsed.params == "" \
        and parsed.fragment == "":
        return create_from_repo(repo, name, path=parsed.path, revision=revision)

    elif parsed.scheme != "" and parsed.hostname != "":
        # Bucket URL
        if parsed.query != "" or parsed.params != "" or parsed.fragment != "":
            raise ValueError("Invalid bucket URL: ", path)
        if revision != "":
            raise ValueError("revision cannot be used together with bucket URLs")
        return create_from_bucket(repo, name, bucket_url=path)

    raise ValueError("Invalid path used, format could not be determined: ", path)


create = create_datasource


def get_or_create(repo: str, name: str, path: str, revision: Optional[str] = None) -> Datasource:
    """
    First attempts to get the repo datasource with the given name, and only if that fails,
    invokes create_datasource with the given parameters.
    See the docs on create_datasource for more info.
    """
    try:
        return get_datasource(repo, name)
    except DatasourceNotFoundError:
        return create_datasource(repo, name, path, revision)


def create_from_bucket(repo: str, name: str, bucket_url: str) -> Datasource:
    # TODO: validation
    source = _create_datasource_state(repo, name, DatasourceType.BUCKET, bucket_url)
    return Datasource(source)


def create_from_repo(repo: str, name: str, path: str, revision: Optional[str] = None) -> Datasource:
    if revision is None:
        repo_api = RepoAPI(repo)
        revision = repo_api.default_branch
    url = f"repo://{repo}/{revision}:{path.lstrip('/')}"
    source = _create_datasource_state(repo, name, DatasourceType.REPOSITORY, url)
    if revision is not None:
        source.revision = revision
    return Datasource(source)


def get_datasource(repo: str, name: Optional[str] = None, id: Optional[Union[int, str]] = None, **kwargs) -> Datasource:
    """
    Additional kwargs:
    revision - for repo datasources defines which branch/revision to download from (default branch if not specified)
    """
    ds_state = DatasourceState(repo=repo, name=name, id=id)
    ds_state.get_from_dagshub()
    if "revision" in kwargs:
        ds_state.revision = kwargs["revision"]
    return Datasource(ds_state)


def get_datasources(repo: str) -> List[Datasource]:
    client = DataClient(repo)
    sources = client.get_datasources(None, None)
    return [Datasource(DatasourceState.from_gql_result(repo, source)) for source in sources]


# Alias
get = get_datasource


def _create_datasource_state(repo: str, name: str, source_type: DatasourceType, path: str) -> DatasourceState:
    ds = DatasourceState(name=name, repo=repo)
    ds.source_type = source_type
    ds.path = path
    ds.create()
    return ds


__all__ = [
    create_datasource,
    create,
    create_from_bucket,
    create_from_repo,
    get_datasource,
    get,
    get_or_create,
]
