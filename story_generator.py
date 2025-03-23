from flask import Flask, request, render_template_string
import asyncio
import fastapi_poe as fp

app = Flask(__name__)

# Replace this with your actual Poe API key (from poe.com/api_key)
POE_API_KEY = "1KKDAZsfNXFXSXUKljtYuF6_HGP_NSsJ_PL2kxHvsDw"

# HTML template with embedded CSS for a clean, simple interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Enhanced Multilingual Didactic Story Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        form {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-right: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        .story {
            background-color: #fff;
            border-left: 4px solid #4CAF50;
            padding: 15px;
            margin-top: 20px;
            position: relative;
        }
        .error {
            color: red;
            font-weight: bold;
        }
        .loading {
            text-align: center;
            margin: 20px 0;
            display: none;
        }
        .progress {
            width: 100%;
            background-color: #ddd;
            border-radius: 4px;
            margin-top: 10px;
        }
        .progress-bar {
            height: 20px;
            background-color: #4CAF50;
            border-radius: 4px;
            text-align: center;
            color: white;
            line-height: 20px;
            transition: width 0.3s ease;
        }
        .story-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .copy-btn {
            background-color: #4267B2;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 5px 10px;
            cursor: pointer;
            font-size: 14px;
        }
        .copy-btn:hover {
            background-color: #365899;
        }
        .copy-feedback {
            color: green;
            margin-left: 10px;
            font-size: 14px;
            display: none;
        }
        .progress-status {
            margin-top: 5px;
            font-size: 14px;
            color: #666;
        }
    </style>
    <script>
        function showLoading() {
            document.getElementById('loading').style.display = 'block';
            document.getElementById('progress-bar').style.width = '0%';
            document.getElementById('progress-bar').innerText = '0%';
            document.getElementById('progress-status').innerText = 'Starting...';
            updateProgress(5, 'Initializing story generation...');
            return true;
        }
        
        function updateProgress(percent, status) {
            document.getElementById('progress-bar').style.width = percent + '%';
            document.getElementById('progress-bar').innerText = percent + '%';
            document.getElementById('progress-status').innerText = status;
            
            // If we're done, hide the loading div after a short delay
            if (percent >= 100) {
                setTimeout(function() {
                    document.getElementById('loading').style.display = 'none';
                }, 1000);
            }
        }
        
        function copyStory() {
            const storyText = document.getElementById('story-text').innerText;
            
            // Create a temporary textarea element to copy from
            const textarea = document.createElement('textarea');
            textarea.value = storyText;
            document.body.appendChild(textarea);
            
            // Select and copy the text
            textarea.select();
            document.execCommand('copy');
            
            // Remove the temporary element
            document.body.removeChild(textarea);
            
            // Show feedback
            const feedback = document.getElementById('copy-feedback');
            feedback.style.display = 'inline';
            
            // Hide feedback after 2 seconds
            setTimeout(function() {
                feedback.style.display = 'none';
            }, 2000);
        }
    </script>
</head>
<body>
    <h1>Enhanced Multilingual Didactic Story Generator</h1>
    <form method="post" onsubmit="return showLoading();">
        <label for="topic">Topic (e.g., photosynthesis, friendship, space exploration):</label>
        <input type="text" id="topic" name="topic" required>
        
        <label for="setting">Setting (e.g., a forest, a futuristic city, a medieval castle):</label>
        <input type="text" id="setting" name="setting" required>
        
        <label for="character">Main Character (e.g., a curious squirrel, a young astronaut, a wise queen):</label>
        <input type="text" id="character" name="character" required>
        
        <label for="complexity">Complexity Level:</label>
        <select id="complexity" name="complexity">
            <option value="beginner">Beginner (simple concepts)</option>
            <option value="intermediate">Intermediate (some detail)</option>
            <option value="master">Master (complex and nuanced)</option>
        </select>
        
        <label for="length">Story Length:</label>
        <select id="length" name="length">
            <option value="short">Short (~300 words)</option>
            <option value="medium">Medium (~700 words)</option>
            <option value="long">Long (~1200 words)</option>
        </select>
        
        <label for="language">Language (leave blank for English):</label>
        <input type="text" id="language" name="language" placeholder="e.g., Spanish, French, German, etc."">
        
        <button type="submit">Generate Story</button>
    </form>
    
    <div id="loading" class="loading">
        <p>Generating your story... This may take a few minutes...</p>
        <div class="progress">
            <div id="progress-bar" class="progress-bar" style="width: 0%">0%</div>
        </div>
        <div id="progress-status" class="progress-status">Starting...</div>
    </div>
    
    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}
    
    {% if story %}
        <div class="story-header">
            <h2>Your Story:</h2>
            <div>
                <button class="copy-btn" onclick="copyStory()">Copy Story</button>
                <span id="copy-feedback" class="copy-feedback">Copied!</span>
            </div>
        </div>
        <div class="story">
            <div id="story-text">{{ story }}</div>
        </div>
    {% endif %}
