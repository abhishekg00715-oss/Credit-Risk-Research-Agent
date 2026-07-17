"""
query_logger.py

Purpose
-------
Log incoming user queries before they are
processed by the Coordinator Agent.

Responsibilities
----------------
- Persist user queries
- Record detected agents
- Record customer identifier
- Maintain append-only JSON log

Future Enhancements
-------------------
- Central logging configuration
- Log rotation
- External logging providers

Author
------
Credit Risk Research Agent
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional


class QueryLogger:
    """
    Logs incoming user queries.

    Log records are persisted as JSON Lines
    to support simple inspection and future
    analytics.
    """

    DEFAULT_LOG_DIRECTORY = (
        Path(__file__).resolve().parents[2]
        / "logs"
    )

    DEFAULT_LOG_FILE = (
        DEFAULT_LOG_DIRECTORY
        / "query_logs.jsonl"
    )

    def __init__(
        self,
        log_file: Path | None = None
    ) -> None:
        """
        Initialize logger.
        """

        self.log_file = (
            log_file
            if log_file
            else self.DEFAULT_LOG_FILE
        )

        self.log_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def log_query(
        self,
        query: str,
        agents: List[str],
        customer_id: Optional[str] = None
    ) -> None:
        """
        Persist a user query.

        Parameters
        ----------
        query : str
            Original user request.

        agents : List[str]
            Agents selected by the
            Intent Routing Service.

        customer_id : str, optional
            Extracted customer identifier.
        """

        log_record = self._build_log_record(
            query=query,
            agents=agents,
            customer_id=customer_id
        )

        self._write_record(
            log_record
        )

    # ---------------------------------------------------------
    # Helper Methods
    # ---------------------------------------------------------

    def _build_log_record(
        self,
        query: str,
        agents: List[str],
        customer_id: Optional[str]
    ) -> dict:
        """
        Build a structured log record.
        """

        return {

            "timestamp": (
                datetime.utcnow()
                .isoformat(timespec="seconds")
            ),

            "query": query,

            "agents": agents,

            "customer_id": customer_id

        }

    def _write_record(
        self,
        record: dict
    ) -> None:
        """
        Append record to log file.

        Logging failures should never
        interrupt the application.
        """

        try:

            with open(
                self.log_file,
                "a",
                encoding="utf-8"
            ) as log_file:

                json.dump(
                    record,
                    log_file
                )

                log_file.write("\n")

        except Exception as exc:

            print(
                f"Query logging failed: {exc}"
            )
