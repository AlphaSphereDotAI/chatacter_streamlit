import gradio as gr

with gr.Blocks() as app:
    gr.Text("😀 Chatacter Alpha Version")
    gr.Text("This is a simple character chatting app. Now we only support Napoleon Bonaparte")
    gr.Button(value="Start Chatting with Napoleon Bonaparte",)
    
    
app.launch()

# st.title("😀 Chatacter Alpha Version")
# st.write(
#     "This is a simple character chatting app. Now we only support Napoleon Bonaparte"
# )

# if st.button("Start Chatting with Napoleon Bonaparte"):
#     st.switch_page("pages/napoleon.py")
