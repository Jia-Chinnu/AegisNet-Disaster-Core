import ollama
import json

def analyze_disaster_data(image_path, text_message):
    """
    This function takes the saved image and text message, sends them 
    to your offline AI models, and returns a smart, structured analysis.
    """
    print(f"\n[AI CORE] Analyzing image: {image_path}...")
    
    # 1. Have the Visual AI look at the photo
    vision_prompt = (
        "Analyze this post-disaster image. Identify if roads, buildings, or bridges "
        "are flooded, blocked, or collapsed. Respond in one short sentence."
    )
    
    try:
        vision_response = ollama.generate(
            model='llava:7b',
            prompt=vision_prompt,
            images=[image_path]
        )
        visual_findings = vision_response['response']
    except Exception as e:
        visual_findings = f"Could not process image: {str(e)}"
    
    print(f"[AI CORE] Visual AI Sighted: {visual_findings}")

    # 2. Have the Text AI read the message + what the Visual AI saw
    print("[AI CORE] Triaging situation details...")
    triage_prompt = f"""
    You are an expert emergency coordinator. Analyze this data:
    Civilian Message: "{text_message}"
    Visual AI Sightings: "{visual_findings}"
    
    You MUST respond ONLY with a valid JSON object. Do not add any conversational text. Use this exact structure:
    {{
      "urgency_level": "CRITICAL" or "HIGH" or "MEDIUM",
      "medical_emergency": true or false,
      "short_summary": "one sentence summary of the danger"
    }}
    """
    
    text_response = ollama.generate(
        model='phi3:mini',
        prompt=triage_prompt
    )
    
    # Clean up output formatting if the model adds markdown ticks
    clean_json = text_response['response'].strip().replace("```json", "").replace("```", "")
    
    try:
        return json.loads(clean_json)
    except:
        return {"raw_ai_output": text_response['response']}