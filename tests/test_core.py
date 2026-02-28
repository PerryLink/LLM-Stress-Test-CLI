"""测试核心压测引擎"""

import pytest
from llm_stress_test_cli.core import RequestMetrics


def test_request_metrics_creation():
    metric = RequestMetrics()
    assert metric.ttft == 0.0
    assert metric.total_latency == 0.0
    assert metric.tokens_generated == 0
    assert metric.success is False
    assert metric.error is None


def test_request_metrics_with_values():
    metric = RequestMetrics(
        ttft=0.1,
        total_latency=1.5,
        tokens_generated=50,
        success=True
    )
    assert metric.ttft == 0.1
    assert metric.total_latency == 1.5
    assert metric.tokens_generated == 50
    assert metric.success is True
