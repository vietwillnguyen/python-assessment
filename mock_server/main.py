# mock_server/main.py
# Simple mock server simulating the DataFabric platform API.
# Run with: uvicorn main:app --reload --port 8000

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Literal
import random

app = FastAPI(title="DataFabric Mock API", version="0.1.0")


# --- Models ---

class Pipeline(BaseModel):
    id: str
    name: str
    status: Literal["active", "paused", "error"]
    created_at: datetime


class RunStatus(BaseModel):
    run_id: str
    pipeline_id: str
    status: Literal["queued", "running", "success", "failed"]
    started_at: datetime | None = None
    message: str | None = None


# --- Fake data ---

PIPELINES: list[Pipeline] = [
    Pipeline(id="pipe-001", name="snowflake_to_clickhouse_hr", status="active", created_at=datetime(2025, 1, 10)),
    Pipeline(id="pipe-002", name="dbt_silver_transform", status="active", created_at=datetime(2025, 2, 1)),
    Pipeline(id="pipe-003", name="cube_cache_refresh", status="paused", created_at=datetime(2025, 3, 15)),
    Pipeline(id="pipe-004", name="agent_eval_ingestion", status="error", created_at=datetime(2025, 4, 1)),
]

PIPELINE_INDEX = {p.id: p for p in PIPELINES}


# --- Endpoints ---

@app.get("/pipelines", response_model=list[Pipeline])
def list_pipelines():
    return PIPELINES


@app.post("/pipelines/{pipeline_id}/run", response_model=RunStatus)
def trigger_run(pipeline_id: str):
    if pipeline_id not in PIPELINE_INDEX:
        raise HTTPException(status_code=404, detail=f"Pipeline '{pipeline_id}' not found")

    pipeline = PIPELINE_INDEX[pipeline_id]

    if pipeline.status == "error":
        raise HTTPException(status_code=409, detail=f"Pipeline '{pipeline_id}' is in error state and cannot be run")

    return RunStatus(
        run_id=f"run-{random.randint(1000, 9999)}",
        pipeline_id=pipeline_id,
        status="queued",
        started_at=datetime.utcnow(),
        message="Run queued successfully",
    )


@app.get("/health")
def health():
    return {"status": "ok"}
