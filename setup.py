from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="system-monitor-cli",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A real-time CLI system monitor built with psutil",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["system_monitor"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.8",
    install_requires=[
        "psutil>=5.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "system-monitor=system_monitor:main",
        ],
    },
)
