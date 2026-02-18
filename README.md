# gitignore-generator

A simple, lightweight CLI tool for generating `.gitignore` files by merging unique lines from predefined templates for common languages and environments (e.g., Python, Node.js, macOS). Templates are combined while preserving input order and eliminating duplicates, with robust error handling for unknown templates and I/O issues.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gitignore-generator.git
   cd gitignore-generator
   ```

2. No external dependencies required (uses Python standard library).

3. Run directly:
   ```
   python src/gitignore_generator.py --help
   ```

## Usage

```
usage: gitignore_generator.py [-h] [--list] [--output OUTPUT] [templates ...]

Generate .gitignore by combining unique lines from predefined templates.

positional arguments:
  templates        Template names to combine (e.g. python node)

options:
  -h, --help       show this help message and exit
  --list           List available templates
  --output OUTPUT, -o OUTPUT
                   Output file path (default: stdout)
```

### Examples

- List available templates:
  ```
  python src/gitignore_generator.py --list
  ```
  Output:
  ```
  docker
  go
  java
  macos
  node
  python
  rust
  ```

- Generate for Python and Node (outputs to stdout):
  ```
  python src/gitignore_generator.py python node
  ```

- Output to file for macOS:
  ```
  python src/gitignore_generator.py --output .gitignore macos
  ```

If no templates are provided (and `--list` not used), the help message is shown automatically.

Available templates: `docker`, `go`, `java`, `macos`, `node`, `python`, `rust`.

## Features

- **Template listing**: `--list` to view all available templates.
- **Merged generation**: Combine multiple templates, preserving order and removing duplicates.
- **Flexible output**: Write to file (`--output`) or stdout.
- **User-friendly UX**: Auto-help on empty args, clear errors for unknown templates (suggest `--list`).
- **Robust handling**: IO errors and validation with appropriate exits.

## Dependencies

- Python 3.x (standard library: `argparse`, `sys`)

## Contributing

Contributions welcome! Fork, make changes in `src/`, and submit a PR. Add tests via example runs if extending.

## License

MIT