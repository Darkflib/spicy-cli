# Spicy CLI

A modern Python command-line interface with multiple commands.

## Features

- Multiple commands with subcommands
- Rich terminal output with colors and formatting
- Configuration management
- Detailed help text for all commands
- Type annotations and validation
- Automatic shell completion

## Installation

For regular use, install with pipx:

```bash
pipx install spicy-cli
```

For development:

```bash
git clone https://github.com/darkflib/spicy-cli.git
cd spicy-cli
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e '.[dev]'
```

## Usage

Show help:

```bash
spicy --help
```

Show version:

```bash
spicy --version
# or
spicy version
```

### Command 1

Run command 1:

```bash
spicy command1 run "Your Name"
spicy command1 run --formal --count 3 "Your Name"
```

Check status:

```bash
spicy command1 status
spicy command1 status --verbose
```

### Command 2

Process files:

```bash
spicy command2 process file1.txt file2.txt
spicy command2 process --output result.txt --force file1.txt file2.txt file3.invalid
```

List items:

```bash
spicy command2 list
spicy command2 list --limit 5 --all
```

### Configuration

Show current configuration:

```bash
spicy config show
```

Change a setting:

```bash
spicy config set timeout 60
spicy config set debug true
```

Reset to defaults:

```bash
spicy config reset
```

### Plugins

List available plugins:

```bash
spicy plugin list
```

Create a new plugin template:

```bash
spicy plugin create "My Plugin" -o my_plugin.py
```

Install a plugin:

```bash
spicy plugin install my_plugin.py
```

Uninstall a plugin:

```bash
spicy plugin uninstall my-plugin
```

#### Example Plugin: Weather

The project includes an example weather plugin in the `examples` directory:

```bash
# Install the example plugin
spicy plugin install examples/weather_plugin.py

# Get current weather
spicy weather current "London, UK"
spicy weather current "New York" --fahrenheit

# Get forecast
spicy weather forecast "Tokyo" --days 5
```

## Development

### Development Scripts

The project includes convenient scripts for common development tasks:

```bash
# On Unix/Linux/Mac:
./scripts/run.sh lint     # Run all linting tools
./scripts/run.sh format   # Format code with black and isort
./scripts/run.sh test     # Run tests with coverage
./scripts/run.sh clean    # Clean build artifacts
./scripts/run.sh build    # Build the package
./scripts/run.sh install  # Install in development mode
./scripts/run.sh run      # Run the CLI (e.g. './scripts/run.sh run --help')
./scripts/run.sh help     # Show help

# On Windows:
scripts\run.bat lint
scripts\run.bat format
# etc.
```

These scripts automatically create and use a virtual environment with uv.

### Testing

Run tests with pytest:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=spicy_cli
```

### Formatting and Type Checking

Format code with black:

```bash
black .
```

Sort imports:

```bash
isort .
```

Type check with mypy:

```bash
mypy .
```

Lint with ruff:

```bash
ruff check .
```

Lint with pylint (with 120 char line length):

```bash
pylint src/ tests/
```

## Docker

To run Spicy CLI in a Docker container, you can use the provided Dockerfile. This allows you to run the CLI without needing to install Python or its dependencies on your local machine.

### Build and Run

To build and run the Docker container, you can use Docker Compose. The provided `docker-compose.yml` file sets up the environment for you.

Build and run with Docker compose:

```bash
docker-compose up --build
```

Run a specific command:

```bash
docker-compose run spicy-cli command1 run "Docker User"
```

### Build and Run for multiarch support

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t spicy-cli:latest --push .
docker run --rm -it spicy-cli:latest
```

## License

MIT
