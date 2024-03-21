import gradio as gr
from summarizer import setup_summarization_chain, load_document


def summarize(url):
    docs = load_document(url)
    llm_chain = setup_summarization_chain()
    result = llm_chain.run(docs)
    return result


iface = gr.Interface(
    fn=summarize,
    inputs="text",
    outputs="text",
    title="Summarizer",
    description="Enter a URL to get a summary of the document.",
)

iface.launch()