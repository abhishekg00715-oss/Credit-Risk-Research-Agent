"""
agent_execution_logger.py

Purpose
-------
Persist agent execution details to support
traceability, debugging and performance
monitoring.

Responsibilities
----------------
- Record agent execution metadata
- Measure execution duration
- Persist execution logs as JSON
- Support future workflow tracing

Author
------
Credit Risk Research Agent
"""

from __future__ import annotations

import json
import uuid

from datetime import datetime
from pathlib import Path
from typing import Any


class AgentExecutionLogger:
    """
    Logger responsible for recording
    agent execution details.
    """

    LOG_DIRECTORY = (
        Path(__file__).resolve().parent / "logs"
    )

    LOG_FILE = (
        LOG_DIRECTORY / "agent_execution_log.json"
    )

    def __init__(self):

        self.LOG_DIRECTORY.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.LOG_FILE.exists():

            self.LOG_FILE.write_text(
                "[]",
                encoding="utf-8"
            )

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def create_correlation_id(
        self
    ) -> str:
        """
        Generate a unique request identifier.
        """

        return str(uuid.uuid4())

    def log_execution(
        self,
        correlation_id: str,
        agent_name: str,
        input_summary: Any,
        response: Any,
        execution_time_ms: float,
        success: bool,
        error_message: str | None = None
    ) -> None:
        """
        Persist a single agent execution.
        """

        log_entry = {

            "timestamp": (
                datetime.utcnow().isoformat()
            ),

            "correlation_id": correlation_id,

            "agent": agent_name,

            "status": (
                "SUCCESS"
                if success
                else "FAILED"
            ),

            "execution_time_ms": round(
                execution_time_ms,
                2
            ),

            "input": input_summary,

            "response_summary": (
                self._summarize_response(
                    response
                )
            ),

            "error_message": error_message

        }

        logs = self._load_logs()

        logs.append(
            log_entry
        )

        self.LOG_FILE.write_text(

            json.dumps(
                logs,
                indent=4
            ),

            encoding="utf-8"

        )

    # ---------------------------------------------------------
    # Helper Methods
    # ---------------------------------------------------------

    def _load_logs(
        self
    ) -> list:

        try:

            return json.loads(

                self.LOG_FILE.read_text(
                    encoding="utf-8"
                )

            )

        except Exception:

            return []

    def _summarize_response(
        self,
        response: Any
    ) -> Any:
        """
        Avoid persisting large payloads.
        """

        if isinstance(response, dict):

            summary = {}

            if "success" in response:

                summary["success"] = (
                    response["success"]
                )

            if "message" in response:

                summary["message"] = (
                    response["message"]
                )

            if "risk_summary" in response:

                risk = response["risk_summary"]

                if isinstance(risk, dict):

                    summary["overall_risk"] = (
                        risk.get(
                            "overall_risk"
                        )
                    )

            return summary

        return str(response)[:250]
