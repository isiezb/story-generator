from flask import Blueprint, request, render_template
from app.services.story_generator import StoryGenerator
from app.models.story_progress import StoryProgress
from app.utils.text_utils import count_words, estimate_reading_time
import asyncio

bp = Blueprint('main', __name__)

def run_async(coroutine):
    """Helper function to run async functions from sync code"""
    return asyncio.run(coroutine)

@bp.route('/', methods=['GET', 'POST'])
def home():
    """Handle both GET and POST requests to the home page."""
    story = None
    error = None
    metrics = None
    
    if request.method == 'POST':
        # Get form data
        topic = request.form.get('topic', '')
        subtopic = request.form.get('subtopic', '')
        complexity = request.form.get('complexity', 'intermediate')
        length = request.form.get('length', 'medium')
        language = request.form.get('language', '').strip()
        
        # If no language is specified, default to German
        if not language:
            language = "Deutsch"
        
        try:
            # Create story generator instance
            story_generator = StoryGenerator()
            
            # Create a progress updater for the frontend
            def update_progress(percent, status):
                # In a real implementation, this would use websockets to update the frontend
                pass
            
            # Generate the story
            story = run_async(story_generator.generate_story(
                topic=subtopic,
                setting="Krankenhaus",
                character="Dr. Schmidt",
                complexity=complexity,
                length=length,
                language=language
            ))
            
            # Check if we got an error
            if story and story.startswith("Error"):
                error = story
                story = None
            else:
                # Calculate metrics
                metrics = {
                    "word_count": count_words(story),
                    "reading_time": estimate_reading_time(story)
                }
                
        except Exception as e:
            error = f"Ein Fehler ist aufgetreten: {str(e)}"
    
    return render_template('index.html', story=story, error=error, metrics=metrics) 