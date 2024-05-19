import streamlit as st
from openai import OpenAI

client = OpenAI()

assistant_id = "asst_u6Y31LBDpGM9yr4cHR6C0CuK"

def main():

    st.image("logo.png", caption="Linkedin: linkedin.com/in/vincent-julian-rost | Datenschutz: https://github.com/vinro04/Ai-consultant/tree/main", use_column_width=True)
    st.title("Virtueller AI Consultant")
    st.text("Mit dieser App kannst du individuelle KI Strategien entwickeln lassen und neue Tools\nfür deinen Anwendungsbereich finden! Beschreibe einfach dein Problem in der Textbox\nund erhalte Vorschläge wie sich deine Arbeit erleichtern lässt.")

    user_input = st.text_input("Beschreibe dein Problem hier:")

    if st.button("Enter"):
        answer = gpt_call(assistant_id=assistant_id, user_input=user_input)
        st.write(answer)


def gpt_call(assistant_id, user_input):
    
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
      thread_id=thread.id,
      role="user",
      content= f"{user_input}",
    )

    run = client.beta.threads.runs.create_and_poll(
      thread_id=thread.id,
      assistant_id=assistant_id,
    )

    if run.status == 'completed': 
      messages = client.beta.threads.messages.list(
      thread_id=thread.id
      )
      
      return messages.data[0].content[0].text.value


main()
