# Two-Model Chain-of-Thought (CoT) Reasoning

This repository demonstrates an advanced **Two-Model Chain-of-Thought (CoT) reasoning** system using two AI models: **OpenAI GPT-4o** and **Groq Llama 3-70B**. The system refines its answers through interactive reasoning between the models, ensuring high accuracy and concise responses. Here's how it works:

## Overview

The primary goal of this approach is to provide more precise answers by leveraging the reasoning capabilities of two AI models in a collaborative manner. The models generate initial responses independently, refine each other's output, and synthesize the final answer with the help of GPT-4o. This step-by-step refinement allows for improved accuracy and clarity.

### Key Features:
- **Interactive Reasoning:** The two models exchange feedback, providing refined answers over several rounds.
- **Concise Responses:** Each model is instructed to generate short and precise answers, minimizing unnecessary elaboration.
- **Chain-of-Thought (CoT):** The models engage in deep, reflective reasoning to ensure well-rounded answers. CoT promotes step-by-step analysis, allowing for more accurate conclusions.

## How It Works

1. **Initial Response Generation:**  
   Both GPT-4o and Groq Llama 3-70B are asked to answer the same question. Each model generates a concise response independently.

2. **Cross-Model Refinement:**  
   The models refine their answers based on feedback from the other. They adjust their responses in two additional rounds, improving accuracy and addressing potential ambiguities.

3. **Final Refined Answer:**  
   After multiple rounds of interaction, GPT-4o synthesizes the most refined answer, taking into account both its own insights and those of Llama 3-70B.

## Code Walkthrough

### 1. Initial Setup
- API keys for **OpenAI** and **Groq AI** are set up to interact with the respective models.
- Models are selected (e.g., `gpt-4o` and `llama-3.3-70b-versatile`).

### 2. Interactive Dialogue Function
- The function `interactive_dialogue` orchestrates the entire process:
  - It first sends the user’s prompt to both models.
  - The models generate their initial responses.
  - Then, each model reviews and refines the other's response.
  - This process is repeated for a few rounds to ensure the final output is as refined as possible.
  - GPT-4o delivers the final, best-refined answer.

### 3. Prompting for Concise Responses
- The system is set to request **short and concise responses** from both models through system instructions like "Please generate the shortest possible answer."

## Example
*"Which is larger, 9.9 or 9.11?"*  

- **Model 1 (GPT-4o-mini):** Generates a response such as "9.9 is larger."  
- **Model 2 (Groq Llama 3-70B):** Might refine with additional reasoning or clarity, e.g., "Since 9.9 is numerically larger than 9.11."  
- Both models continue refining each other's responses until GPT-4o provides the most accurate and concise final answer: "9.9 is numerically larger than 9.11."

## Advantages

- **Increased Accuracy:** Multiple models provide diverse reasoning, which leads to a more accurate conclusion.
- **Collaborative Improvement:** The feedback loop between the models helps correct and refine responses, addressing ambiguities.
- **Concise Responses:** The system prioritizes brevity, ensuring the final output is to the point without unnecessary elaboration.

## Requirements

- Python 3.x
- `openai` library (for GPT-4o)
- `groq` library (for Llama 3-70B)
- API Keys for OpenAI and Groq

## How to Use

1. Install dependencies:

```bash
pip install openai groq
```

2. Replace the `sk-YOUR_OPENAI_KEY` and `gsk-YOUR_GROQ_KEY` with your respective API keys.

3. Run the script with a prompt:

```python
input_text = "Which is bigger, 9.9 or 9.11?"
final_answer = interactive_dialogue("gpt-4o", "llama-3-70b", input_text)
print(final_answer)
```

4. The system will output the most refined and concise response after several rounds of reasoning.

## Conclusion

This Two-Model Chain-of-Thought (CoT) system offers an innovative approach to improving AI reasoning. By combining the strengths of two powerful models, it ensures that answers are not only accurate but also concise. This method provides a reliable, efficient way to refine complex responses in real-time.
