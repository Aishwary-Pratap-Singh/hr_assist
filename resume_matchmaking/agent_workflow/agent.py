from .agent_instruction import get_instruction_1
from decouple import config
import google.generativeai as genai
from decouple import config




def hr_agent(content):
    genai.configure(api_key=config("GEMINI_SECRET_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash") 
    response = model.generate_content(content)
    answer = response.text
    return answer

    

def create_agent(resume, jd):
    instructions1 = get_instruction_1(resume, jd)
    print("instruction: ", instructions1)
    hr_agent1 = hr_agent(instructions1)
    return hr_agent1


def send_email(match):
    if int(match) > 75:
        print("sending email...") 
    else:
        print("Did not qualify.")

def run_agent(resume, jd):
    response = create_agent(resume, jd)
    print( response, type(response))
    send_email(response)
    return response


