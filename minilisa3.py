import subprocess

class TestFailure(Exception):
    pass


class BaseTest:
    name = "base"

    def run(self):
        output = subprocess.run(
            ["echo", "Hello from Bash"],
            capture_output=True,
            text=True
        )

        # Check:
        # 1. Command succeeded (returncode == 0)
        # 2. No error output
        # 3. Expected stdout (note the newline)
        if (
            output.returncode == 0
            and output.stderr == ""
            and output.stdout == "Hello from Bash\n"
        ):
            return "test passed"
        else:
            raise TestFailure("test failed")
