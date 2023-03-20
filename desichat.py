import gradio as gr
import openai

openai.api_key="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"


message_history = [ {"role": "system", "content": "You are a chat bot named raven that sarcastically communicates in roman urdu. Don't use any hindi words and always give the answer if you have it otherwise sarcasitcally say i dont't know"},
        {"role": "user", "content": "Tumhara naam kya hai?"}, 
        {"role": "assistant", "content": "Mera naam raven hai. Tumse matlab?"},]

def predict(inp):
    global message_history
    message_history.append({"role": "user", "content": f"{inp}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history,
    )
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": f"{reply_content}"}) 
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(3, len(message_history)-1, 2)]  
    return response 

with gr.Blocks() as demo: 

    # creates a new Chatbot instance and assigns it to the variable chatbot.
    chatbot = gr.Chatbot() 

    # creates a new Row component, which is a container for other components.
    with gr.Row(): 

        txt = gr.Textbox(show_label=False, placeholder="Enter text and press enter").style(container=False)

    txt.submit(predict, txt, chatbot) # submit(function, input, output)
    txt.submit(None, None, txt, _js="() => {''}") # No function, no input to that function, submit action to textbox is a js function that returns empty string, so it clears immediately.
         
demo.launch()



  