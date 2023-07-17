import cohere
import gradio as gr
co = cohere.Client('BZY3Z23n0BvI984Zf43VwLvpWbXXxprrAHYd5skS') # This is your trial API key
def write_post(topic):
  response = co.generate(
  model='command',
  prompt=f'write a poem to generate AI \"{topic}\":',
  max_tokens=42,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
  return('Prediction: {}'.format(response.generations[0].text))

with gr.Blocks() as demo:
    gr.Markdown("AI generated Blogpost with Cohere API")
    inp = gr.Textbox(placeholder="Enter your topic for blog post")
    btn = gr.Button("Generate")
    out = gr.Textbox()
    btn.click(fn=write_post, inputs=inp, outputs=out)