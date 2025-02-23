# main_app/context_processors.py

def footer_content(request):
    return {
        'social_links': {
            'github': 'https://github.com/Vvikram10',
            'linkedin': 'https://linkedin.com/in/vvikram10',
            'twitter': 'https://twitter.com/yourusername',
            'instagram': 'https://www.instagram.com/v_vik_ram_?igsh=cmMxaDhuOTJzb3Vr',
        },
        'footer_nav': [
            {'name': 'Home', 'url': 'home'},
            {'name': 'About', 'url': 'about'},
            {'name': 'Projects', 'url': 'projects'},
            {'name': 'Contact', 'url': 'contact'},
        ]
    }