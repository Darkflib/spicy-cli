import re
from typer.testing import CliRunner
from spicy_cli.main import app # Assuming 'app' is your main Typer application

runner = CliRunner()

# Regex to validate a UUID
UUID_PATTERN = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')

def is_valid_uuid(uuid_string):
    return bool(UUID_PATTERN.match(uuid_string))

def test_uuid_generate_default():
    """Test generating a single UUID (default behavior)."""
    result = runner.invoke(app, ["uuid", "generate"])
    assert result.exit_code == 0
    output_lines = result.stdout.strip().split('\n')
    assert len(output_lines) == 1
    assert is_valid_uuid(output_lines[0])

def test_uuid_generate_multiple():
    """Test generating multiple UUIDs using the -n option."""
    count = 5
    result = runner.invoke(app, ["uuid", "generate", "-n", str(count)])
    assert result.exit_code == 0
    output_lines = result.stdout.strip().split('\n')
    assert len(output_lines) == count
    for line in output_lines:
        assert is_valid_uuid(line)

def test_uuid_generate_custom_count():
    """Test generating a specific number of UUIDs (e.g., 3)."""
    count = 3
    result = runner.invoke(app, ["uuid", "generate", "--count", str(count)])
    assert result.exit_code == 0
    output_lines = result.stdout.strip().split('\n')
    assert len(output_lines) == count
    for line in output_lines:
        assert is_valid_uuid(line)

def test_uuid_generate_invalid_count_zero():
    """Test generating UUIDs with an invalid count (0)."""
    result = runner.invoke(app, ["uuid", "generate", "-n", "0"])
    assert result.exit_code == 1
    assert "Error: Number of UUIDs must be at least 1." in result.stdout

def test_uuid_generate_invalid_count_negative():
    """Test generating UUIDs with an invalid negative count."""
    result = runner.invoke(app, ["uuid", "generate", "-n", "-5"])
    assert result.exit_code == 1
    assert "Error: Number of UUIDs must be at least 1." in result.stdout

# It might also be useful to test the help message for the command
def test_uuid_generate_help():
    """Test the help message for the uuid generate command."""
    result = runner.invoke(app, ["uuid", "generate", "--help"])
    assert result.exit_code == 0
    assert "Generate one or more UUIDs." in result.stdout
    assert "--count, -n INTEGER" in result.stdout
