
import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import EchoWorkflow

async def main():
    client = await Client.connect("temporal:7233")
    worker = Worker(client, task_queue="demo-queue", workflows=[EchoWorkflow])
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
