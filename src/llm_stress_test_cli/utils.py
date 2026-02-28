"""统计工具函数"""

import numpy as np
from typing import List


def calculate_percentile(data: List[float], percentile: int) -> float:
    """计算百分位数"""
    if not data:
        return 0.0
    return float(np.percentile(data, percentile))


def format_latency(seconds: float) -> str:
    """格式化延迟显示(ms)"""
    return f"{seconds * 1000:.1f}ms"


def calculate_success_rate(total: int, success: int) -> float:
    """计算成功率"""
    if total == 0:
        return 0.0
    return (success / total) * 100
