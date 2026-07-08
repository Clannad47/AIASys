"""Node.js 运行时工具函数单元测试。"""

import pytest

from app.services.node_runtime import _parse_fnm_list_versions


@pytest.mark.parametrize(
    "stdout,expected",
    [
        ("* v22.15.0 default\n* v20.15.1\n", ["22.15.0", "20.15.1"]),
        ("v18.20.4\nv20.15.0\n", ["18.20.4", "20.15.0"]),
        ("* v22.15.0\n", ["22.15.0"]),
        ("", []),
        ("no versions here", []),
        ("v22.15.0 lts\nv23.0.0 latest\n", ["22.15.0", "23.0.0"]),
    ],
)
def test_parse_fnm_list_versions(stdout: str, expected: list[str]) -> None:
    assert _parse_fnm_list_versions(stdout) == expected
