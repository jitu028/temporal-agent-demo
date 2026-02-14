from fastapi import FastAPI
from temporalio.client import Client
import uuid

app = FastAPI()

@app.get("/run/{text}")
async def run_workflow(text: str):
    client = await Client.connect("temporal:7233")

    handle = await client.start_workflow(
        "EchoWorkflow",
        text,
        id=f"wf-{text}-{uuid.uuid4()}",
        task_queue="demo-queue",
    )

    result = await handle.result()
    return {"result": result}
