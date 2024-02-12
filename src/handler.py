import runpod

from rag import query_markdown_docs

log = runpod.RunPodLogger()


async def async_generator_handler(job):
    """Handler function that will be used to process jobs with the Llama model."""
    try:
        job_input = job["input"]

        # Assuming the input contains a 'prompt' key for the Llama model
        prompt = job_input.get("prompt", "")

        # Perform inference using the rag model
        output = query_markdown_docs(prompt)

        return output

    except Exception as e:
        log.error(f"Error: {str(e)}")
        return f"Error: {str(e)}"


runpod.serverless.start(
    {"handler": async_generator_handler, "return_aggregate_stream": True}
)
