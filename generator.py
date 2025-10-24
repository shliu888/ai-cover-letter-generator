import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
llm = init_chat_model("google_genai:gemini-2.0-flash")

from typing_extensions import TypedDict

from langgraph.graph import StateGraph,END
from langchain_core.messages import SystemMessage, HumanMessage


class State(TypedDict):
    resume: str
    cover_letter: str

workflow=StateGraph(State)

def cover_letter(state: State):
    sys_prompt=SystemMessage("You are a resume coach. You are to take a resume, and write the best possible cover letter that you can write. You can only use things that are on the resume. ")
    msg=[sys_prompt, HumanMessage(content=f"Resume: {state['resume']}")]
    letter=llm.invoke(msg).content
    return {"cover_letter":letter}

workflow.add_node("make_cover", cover_letter)
workflow.set_entry_point("make_cover")

try:
    app = workflow.compile()
except Exception as e:
    print("[error] failed to compile workflow:", e)
    raise

while True:
    try:
        resume = input("Enter your resume (or type 'exit' to quit): ")
    except EOFError:
        break
    if resume.strip().lower() == 'exit':
        break
    initial_state = {"resume": resume}
    try:
        result = app.invoke(initial_state)
    except Exception as e:
        print("[error] workflow invocation failed:", e)
        continue
    print("\n--- COVER LETTER ---\n")
    print(result.get("cover_letter", "(no cover letter returned)"))
    print("\n" + "="*40 + "\n")
