from dataclasses import dataclass
from typing import List
import numpy as np

@dataclass
class Solution:
    """TSP solution."""

    path: List[int]
    points: np.ndarray

    @property
    def tour(self):
        """Return the tour."""
        return self.path

    @property
    def optimal_value(self):
        """Return the total length of the tour."""
        # 使用numpy的diff函数计算路径中每两个连续点之间的差值
        diffs = np.diff(self.points[self.path], axis=0)
        # 使用numpy的linalg.norm函数计算每个差值的范数（即长度），然后求和
        total_length = np.sum(np.linalg.norm(diffs, axis=1))
        return total_length

    @property
    def found_tour(self):
        """Return the found tour."""
        return self.path is not None