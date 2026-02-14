
from temporalio import workflow

@workflow.defn
class EchoWorkflow:
    @workflow.run
    async def run(self, text: str) -> str:
        return f"Echo from Temporal Agent: {text}"
