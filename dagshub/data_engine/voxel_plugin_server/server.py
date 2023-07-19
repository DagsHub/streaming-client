import asyncio
import logging
from threading import Thread
from typing import TYPE_CHECKING, Optional

from hypercorn.asyncio import serve
from hypercorn.config import Config

from dagshub.common import is_inside_colab
from dagshub.data_engine.voxel_plugin_server.app import app
from dagshub.data_engine.voxel_plugin_server.models import PluginServerState

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from dagshub.data_engine.model.datasource import Datasource
    import fiftyone as fo

DEFAULT_PORT = 5152

_running_server = None


class PluginServer:
    def __init__(self, state: PluginServerState):
        self._ev_loop = asyncio.new_event_loop()

        self._config = Config()
        self.server_address = self.generate_url()
        print(f"URL: {self.server_address}")
        self._config.bind = [f"0.0.0.0:{DEFAULT_PORT}"]
        self._state = state

        self._shutdown_event = asyncio.Event()
        self._thread = Thread(target=self._ev_loop.run_until_complete, args=(self.start_serve(),), daemon=True)
        self._thread.start()

    def generate_url(self):
        if is_inside_colab():
            from google.colab.output import eval_js
            proxy_link = eval_js(f"google.colab.kernel.proxyPort({DEFAULT_PORT})")
            return proxy_link
        else:
            return f"http://localhost:{DEFAULT_PORT}"


    def set_plugin_config(self, session: "fo.Session"):
        dataset = session.dataset
        dataset.app_config.plugins["dagshub"] = {
            "server": self.server_address,
            "in_colab": is_inside_colab(),
        }
        dataset.save()

    async def start_serve(self):
        self.set_state(self._state)
        await serve(app, self._config, shutdown_trigger=self._shutdown_event.wait)

    def set_state(self, state: PluginServerState):
        self._state = state
        app.state.PLUGIN_STATE = self._state
        self.set_plugin_config(state.voxel_session)

    def stop(self):
        self._shutdown_event.set()
        self._thread.join()


def run_plugin_server(voxel_session: "fo.Session", datasource: "Datasource", branch: Optional[str]) -> PluginServer:
    global _running_server
    state = PluginServerState(voxel_session, datasource, branch)
    if _running_server is None:
        _running_server = PluginServer(state)
    else:
        _running_server.set_state(state)

    return _running_server

# if __name__ == "__main__":
#     repo = RepoAPI(repo="kirill/baby-yoda-segmentation-dataset", host="http://localhost:3000")
#     set_voxel_envvars()
#     logging.basicConfig(level=logging.INFO)
#
#     import fiftyone as fo
#
#     fo.set_logging_level(level=logging.INFO)
#
#     sess = fo.launch_app(fo.load_dataset("default-dataset"))
#     server_state = PluginServerState(voxel_session=sess, repo=repo, branch=None)
#     run_plugin_server(sess, repo, None)
#     sess.wait()
