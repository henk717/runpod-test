"""Example handler file."""

import os
import subprocess

# If PORT_HEALTH is set, run the helper script and exit.
if "PORT_HEALTH" in os.environ:
    # Run the script and stop further execution
    subprocess.run(["/opt/koboldcpp/docker-helper.sh"], check=True)
    raise SystemExit

# Normal serverless behavior
import runpod


def handler(job):
    """Handler function that will be used to process jobs."""
    job_input = job["input"]

    name = job_input.get("name", "World")

    return f"Hello, {name}!"


runpod.serverless.start({"handler": handler})
