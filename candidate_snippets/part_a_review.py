# Part A — Code Review
#
# This is a PR adding a ClickHouse client wrapper to our shared platform library.
# Review it as you would a real PR — walk through what you'd comment on, block, or approve.

import clickhouse_connect
from typing import Any


class ClickHouseClient:
    def __init__(self, host: str, port: int, settings: dict = {}):
        self.host = host
        self.port = port
        self.settings = settings
        self._client = None

    def connect(self):
        self._client = clickhouse_connect.get_client(
            host=self.host,
            port=self.port,
            settings=self.settings,
        )

    def query(self, sql: str, params: Any = None) -> list:
        try:
            result = self._client.query(sql, params)
            return result.result_rows
        except Exception as e:
            print(f"Query failed: {e}")
            return []

    def run_pipeline_query(self, pipeline_id: str) -> list:
        sql = f"SELECT * FROM pipelines WHERE id = '{pipeline_id}'"
        return self.query(sql)

    def close(self):
        self._client.close()
