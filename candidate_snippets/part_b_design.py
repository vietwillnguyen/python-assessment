# Part B — System Design
#
# This utility function exists in three of our repos right now —
# the Dagster orchestration code, the dbt runner, and the agent eval framework.
# Each copy has drifted slightly. You've been asked to extract it into a single
# internal shared Python package that all three consume.
# Walk through how you'd design it.

import os
import clickhouse_connect


def get_ch_client():
    return clickhouse_connect.get_client(
        host=os.environ["CH_HOST"],
        port=int(os.environ.get("CH_PORT", "8123")),
        username=os.environ.get("CH_USER", "default"),
        password=os.environ["CH_PASSWORD"],
    )


# --- Drifted copy in repo 2 (dbt runner) ---
# Has an extra timeout param added by someone, not present elsewhere

def get_ch_client_with_timeout():
    return clickhouse_connect.get_client(
        host=os.environ["CH_HOST"],
        port=int(os.environ.get("CH_PORT", "8123")),
        username=os.environ.get("CH_USER", "default"),
        password=os.environ["CH_PASSWORD"],
        connect_timeout=int(os.environ.get("CH_TIMEOUT", "30")),
    )


# --- Drifted copy in repo 3 (agent eval) ---
# Reads from a different env var naming convention

def get_clickhouse_connection():
    return clickhouse_connect.get_client(
        host=os.environ["CLICKHOUSE_HOST"],
        port=int(os.environ.get("CLICKHOUSE_PORT", "8123")),
        username=os.environ.get("CLICKHOUSE_USERNAME", "default"),
        password=os.environ["CLICKHOUSE_PASSWORD"],
    )
