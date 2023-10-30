import os
import subprocess

def generate_html_report(passed, failed):
    report = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
            }}
            .passed {{
                color: green;
            }}
            .failed {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <h1>Test Results</h1>
        <p>Total tests executed: {len(passed) + len(failed)}</p>
        <p class="passed">Tests passed: {len(passed)}</p>
        <ul>
    """

    for path in passed:
        report += f"            <li class='passed'>{path}</li>\n"

    report += f"""
        </ul>
        <p class="failed">Tests failed: {len(failed)}</p>
        <ul>
    """

    for path in failed:
        report += f"            <li class='failed'>{path}</li>\n"

    report += """
        </ul>
    </body>
    </html>
    """

    with open("index.html", "w") as html_file:
        html_file.write(report)

    print(f"\nThe report is also updated to the index.html file.")

def run_tests():
    GREEN = "\033[32m"
    RED = "\033[31m"
    RESET = "\033[0m"

    print("\nRunning tests...")

    total = 0
    passed = []
    failed = []

    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.startswith('test') and file.endswith('.py'):
                path = os.path.join(root, file)

                result = subprocess.run(['python3', path], capture_output=True, text=True)
                
                if "FAILED" in result.stderr:
                    failed.append(path)
                else:
                    passed.append(path)

                total += 1

    print(f"\nRan all {total} test files and here's the result:")
    
    print(GREEN + f"\nPassed: {len(passed)}" + RESET)
    for path in passed:
        print(f"    {path}")

    print(RED + f"\nFailed: {len(failed)}" + RESET)
    for path in failed:
        print(f"    {path}")

    generate_html_report(passed, failed)

if __name__ == '__main__':
    run_tests()
