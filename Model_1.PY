import openai
from groq import Groq

# Set up the API keys for OpenAI (ChatGPT) and Groq AI
openai.api_key = "Add OpenAi Api key here."
groq_client = Groq(api_key="Add Groq Api key here.")

def interactive_dialogue(model1, model2, prompt):
    """Models interact like two friends talking to refine an answer over 3 rounds."""
    try:
        dialogue_history = ""
        
        # First round of responses (initial thoughts)
        response_model1 = openai.ChatCompletion.create(
            model=model1,
            messages=[{"role": "system", "content": "You are a helpful assistant. Provide a brief and clear answer."},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=60
        )
        response_model1_text = response_model1['choices'][0]['message']['content'].strip()

        response_model2 = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            stream=False,
            max_tokens=60
        )
        response_model2_text = response_model2.choices[0].message.content.strip()

        dialogue_history += f"ChatGPT (Model 1) says: {response_model1_text}\nGroq (Model 2) responds: {response_model2_text}\n"

        # First round interaction: models respond to each other
        for _ in range(2):  # 2 more rounds after the initial response (total of 3 rounds)
            response_model2_refined = groq_client.chat.completions.create(
                messages=[{"role": "user", "content": f"{dialogue_history}\n\nGroq, do you agree with ChatGPT's answer?"}],
                model="llama-3.3-70b-versatile",
                stream=False,
                max_tokens=60
            )
            response_model2_refined_text = response_model2_refined.choices[0].message.content.strip()

            response_model1_refined = openai.ChatCompletion.create(
                model=model1,
                messages=[{"role": "system", "content": "You are a helpful assistant. Respond to Groq's question and refine your response."},
                          {"role": "user", "content": f"{dialogue_history}\n\nChatGPT, refine your response based on Groq's thoughts."}],
                temperature=0.7,
                max_tokens=60
            )
            response_model1_refined_text = response_model1_refined['choices'][0]['message']['content'].strip()

            dialogue_history += f"ChatGPT (Model 1) refined says: {response_model1_refined_text}\nGroq (Model 2) responds: {response_model2_refined_text}\n"

        # Final round: After 3 rounds, ChatGPT generates the best refined answer
        final_response_model1 = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "You are a helpful assistant. After considering all previous dialogue, provide the most refined and perfect answer."},
                      {"role": "user", "content": dialogue_history}],
            temperature=0.7,
            max_tokens=100
        )
        final_response_model1_text = final_response_model1['choices'][0]['message']['content'].strip()

        # Return the final combined conversation and ChatGPT's final refined response
        final_dialogue = f"After three rounds of interaction, here are the final responses:\n\n{dialogue_history}\nFinal Refined Answer by ChatGPT: {final_response_model1_text}"

        return final_dialogue

    except Exception as e:
        return f"Error during the interactive reasoning process: {e}"

# Example input text for reasoning
input_text = "9.1 and 9.9 which one is bigger?"

# Perform interactive dialogue between models
final_refined_answer = interactive_dialogue("gpt-4o-mini", groq_client, input_text)

# Print the final result of the interactive dialogue
print("\n--- Final Refined Answer After Interactive Dialogue ---\n")
print(final_refined_answer)
print("\n--- End of Reasoning Output ---\n") 