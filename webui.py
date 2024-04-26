import gradio as gr

from summarizer import load_document, setup_summarization_chain
from translator import setup_translator_chain


def summarize(url):
    docs = load_document(url)
    llm_chain = setup_summarization_chain()
    result = llm_chain.run(docs)

    return [result, gr.Button("🇹🇷 Translate ", visible=True)]


def translate(text):
    llm_chain = setup_translator_chain()
    result = llm_chain.run(text)
    return result


with gr.Blocks() as demo:
    gr.Markdown(
        """# Cobanov Web Summarizer
    Easily summarize any web page with a single click."""
    )

    with gr.Row():
        with gr.Column():
            url = gr.Text(label="URL", placeholder="Enter URL here")
            btn_generate = gr.Button("Generate")

            summary = gr.Markdown(label="Summary")
            btn_translate = gr.Button(visible=False)

    gr.Examples(
        [
            "https://cobanov.dev/haftalik-bulten/hafta-13",
            "https://bawolf.substack.com/p/embeddings-are-a-good-starting-point",
        ],
        inputs=[url],
    )
    gr.Markdown(
        """
        ```
        Model: llama3-8b
        Author: Mert Cobanov
        Contact: mertcobanov@gmail.com
        Repo: github.com/mertcobanov/easy-web-summarizer
        ```"""
    )
    btn_generate.click(summarize, inputs=[url], outputs=[summary, btn_translate])
    btn_translate.click(translate, inputs=[summary], outputs=[summary])


demo.launch()
