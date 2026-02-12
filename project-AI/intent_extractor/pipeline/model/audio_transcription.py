import requests
import os
import time
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("PYANNOTE")

class Transcribe:
    def __init__(self, url):
        self.url = url
        self.headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
        }

        self.data = {
            "url": self.url,
            "transcription": True
        }


    def transcribe_text(self):
        response = requests.post(
            "https://api.pyannote.ai/v1/diarize",
            headers=self.headers,
            json=self.data
        )

        if response.status_code != 200:
            print("Error creating job:", response.text)
            exit()

        job_id = response.json()["jobId"]
        print("Job created:", job_id)

        while True:
            response = requests.get(
                f"https://api.pyannote.ai/v1/jobs/{job_id}",
                headers=self.headers
            )

            if response.status_code != 200:
                print("Error checking job:", response.text)
                break

            job_data = response.json()
            status = job_data["status"]

            if status == "succeeded":
                print("Job completed successfully!")
                output = job_data["output"]
                break

            elif status in ["failed", "canceled"]:
                print("Job failed or canceled.")
                break

            print("Waiting...")
            time.sleep(5)



        if status == "succeeded":
            for turn in output["turnLevelTranscription"]:
                words = turn["text"].split()
                for word in words:
                    print(word, end=" ", flush=True)
                    time.sleep(0.08)

            print()

