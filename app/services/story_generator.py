import asyncio
import fastapi_poe as fp
from flask import current_app
from app.services.poe_service import call_poe_api
from app.models.story_progress import StoryProgress

class StoryGenerator:
    def __init__(self):
        self.progress = StoryProgress()

    async def generate_research_content(self, topic, complexity, language="", progress_callback=None):
        """Generate accurate research content about the topic"""
        if progress_callback:
            progress_callback(10, f"Recherchiere über {topic}...")
        
        complexity_map = {
            "beginner": "einfache, grundlegende Konzepte mit Basis-Vokabular",
            "intermediate": "moderat detaillierte Informationen mit Fachterminologie",
            "master": "komplexe, differenzierte Informationen mit fortgeschrittener Terminologie"
        }
        
        complexity_desc = complexity_map.get(complexity, complexity_map["intermediate"])
        
        language_instruction = ""
        if language and language.lower() != "deutsch":
            language_instruction = f"Antworten Sie in {language}. "
        
        research_prompt = f"""
        {language_instruction}Ich benötige präzise, gut recherchierte Informationen über "{topic}" auf {complexity} Niveau ({complexity_desc}).
        
        Bitte geben Sie:
        1. 3-5 wichtige Fakten oder Prinzipien über {topic}
        2. Relevante Fachbegriffe oder Terminologie, die einbezogen werden sollte
        3. Häufige Missverständnisse oder interessante Aspekte über {topic}
        4. Eine klare Erklärung, warum dieses Thema wichtig ist oder wie es mit der Praxis verbunden ist
        
        Formatieren Sie Ihre Antwort in klaren Abschnitten. Seien Sie präzise und lehrreich.
        """
        
        research_response = await call_poe_api(research_prompt)
        
        if progress_callback:
            progress_callback(20, f"Recherche zu {topic} abgeschlossen!")
        
        return research_response

    async def develop_character(self, character, topic, setting, language="", progress_callback=None):
        """Develop the main character with traits that support the story"""
        if progress_callback:
            progress_callback(30, f"Entwickle Charakter: {character}...")
        
        language_instruction = ""
        if language and language.lower() != "deutsch":
            language_instruction = f"Antworten Sie in {language}. "
        
        character_prompt = f"""
        {language_instruction}Erstellen Sie ein detailliertes Profil für "{character}", der in einer didaktischen Geschichte über "{topic}" in "{setting}" die Hauptrolle spielt.
        
        Beinhalten Sie:
        1. Wichtige Persönlichkeitsmerkmale, die diesem Charakter helfen, sich mit dem Thema auseinanderzusetzen
        2. Hintergrundinformationen, die erklären, warum dieser Charakter sich für {topic} interessiert
        3. Fähigkeiten, Einschränkungen oder Motivationen, die die Reise des Charakters antreiben
        4. Wie der Charakter durch das Lernen über {topic} wachsen oder sich verändern könnte
        
        Gestalten Sie den Charakter ansprechend und nachvollziehbar, während Sie sicherstellen, dass er sich gut eignet, um über {topic} zu lehren.
        """
        
        character_response = await call_poe_api(character_prompt)
        
        if progress_callback:
            progress_callback(40, f"Charakterentwicklung abgeschlossen!")
        
        return character_response

    async def create_setting_details(self, setting, topic, character, language="", progress_callback=None):
        """Create detailed setting information that supports the story"""
        if progress_callback:
            progress_callback(50, f"Gestalte die Welt: {setting}...")
        
        language_instruction = ""
        if language and language.lower() != "deutsch":
            language_instruction = f"Antworten Sie in {language}. "
        
        setting_prompt = f"""
        {language_instruction}Erstellen Sie eine lebendige, detaillierte Beschreibung von "{setting}" für eine didaktische Geschichte über "{topic}" mit "{character}" als Hauptfigur.
        
        Beinhalten Sie:
        1. Sinnliche Details, die diese Umgebung lebendig machen (Sehen, Hören, Riechen, Fühlen)
        2. Spezifische Orte innerhalb dieser Umgebung, wo Lehrinhalte über {topic} natürlich eingebracht werden könnten
        3. Elemente der Umgebung, die sich natürlich mit Aspekten von {topic} verbinden lassen
        4. Herausforderungen oder Möglichkeiten, die diese Umgebung für {character} bietet
        
        Gestalten Sie die Umgebung sowohl immersiv als auch zweckmäßig für die Vermittlung von {topic}.
        """
        
        setting_response = await call_poe_api(setting_prompt)
        
        if progress_callback:
            progress_callback(60, f"Umgebungsgestaltung abgeschlossen!")
        
        return setting_response

    async def plot_development(self, topic, character, setting, research, character_details, setting_details, complexity, language="", progress_callback=None):
        """Develop a plot that organically teaches about the topic"""
        if progress_callback:
            progress_callback(70, f"Entwickle Handlungsstruktur...")
        
        language_instruction = ""
        if language and language.lower() != "deutsch":
            language_instruction = f"Antworten Sie in {language}. "
        
        plot_prompt = f"""
        {language_instruction}Erstellen Sie unter Verwendung der folgenden Forschungs-, Charakter- und Umgebungsinformationen eine strukturierte Handlungsübersicht für eine didaktische Geschichte über "{topic}" auf {complexity} Niveau.
        
        FORSCHUNG:
        {research}
        
        CHARAKTER:
        {character_details}
        
        UMGEBUNG:
        {setting_details}
        
        Ihre Handlungsübersicht sollte beinhalten:
        1. Einen fesselnden Anfang, der {character} einführt und seine Verbindung zu {topic} herstellt
        2. 2-3 Schlüsselereignisse, bei denen {character} verschiedene Aspekte von {topic} kennenlernt
        3. Einen Höhepunkt, bei dem {character} das Gelernte über {topic} anwenden muss
        4. Eine Auflösung, die die wichtigsten Lehrinhalte über {topic} verstärkt
        
        Stellen Sie sicher, dass die Handlung Lehrinhalte natürlich integriert, während sie spannend und für das {complexity} Niveau angemessen bleibt.
        """
        
        plot_response = await call_poe_api(plot_prompt)
        
        if progress_callback:
            progress_callback(80, f"Handlungsentwicklung abgeschlossen!")
        
        return plot_response

    async def synthesize_story(self, topic, character, setting, complexity, research, character_details, setting_details, plot, length, language="", progress_callback=None):
        """Combine all elements into a cohesive, engaging story"""
        if progress_callback:
            progress_callback(90, f"Verfasse die finale Geschichte...")
        
        # Map length selection to target word count
        word_counts = {
            "short": 300,
            "medium": 700,
            "long": 1200
        }
        target_words = word_counts.get(length, 700)
        
        language_instruction = ""
        if language and language.lower() != "deutsch":
            language_instruction = f"Schreiben Sie die finale Geschichte in {language}. "
        
        synthesis_prompt = f"""
        {language_instruction}Schreiben Sie eine vollständige, fesselnde didaktische Geschichte über "{topic}" mit "{character}" in "{setting}" auf {complexity} Niveau.
        
        Verwenden Sie diese vorbereiteten Elemente für Ihre Geschichte:
        
        FORSCHUNG:
        {research}
        
        CHARAKTER:
        {character_details}
        
        UMGEBUNG:
        {setting_details}
        
        HANDLUNG:
        {plot}
        
        Richtlinien:
        1. Die Geschichte sollte etwa {target_words} Wörter lang sein
        2. Integrieren Sie Lehrinhalte über {topic} natürlich in die Handlung
        3. Verwenden Sie Sprache und Komplexität, die für ein {complexity} Niveau geeignet sind
        4. Erstellen Sie einen befriedigenden Handlungsbogen mit einer klaren Lektion über {topic}
        5. Schließen Sie mit einer subtilen Zusammenfassung der wichtigsten Punkte über {topic} durch die Reise des Charakters
        
        Erstellen Sie eine fesselnde Geschichte, die lehrt und unterhält!
        """
        
        story = await call_poe_api(synthesis_prompt)
        
        if progress_callback:
            progress_callback(100, "Geschichte abgeschlossen!")
        
        return story

    def format_story_text(self, text):
        """Format the story text with proper paragraphs and spacing"""
        # Split the text into paragraphs
        paragraphs = text.split('\n\n')
        
        # Clean up each paragraph
        formatted_paragraphs = []
        for paragraph in paragraphs:
            # Remove extra whitespace
            paragraph = paragraph.strip()
            if paragraph:
                # Add proper indentation
                formatted_paragraphs.append(f"    {paragraph}")
        
        # Join paragraphs with double line breaks
        return '\n\n'.join(formatted_paragraphs)

    async def generate_story(self, topic, setting, character, complexity, length, language="", progress_callback=None):
        """Main method to generate a complete story"""
        try:
            # Step 1: Research content
            research = await self.generate_research_content(topic, complexity, language, progress_callback)
            
            # Step 2: Character development
            character_details = await self.develop_character(character, topic, setting, language, progress_callback)
            
            # Step 3: Setting creation
            setting_details = await self.create_setting_details(setting, topic, character, language, progress_callback)
            
            # Step 4: Plot development
            plot = await self.plot_development(topic, character, setting, research, 
                                           character_details, setting_details, complexity, language, progress_callback)
            
            # Step 5: Synthesize final story
            final_story = await self.synthesize_story(topic, character, setting, complexity, 
                                                  research, character_details, setting_details, 
                                                  plot, length, language, progress_callback)
            
            # Format the story text
            final_story = self.format_story_text(final_story)
            
            return final_story
            
        except Exception as e:
            return f"Fehler bei der Geschichtengenerierung: {str(e)}" 