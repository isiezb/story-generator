import fastapi_poe as fp
from flask import current_app

async def call_poe_api(prompt, bot_name="gemini-1.5-flash"):
    """
    Send a prompt to the Poe API and get the response using the fastapi-poe library.
    
    Args:
        prompt (str): The prompt to send to the API
        bot_name (str): The name of the bot to use
        
    Returns:
        str: The response from the API or an error message
    """
    try:
        message = fp.ProtocolMessage(role="user", content=prompt)
        response_text = ""
        
        async for partial in fp.get_bot_response(
            messages=[message], 
            bot_name=bot_name, 
            api_key=current_app.config['POE_API_KEY']
        ):
            if hasattr(partial, 'text'):
                response_text += partial.text
        
        return response_text
    except Exception as e:
        return f"Error calling Poe API: {str(e)}" 