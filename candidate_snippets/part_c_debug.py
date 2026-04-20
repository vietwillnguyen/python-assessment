# Part C — Debugging
#
# This client works fine in unit tests and when run as a standalone script,
# but it deadlocks intermittently when called from inside a Dagster op in production.
# Walk through how you'd diagnose this.

import asyncio
import httpx


class PipelineClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self._http = httpx.AsyncClient()

    def get_run_status(self, run_id: str) -> dict:
        return asyncio.run(self._fetch_status(run_id))

    async def _fetch_status(self, run_id: str) -> dict:
        resp = await self._http.get(f"{self.base_url}/runs/{run_id}")
        return resp.json()
