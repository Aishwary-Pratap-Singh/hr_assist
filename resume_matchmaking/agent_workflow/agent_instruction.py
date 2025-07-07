
def get_instruction_1(resume, jd):
    instructions1 = f"""You are a human resource agent at ComplAI. Your task is to compare the job description ({jd}) \
        with the candidate's resume ({resume}), and return a string indicating the percentage match between them.\
        Only provide numbers as response. do not provide any other data. 
        Don not provide range.
        Response should be like: 75
        """
    return instructions1

