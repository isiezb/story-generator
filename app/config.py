class Config:
    SECRET_KEY = 'your-secret-key-here'  # Change this in production
    POE_API_KEY = "1KKDAZsfNXFXSXUKljtYuF6_HGP_NSsJ_PL2kxHvsDw"
    DEBUG = True

    # Medical topics and their descriptions
    MEDICAL_TOPICS = {
        "physiology": {
            "name": "Physiologie",
            "subtopics": [
                "Herz-Kreislauf-System",
                "Nervensystem",
                "Atmungssystem",
                "Verdauungssystem",
                "Endokrines System",
                "Immunsystem",
                "Muskel-Skelett-System"
            ]
        },
        "biochemistry": {
            "name": "Biochemie",
            "subtopics": [
                "Glykolyse",
                "Citratzyklus",
                "Oxidative Phosphorylierung",
                "Lipidstoffwechsel",
                "Proteinbiosynthese",
                "Enzymkinetik",
                "Hormonregulation"
            ]
        },
        "pharmacology": {
            "name": "Pharmakologie",
            "subtopics": [
                "Antibiotika",
                "Analgetika",
                "Antihypertensiva",
                "Antikoagulanzien",
                "Antidepressiva",
                "Immunsuppressiva",
                "Chemotherapeutika"
            ]
        },
        "clinical_reasoning": {
            "name": "Klinische Diagnostik",
            "subtopics": [
                "Differenzialdiagnose",
                "Notfallmedizin",
                "Klinische Untersuchung",
                "Labordiagnostik",
                "Bildgebende Verfahren",
                "Therapieplanung",
                "Prognoseeinschätzung"
            ]
        },
        'atoms_and_molecules': {
            'name': 'Atome und Moleküle',
            'subtopics': [
                'Atomaufbau und Periodensystem',
                'Chemische Bindungen',
                'Molekülstrukturen',
                'Elektronenkonfiguration'
            ]
        },
        'chemical_reactions': {
            'name': 'Chemische Reaktionen',
            'subtopics': [
                'Säure-Base-Reaktionen',
                'Redox-Reaktionen',
                'Energieumsatz bei Reaktionen',
                'Reaktionsgeschwindigkeit'
            ]
        },
        'organic_chemistry': {
            'name': 'Organische Chemie',
            'subtopics': [
                'Kohlenhydrate',
                'Proteine und Aminosäuren',
                'Lipide',
                'Vitamine und Coenzyme'
            ]
        },
        'analytical_chemistry': {
            'name': 'Analytische Chemie',
            'subtopics': [
                'Titration',
                'Spektroskopie',
                'Chromatographie',
                'pH-Messung'
            ]
        },
        'food_chemistry': {
            'name': 'Lebensmittelchemie',
            'subtopics': [
                'Nährstoffanalyse',
                'Lebensmittelzusatzstoffe',
                'Lebensmittelkonservierung',
                'Lebensmittelsicherheit'
            ]
        }
    }

    # Complexity levels with medical-specific descriptions
    COMPLEXITY_LEVELS = {
        "beginner": {
            "name": "Anfänger",
            "description": "Grundlegende Konzepte mit einfacher Terminologie"
        },
        "intermediate": {
            "name": "Fortgeschritten",
            "description": "Detaillierte Informationen mit Fachterminologie"
        },
        "master": {
            "name": "Experte",
            "description": "Komplexe Zusammenhänge mit fortgeschrittener Terminologie"
        },
        'beginner': {
            'name': 'Anfänger',
            'description': 'Grundlegende Konzepte mit einfacher Erklärung'
        },
        'intermediate': {
            'name': 'Fortgeschritten',
            'description': 'Detailliertere Erklärungen mit Fachbegriffen'
        },
        'advanced': {
            'name': 'Experte',
            'description': 'Komplexe Zusammenhänge und detaillierte Mechanismen'
        }
    }

    # Story length options with medical context
    STORY_LENGTHS = {
        "short": {
            "name": "Kurz",
            "words": 300,
            "description": "Schnelle Übersicht"
        },
        "medium": {
            "name": "Mittel",
            "words": 700,
            "description": "Ausführliche Erklärung"
        },
        "long": {
            "name": "Lang",
            "words": 1200,
            "description": "Tiefgehende Analyse"
        },
        'short': {
            'name': 'Kurz',
            'words': 300,
            'description': 'Schnelle Einführung in das Thema'
        },
        'medium': {
            'name': 'Mittel',
            'words': 600,
            'description': 'Ausführliche Erklärung mit Beispielen'
        },
        'long': {
            'name': 'Lang',
            'words': 1000,
            'description': 'Umfassende Behandlung mit vielen Details'
        }
    }

    # System prompt for story generation
    SYSTEM_PROMPT = """Du bist ein Experte für didaktische Geschichten im Bereich der Chemie für Ernährungswissenschaften.
    Deine Aufgabe ist es, komplexe chemische Konzepte in fesselnde, leicht verständliche Geschichten zu verwandeln.
    Die Geschichten sollten:
    - Wissenschaftlich korrekt sein
    - Praktische Beispiele aus der Ernährungswissenschaft enthalten
    - Die gewählte Komplexitätsebene einhalten
    - Interaktiv und ansprechend sein
    - Fachbegriffe angemessen erklären
    - Zusammenhänge klar darstellen
    - Die gewünschte Länge einhalten
    - In der gewählten Sprache verfasst sein (Standard: Deutsch)""" 