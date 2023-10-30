import os
import subprocess

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


if __name__ == '__main__':
    run_tests()