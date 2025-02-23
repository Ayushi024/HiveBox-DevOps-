"""
Unit test for verifying the application version output.
"""

import subprocess


def test_version():
    """Test that app.py prints the correct version."""
    result = subprocess.run(
        ["python", "basic_versioning/app.py"], capture_output=True, text=True
    )
    assert result.returncode == 0
    assert "App Version: v0.0.1" in result.stdout
