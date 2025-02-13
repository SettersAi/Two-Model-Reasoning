import openai
from groq import Groq

# Set up the API keys for OpenAI (ChatGPT) and Groq AI
openai.api_key = "Add OpenAi Api key here."
groq_client = Groq(api_key="Add Groq Api key here.")

def interactive_dialogue(model1, model2, prompt):
    """Multi-model concise reasoning with self-reflection."""
    try:
        dialogue_history = ""

        # First round: Initial response
        response_model1 = openai.ChatCompletion.create(
            model=model1,
            messages=[
                {"role": "system", "content": "Be concise. Answer in the shortest, most accurate way possible."},
                {"role": "user", "content": f"{prompt}"}
            ],
            temperature=0.3,
            max_tokens=50
        )
        response_model1_text = response_model1['choices'][0]['message']['content'].strip()

        response_model2 = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model2,
            stream=False,
            max_tokens=50
        )
        response_model2_text = response_model2.choices[0].message.content.strip()

        dialogue_history += f"ChatGPT: {response_model1_text}\nGroq: {response_model2_text}\n"

        # Refinement: 2 rounds
        for _ in range(2):
            response_model2_refined = groq_client.chat.completions.create(
                messages=[{"role": "user", "content": f"{dialogue_history}\nRefine your answer."}],
                model=model2,
                stream=False,
                max_tokens=50
            )
            response_model2_refined_text = response_model2_refined.choices[0].message.content.strip()

            response_model1_refined = openai.ChatCompletion.create(
                model=model1,
                messages=[
                    {"role": "system", "content": "Be concise and precise. Keep responses short."},
                    {"role": "user", "content": f"{dialogue_history}\nRefine your answer."}
                ],
                temperature=0.3,
                max_tokens=50
            )
            response_model1_refined_text = response_model1_refined['choices'][0]['message']['content'].strip()

            dialogue_history += f"ChatGPT: {response_model1_refined_text}\nGroq: {response_model2_refined_text}\n"

        # Final response
        final_response_model1 = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Give the most refined and shortest final answer. and behave like a Reasoning Model."},
                {"role": "user", "content": dialogue_history}
            ],
            temperature=0.3,
            max_tokens=50
        )
        final_response_model1_text = final_response_model1['choices'][0]['message']['content'].strip()

        return f"{dialogue_history}\nFinal Answer: {final_response_model1_text}"

    except Exception as e:
        return f"Error: {e}"

# Example input
input_text = "9.9 and 9.11, which is bigger?"

# Execute concise reasoning
final_refined_answer = interactive_dialogue("gpt-4o-mini", "llama-3.3-70b-versatile", input_text)

# Print final response
print("\n--- Final Answer ---\n")
print(final_refined_answer)
print("\n--- End of Output ---\n")
