import argparse
import sys

templates = {
    "python": [
        "*.pyc",
        "__pycache__/",
        ".env",
        ".venv/",
        "env/",
        "venv/",
    ],
    "node": [
        "node_modules/",
        "npm-debug.log*",
        "yarn-debug.log*",
        "yarn-error.log*",
        ".env",
    ],
    "macos": [
        ".DS_Store",
        "Thumbs.db",
    ],
    "java": [
        "*.class",
        "target/",
    ],
    "rust": [
        "target/",
    ],
    "go": [
        "*.exe",
    ],
    "docker": [
        "*.dockerignore",
    ],
}

def main():
    parser = argparse.ArgumentParser(
        description="Generate .gitignore by combining unique lines from predefined templates."
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available templates"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "templates",
        nargs="*",
        help="Template names to combine (e.g. python node)"
    )
    args = parser.parse_args()

    if args.list:
        print("\n".join(sorted(templates.keys())))
        sys.exit(0)

    if not args.templates:
        parser.print_help()
        sys.exit(0)

    unknown_templates = [t for t in args.templates if t not in templates]
    if unknown_templates:
        print(
            f"Error: Unknown templates: {', '.join(unknown_templates)}. "
            f"Use --list to see available.",
            file=sys.stderr
        )
        sys.exit(1)

    lines = []
    seen = set()
    for template_name in args.templates:
        for line in templates[template_name]:
            if line not in seen:
                seen.add(line)
                lines.append(line)

    content = "\n".join(lines) + "\n"

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to {args.output}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        sys.stdout.write(content)

    sys.exit(0)

if __name__ == "__main__":
    main()
