from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="**********"
)

result = client.run_workflow(
    workspace_name="bicycle-parts",
    workflow_id="detect-count-and-visualize-2",
    images={
        "image": "YOUR_IMAGE.jpg"
    },
    use_cache=True # cache workflow definition for 15 minutes
)
