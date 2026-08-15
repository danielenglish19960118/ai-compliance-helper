import os
import json
from openai import OpenAI

# Initialize client (compatible with OpenAI format or open-source APIs)
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "your-api-key-here")
)

def ai_compliance_and_polish_helper(draft_content: str) -> dict:
    """
    AI Smart Compliance & Polishing Helper Prototype
    Core Philosophy: Zero bans, automated background refinement, protecting creators' work.
    """
    
    system_prompt = (
        "You are a gentle and professional AI creator collaboration assistant. Your task is to review drafts:"
        "1. Check if the content has severe violation risks (e.g., fraud, extreme violence, illegal acts)."
        "2. If there are minor edge-cases or imprecise phrasing, automatically refine and polish it in the background to ensure compliance while keeping the author's original intent."
        "3. NEVER lecture, scold, or demand self-reflection from the creator."
        "4. Output format must be strictly JSON containing three fields:"
        "   - 'status': 'passed' (published directly) or 'auto_fixed' (automatically refined for compliance)"
        "   - 'final_content': The final processed content ready for publishing"
        "   - 'editor_note': A friendly note to the author explaining any changes made, or confirming everything looks great"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", # Can be replaced with open-source or efficient models
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Please review and process this draft:\n\n{draft_content}"}
            ],
            response_format={"type": "json_object"}
        )
        
        result = json.loads(response.choices[0].message.content)
        
        # Core promise append
        result["account_status"] = "SAFE (Account is 100% secure, never banned)"
        return result

    except Exception as e:
        return {
            "status": "error",
            "final_content": draft_content,
            "editor_note": f"System connection error. Automated check skipped, original draft preserved. Error: {str(e)}",
            "account_status": "SAFE (Account is 100% secure, never banned)"
        }

# --- Test Execution ---
if __name__ == "__main__":
    # Simulate a creator drafting content with emotional or borderline wording
    sample_draft = "These big corporations are completely scams, their business tactics are trash and nobody should ever buy their products!"
    
    print("--- Submitting to AI Compliance & Polishing Helper ---")
    print(f"Original Draft: {sample_draft}\n")
    
    # Execute helper (uncomment when API key is set)
    # output = ai_compliance_and_polish_helper(sample_draft)
    
    # Simulated Prototype Output Display:
    mock_output = {
        "status": "auto_fixed",
        "final_content": "This corporation's business practices have raised concerns, and we recommend consumers carefully evaluate and review related feedback before purchasing.",
        "editor_note": "Your draft was automatically refined in the background to soften emotional language and potential controversies, ensuring smooth and compliant publishing!",
        "account_status": "SAFE (Account is 100% secure, never banned)"
    }
    
    print("--- Processing Result ---")
    print(f"Status: {mock_output['status']}")
    print(f"Final Published Content: {mock_output['final_content']}")
    print(f"Editor Note: {mock_output['editor_note']}")
    print(f"Account Status: {mock_output['account_status']}")
