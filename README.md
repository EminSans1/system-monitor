# System Monitor

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Lightweight real-time CLI system monitor built with Python and `psutil`.

## Features

- Real-time CPU utilization with visual progress bar
- RAM usage with total/used/percent breakdown
- Disk usage statistics for root partition
- Top 5 processes sorted by CPU consumption
- Auto-refresh every 2 seconds
- Cross-platform: Windows, macOS, Linux
- Single dependency: `psutil`

## Installation

```bash
git clone https://github.com/EminSans1/system-monitor.git
cd system-monitor
pip install -r requirements.txt
```

## Usage

```bash
python system_monitor.py
```

Or install as a package:

```bash
pip install -e .
system-monitor
```

Press `Ctrl+C` to stop.

## Sample Output

```
╔══════════════════════════════════════════════════════════════════════╗
║                           SYSTEM MONITOR                            ║
╚══════════════════════════════════════════════════════════════════════╝
  Time: 2026-06-13 15:30:00

  CPU Usage: [████████░░░░░░░░░░░░░░░░░░░░░░░░] 25.3%

  Memory Usage: [██████████████████░░░░░░░░░░░░░░] 55.2%
    Used: 4.42 GB / 8.00 GB

  Disk Usage (/): [████████████████████████░░░░░░░░] 75.8%
    Used: 379.00 GB / 500.00 GB

  ----------------------------------------------------------
  Top 5 Processes by CPU Usage:
  ----------------------------------------------------------
  PID        Name                           CPU%       RAM%
  ---------- ------------------------------ ---------- ----------
  1234       chrome                         12.5       8.3
  5678       code                           8.2        5.1
  9012       node                           6.7        3.2
  3456       python                         4.3        2.1
  7890       slack                          3.1        4.5

  Press Ctrl+C to exit
```

## Development

### Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install pytest pytest-cov
```

### Tests

```bash
pytest
pytest --cov=system_monitor --cov-report=html
```

## Project Structure

```
system-monitor/
├── system_monitor.py          # Main application
├── requirements.txt           # Dependencies
├── setup.py                   # Package setup
├── pyproject.toml             # Build config
├── tests/
│   ├── __init__.py
│   └── test_system_monitor.py
├── LICENSE
├── README.md
└── .gitignore
```

## Contributing

1. Fork the repository
2. Create your branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License — see [LICENSE](LICENSE) for details.

## Acknowledgments

- [psutil](https://github.com/giampaolo/psutil) — cross-platform process and system monitoring
