from pathlib import Path

from haystack import Pipeline
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import BM25Retriever, MarkdownConverter, PromptNode, PromptTemplate


def query_markdown_docs(query: str) -> str:
    markdown_files_directory_paths = ["src/docs"]

    # Initialize document store and markdown converter
    document_store = InMemoryDocumentStore(use_bm25=True)
    converter = MarkdownConverter(remove_numeric_tables=True, valid_languages=["en"])

    # Search for markdown files and convert them to documents
    for directory_path in markdown_files_directory_paths:
        directory = Path(directory_path)
        if directory.exists() and directory.is_dir():
            for markdown_file_path in directory.rglob("*.md"):
                docs = converter.convert(file_path=str(markdown_file_path), meta=None)

                if isinstance(docs, dict):
                    docs = [docs]
                document_store.write_documents(docs)

    # Initialize the retriever
    retriever = BM25Retriever(document_store=document_store)

    # Define the prompt template for question answering
    qa_template = PromptTemplate(
        prompt="""Using only the information contained in the context,
answer only the question asked without adding suggestions of possible questions and answer exclusively in Italian.
If the answer cannot be deduced from the context, reply: 'I don't know because it is not relevant to the Context.'
Context: {join(documents)};
Question: {query}"""
    )

    prompt_node = PromptNode(
        model_name_or_path="mistralai/Mixtral-8x7B-Instruct-v0.1",
        api_key="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",
        default_prompt_template=qa_template,
        max_length=500,
        model_kwargs={"model_max_length": 7000},
    )
    pipeline = Pipeline()
    pipeline.add_node(component=retriever, name="retriever", inputs=["Query"])
    pipeline.add_node(component=prompt_node, name="prompt_node", inputs=["retriever"])

    def print_answer(out):
        return print(out["results"][0].strip())

    print_answer(pipeline.run(query=query))

    output = pipeline.run(query=query)

    try:
        answer = output["results"][0].strip()
    except IndexError:
        answer = "No answer found."

    return answer


# answer = query_markdown_docs("What is a Pod?")
