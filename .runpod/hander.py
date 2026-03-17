try:
    import runpod
    import time
    def handler(event):
        time.sleep(10)
        result = "Hi! Want to use KoboldCpp on serverless? You can! But it must be a load balanced instance, this is the only thing we support."
        
        # Return the result
        return result

    runpod.serverless.start({"handler": handler})
except:
    import os
    import json
    import requests
    import time
    # -------------------------------------------------------------------
    # Fake environment variables that RunPod normally injects
    # Replace these with real values if you want to test against RunPod.
    # -------------------------------------------------------------------
    RUNPOD_JOB_ID = os.getenv("RUNPOD_JOB_ID", "test-job-123")
    RUNPOD_ENDPOINT = os.getenv(
        "RUNPOD_RESULT_URL",
        f"https://api.runpod.io/v2/YOUR_ENDPOINT_ID/jobs/{RUNPOD_JOB_ID}/result"
    )
    RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY", "FAKE_API_KEY")


    def send_result(job_id, result):
        """Send a result payload back to RunPod, just like the SDK does."""
        payload = {
            "id": job_id,
            "status": "COMPLETED",
            "output": result
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {RUNPOD_API_KEY}"
        }

        print("Sending result to:", RUNPOD_ENDPOINT)
        print("Payload:", payload)

        response = requests.post(
            RUNPOD_ENDPOINT,
            headers=headers,
            data=json.dumps(payload)
        )

        print("Response status:", response.status_code)
        print("Response body:", response.text)


    # -------------------------------------------------------------------
    # Fake handler logic — this is where you'd normally process a job
    # -------------------------------------------------------------------
    def handler():
        # Pretend we did some work
        time.sleep(10)
        result = {"message": "Hi! Want to use KoboldCpp on serverless? You can! But it must be a load balanced instance, this is the only thing we support.}

        # Send result back to RunPod
        send_result(RUNPOD_JOB_ID, result)


    handler()

