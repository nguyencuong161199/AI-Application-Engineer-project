from openai import OpenAI
import os
import json

# Set up OpenAI environment variables
os.environ["OPENAI_API_KEY"] = "sk-v7MixFROMXjbzCX8NcdSDA"
os.environ["MODEL_NAME"] = "gpt-4o-mini"

client = OpenAI(
    base_url="https:e",
    api_key="...",
)

def create_conversation_with_few_shot_examples():
    """
    Creates a conversation with few-shot examples for sentiment analysis
    and chain-of-thought reasoning.
    """
    
    # Few-shot examples demonstrating sentiment analysis and reasoning
    few_shot_examples = [
        {
            "role": "user", 
            "content": "Analyze the sentiment of this text: 'I love attending networking events!'"
        },
        {
            "role": "assistant", 
            "content": "Let me analyze this step by step:\n1. The text contains 'I love' which is a strong positive emotion\n2. 'attending networking events' shows active participation\n3. The exclamation mark emphasizes enthusiasm\n\nSentiment: Positive\nConfidence: High\nReasoning: The text expresses genuine enthusiasm and enjoyment for networking activities."
        },
        {
            "role": "user", 
            "content": "Analyze the sentiment of this text: 'Networking can be really stressful sometimes.'"
        },
        {
            "role": "assistant", 
            "content": "Let me analyze this step by step:\n1. The text mentions 'stressful' which is a negative emotion\n2. 'can be' suggests this is a recurring experience\n3. 'sometimes' indicates it's not always negative\n\nSentiment: Negative\nConfidence: Medium\nReasoning: While the text acknowledges stress, it's not completely negative as it's situational."
        },
        {
            "role": "user", 
            "content": "Analyze the sentiment of this text: 'I'm neutral about networking events - they're okay.'"
        },
        {
            "role": "assistant", 
            "content": "Let me analyze this step by step:\n1. The text explicitly states 'neutral' which indicates no strong feelings\n2. 'they're okay' suggests mild acceptance\n3. No strong positive or negative language is used\n\nSentiment: Neutral\nConfidence: High\nReasoning: The text clearly expresses indifference with no strong emotional indicators."
        }
    ]
    
    # System prompt that defines the assistant's role and capabilities
    system_prompt = {
        "role": "system", 
        "content": """You are a helpful event management assistant with expertise in:
1. Sentiment analysis with detailed reasoning
2. Providing conversation starters for networking events
3. Event planning and management advice
4. Chain-of-thought reasoning for complex problems

Always provide step-by-step reasoning when analyzing sentiment or solving problems.
Format your responses clearly with structured explanations."""
    }
    
    # Build conversation messages
    conversation_messages = [system_prompt]
    conversation_messages.extend(few_shot_examples)
    
    return conversation_messages

def add_user_question(conversation_messages, question, use_chain_of_thought=True):
    """
    Adds a user question to the conversation with optional chain-of-thought prompting.
    """
    if use_chain_of_thought:
        question += " Please explain your reasoning step-by-step."
    
    conversation_messages.append({
        "role": "user",
        "content": question
    })
    
    return conversation_messages

def get_ai_response(conversation_messages, temperature=0.7):
    """
    Calls Azure OpenAI API and returns the response.
    """
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=conversation_messages,
            temperature=temperature,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Azure OpenAI API: {str(e)}"

def print_conversation_analysis(conversation_messages, response):
    """
    Prints a formatted analysis of the conversation and response.
    """
    print("=" * 80)
    print("CONVERSATION ANALYSIS")
    print("=" * 80)
    
    print("\n📋 CONVERSATION STRUCTURE:")
    for i, message in enumerate(conversation_messages):
        role = message["role"].upper()
        content_preview = message["content"][:100] + "..." if len(message["content"]) > 100 else message["content"]
        print(f"{i+1}. {role}: {content_preview}")
    
    print(f"\n🤖 AI RESPONSE:")
    print("-" * 40)
    print(response)
    
    print("\n📊 ANALYSIS SUMMARY:")
    print("-" * 40)
    print(f"• Total messages in conversation: {len(conversation_messages)}")
    print(f"• Few-shot examples included: {len([m for m in conversation_messages if m['role'] == 'assistant' and m != conversation_messages[-1]])}")
    print(f"• System prompt included: {any(m['role'] == 'system' for m in conversation_messages)}")
    print(f"• Chain-of-thought prompting: {'Yes' if 'step-by-step' in conversation_messages[-1]['content'] else 'No'}")

def main():
    """
    Main function demonstrating the complete workflow.
    """
    print("🚀 Azure OpenAI Conversation with Few-Shot Learning and Chain-of-Thought")
    print("=" * 80)
    
    # Create conversation with few-shot examples
    conversation_messages = create_conversation_with_few_shot_examples()
    
    # Add user question with chain-of-thought prompting
    user_question = "What are some good conversation starters at networking events?"
    conversation_messages = add_user_question(conversation_messages, user_question, use_chain_of_thought=True)
    
    # Get AI response
    print("🔄 Calling Azure OpenAI API...")
    response = get_ai_response(conversation_messages)
    
    # Print analysis
    print_conversation_analysis(conversation_messages, response)
    
    # Demonstrate sentiment analysis
    print("\n" + "=" * 80)
    print("SENTIMENT ANALYSIS DEMONSTRATION")
    print("=" * 80)
    
    # Create new conversation for sentiment analysis
    sentiment_conversation = create_conversation_with_few_shot_examples()
    sentiment_question = "Analyze the sentiment of this text: 'I'm excited to meet new people at the conference!'"
    sentiment_conversation = add_user_question(sentiment_conversation, sentiment_question, use_chain_of_thought=True)
    
    sentiment_response = get_ai_response(sentiment_conversation)
    print_conversation_analysis(sentiment_conversation, sentiment_response)

if __name__ == "__main__":
    main() 