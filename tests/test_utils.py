"""测试统计工具函数"""

import pytest
from llm_stress_test_cli.utils import calculate_percentile, format_latency, calculate_success_rate


def test_calculate_percentile():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert calculate_percentile(data, 50) == 3.0
    assert calculate_percentile([], 50) == 0.0


def test_format_latency():
    assert format_latency(0.123) == "123.0ms"
    assert format_latency(1.5) == "1500.0ms"


def test_calculate_success_rate():
    assert calculate_success_rate(100, 95) == 95.0
    assert calculate_success_rate(0, 0) == 0.0