</body>
</html>
"""

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
            api_key=POE_API_KEY
        ):
            if hasattr(partial, 'text'):
                response_text += partial.text
        
        return response_text
    except Exception as e:
        return f"Error calling Poe API: {str(e)}"

def run_async(coroutine):
    """Helper function to run async functions from sync code"""
    return asyncio.run(coroutine)

class StoryProgress:
    """Helper class to track story generation progress"""
    def __init__(self):
        self.percent = 0
        self.status = "Initializing..."

    def update(self, percent, status):
        self.percent = percent
        self.status = status
        return self.percent, self.status

async def generate_research_content(topic, complexity, language="", progress_callback=None):
    """Generate accurate research content about the topic"""
    if progress_callback:
        progress_callback(10, f"Researching about {topic}...")
    
    complexity_map = {
        "beginner": "simple, foundational concepts with basic vocabulary",
        "intermediate": "moderately detailed information with some domain-specific terminology",
        "master": "complex, nuanced information with advanced terminology and deeper insights"
    }
    
    complexity_desc = complexity_map.get(complexity, complexity_map["intermediate"])
    
    language_instruction = ""
    if language:
        language_instruction = f"Respond in {language}. "
    
    research_prompt = f"""
    {language_instruction}I need accurate, well-researched information about "{topic}" at a {complexity} level ({complexity_desc}).
    
    Please provide:
    1. 3-5 key facts or principles about {topic}
    2. Any relevant vocabulary or terminology that should be included
    3. Common misconceptions or interesting aspects about {topic}
    4. A clear explanation of why this topic matters or how it connects to real life
    
    Format your response in clear sections. Be accurate and educational.
    """
    
    research_response = await call_poe_api(research_prompt)
    
    if progress_callback:
        progress_callback(20, f"Research on {topic} complete!")
        
    return research_response

async def develop_character(character, topic, setting, language="", progress_callback=None):
    """Develop the main character with traits that support the story"""
    if progress_callback:
        progress_callback(30, f"Developing character: {character}...")
    
    language_instruction = ""
    if language:
        language_instruction = f"Respond in {language}. "
    
    character_prompt = f"""
    {language_instruction}Create a detailed profile for "{character}" who will star in a didactic story about "{topic}" set in "{setting}".
    
    Include:
    1. Key personality traits that will help this character engage with the topic
    2. Background details that explain why this character cares about or encounters {topic}
    3. Skills, limitations, or motivations that will drive the character's journey
    4. How the character might grow or change through learning about {topic}
    
    Keep the character engaging and relatable while ensuring they're a good vehicle for teaching about {topic}.
    """
    
    character_response = await call_poe_api(character_prompt)
    
    if progress_callback:
        progress_callback(40, f"Character development complete!")
        
    return character_response

async def create_setting_details(setting, topic, character, language="", progress_callback=None):
    """Create detailed setting information that supports the story"""
    if progress_callback:
        progress_callback(50, f"Building the world: {setting}...")
    
    language_instruction = ""
    if language:
        language_instruction = f"Respond in {language}. "
    
    setting_prompt = f"""
    {language_instruction}Create a vivid, detailed description of "{setting}" for a didactic story about "{topic}" featuring "{character}".
    
    Include:
    1. Sensory details that make this setting come alive (sights, sounds, smells, textures)
    2. Specific locations within this setting where teaching moments about {topic} could naturally occur
    3. Elements of the setting that naturally connect to or demonstrate aspects of {topic}
    4. Any challenges or opportunities the setting presents for {character}
    
    Make the setting both immersive and purposeful for teaching about {topic}.
    """
    
    setting_response = await call_poe_api(setting_prompt)
    
    if progress_callback:
        progress_callback(60, f"Setting creation complete!")
        
    return setting_response

async def plot_development(topic, character, setting, research, character_details, setting_details, complexity, language="", progress_callback=None):
    """Develop a plot that organically teaches about the topic"""
    if progress_callback:
        progress_callback(70, f"Crafting plot structure...")
    
    language_instruction = ""
    if language:
        language_instruction = f"Respond in {language}. "
    
    plot_prompt = f"""
    {language_instruction}Using the research, character, and setting information below, create a structured plot outline for a didactic story about "{topic}" at a {complexity} level.
    
    RESEARCH:
    {research}
    
    CHARACTER:
    {character_details}
    
    SETTING:
    {setting_details}
    
    Your plot outline should include:
    1. A compelling opening that introduces {character} and establishes their connection to {topic}
    2. 2-3 key events where {character} encounters and learns about different aspects of {topic}
    3. A climax that challenges {character} to apply what they've learned about {topic}
    4. A resolution that reinforces the key educational points about {topic}
    
    Ensure the plot naturally integrates teaching moments while remaining engaging and appropriate for the {complexity} level.
    """
    
    plot_response = await call_poe_api(plot_prompt)
    
    if progress_callback:
        progress_callback(80, f"Plot development complete!")
        
    return plot_response

async def synthesize_story(topic, character, setting, complexity, research, character_details, setting_details, plot, length, language="", progress_callback=None):
    """Combine all elements into a cohesive, engaging story"""
    if progress_callback:
        progress_callback(90, f"Synthesizing final story...")
    
    # Map length selection to target word count
    word_counts = {
        "short": 300,
        "medium": 700,
        "long": 1200
    }
    target_words = word_counts.get(length, 700)
    
    language_instruction = ""
    if language:
        language_instruction = f"Write the final story in {language}. "
    
    synthesis_prompt = f"""
    {language_instruction}Write a complete, engaging didactic story about "{topic}" featuring "{character}" in "{setting}" at a {complexity} level.
    
    Use these prepared elements to craft your story:
    
    RESEARCH:
    {research}
    
    CHARACTER:
    {character_details}
    
    SETTING:
    {setting_details}
    
    PLOT:
    {plot}
    
    Guidelines:
    1. The story should be approximately {target_words} words long
    2. Naturally weave educational content about {topic} throughout the narrative
    3. Use language and complexity appropriate for a {complexity} level audience
    4. Create a satisfying narrative arc with a clear lesson about {topic}
    5. End with a subtle recap of the key points about {topic} through the character's journey
    
    Create an engaging story that teaches while entertaining!
    """
    
    story = await call_poe_api(synthesis_prompt)
    
    if progress_callback:
        progress_callback(100, "Story complete!")
        
    return story

@app.route('/', methods=['GET', 'POST'])
def home():
    """Handle both GET and POST requests to the home page."""
    story = None
    error = None
    
    if request.method == 'POST':
        # Get form data
        topic = request.form.get('topic', '')
        setting = request.form.get('setting', '')
        character = request.form.get('character', '')
        complexity = request.form.get('complexity', 'intermediate')
        length = request.form.get('length', 'medium')
        language = request.form.get('language', '').strip()
        
        try:
            # Create a progress updater for the frontend
            # (Note: In a real implementation, you would use websockets to update the progress bar)
            # This is a placeholder for the concept
            
            async def generate_story():
                # Step 1: Research content
                research = await generate_research_content(topic, complexity, language)
                
                # Step 2: Character development
                character_details = await develop_character(character, topic, setting, language)
                
                # Step 3: Setting creation
                setting_details = await create_setting_details(setting, topic, character, language)
                
                # Step 4: Plot development
                plot = await plot_development(topic, character, setting, research, 
                                           character_details, setting_details, complexity, language)
                
                # Step 5: Synthesize final story
                final_story = await synthesize_story(topic, character, setting, complexity, 
                                                  research, character_details, setting_details, 
                                                  plot, length, language)
                
                return final_story
                
            # Generate the story
            story = run_async(generate_story())
            
            # Check if we got an error
            if story and story.startswith("Error"):
                error = story
                story = None
                
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template_string(HTML_TEMPLATE, story=story, error=error)

if __name__ == '__main__':
    print("Enhanced Didactic Story Generator is running!")
    print("Open your web browser and visit: http://localhost:5000")
    app.run(host='0.0.0.0', port=5001, debug=True)  # Changed port to 5001 to avoid AirPlay conflicts