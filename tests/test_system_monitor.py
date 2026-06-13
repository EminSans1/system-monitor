import sys
import os
from unittest import mock

import psutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from system_monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_top_processes,
    format_size,
    progress_bar,
)


def test_get_cpu_usage():
    with mock.patch("psutil.cpu_percent", return_value=45.5):
        assert get_cpu_usage() == 45.5


def test_get_memory_usage():
    mock_mem = mock.Mock()
    mock_mem.total = 8 * 1024 ** 3
    mock_mem.used = 4 * 1024 ** 3
    mock_mem.percent = 50.0
    with mock.patch("psutil.virtual_memory", return_value=mock_mem):
        result = get_memory_usage()
        assert result["total"] == 8.0
        assert result["used"] == 4.0
        assert result["percent"] == 50.0


def test_get_disk_usage():
    mock_disk = mock.Mock()
    mock_disk.total = 500 * 1024 ** 3
    mock_disk.used = 250 * 1024 ** 3
    mock_disk.percent = 50.0
    with mock.patch("psutil.disk_usage", return_value=mock_disk):
        result = get_disk_usage()
        assert result["total"] == 500.0
        assert result["used"] == 250.0
        assert result["percent"] == 50.0


def test_get_top_processes():
    mock_proc = mock.Mock()
    mock_proc.info = {
        "pid": 1234,
        "name": "python",
        "cpu_percent": 25.0,
        "memory_percent": 5.0,
    }
    with mock.patch("psutil.process_iter", return_value=[mock_proc]):
        result = get_top_processes(1)
        assert len(result) == 1
        assert result[0]["pid"] == 1234


def test_get_top_processes_skips_invalid():
    good_proc = mock.Mock()
    good_proc.info = {
        "pid": 1,
        "name": "init",
        "cpu_percent": 0.1,
        "memory_percent": 0.01,
    }
    bad_proc = mock.Mock()
    bad_proc.info = {
        "pid": 2,
        "name": "dead",
        "cpu_percent": None,
        "memory_percent": 0.0,
    }
    with mock.patch("psutil.process_iter", return_value=[good_proc, bad_proc]):
        result = get_top_processes(5)
        assert len(result) == 1
        assert result[0]["pid"] == 1


def test_get_top_processes_handles_access_denied():
    good_proc = mock.Mock()
    good_proc.info = {
        "pid": 1,
        "name": "init",
        "cpu_percent": 0.1,
        "memory_percent": 0.01,
    }
    bad_proc = mock.Mock()
    type(bad_proc).info = mock.PropertyMock(side_effect=psutil.AccessDenied(1, "read"))
    with mock.patch("psutil.process_iter", return_value=[good_proc, bad_proc]):
        result = get_top_processes(5)
        assert len(result) == 1
        assert result[0]["pid"] == 1


def test_format_size():
    assert format_size(1.0) == "1.00 GB"
    assert format_size(1024.567) == "1024.57 GB"
    assert format_size(0.5) == "0.50 GB"


def test_progress_bar():
    bar = progress_bar(50)
    assert "\u2588" in bar
    assert "\u2591" in bar
    assert "50.0%" in bar


def test_progress_bar_full():
    bar = progress_bar(100)
    assert "\u2588" * 30 in bar
    assert "100.0%" in bar


def test_progress_bar_empty():
    bar = progress_bar(0)
    assert "\u2591" * 30 in bar
    assert "0.0%" in bar
