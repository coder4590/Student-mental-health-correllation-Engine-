import re
from .mental_health_knowledge import KNOWLEDGE_BASE


def preprocess(text):
    """Clean and normalize user input."""
    text = text.lower().strip()
    # Remove excessive punctuation
    text = re.sub(r'([!?.,])\1{2,}', r'\1\1', text)
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    return text


def is_nonsense(text):
    """Detect if input is mostly random characters or keyboard smashing."""
    # Check if text is mostly non-alphabetic
    alpha_count = sum(1 for c in text if c.isalpha())
    if len(text) > 3 and alpha_count < len(text) * 0.3:
        return True
    
    # Check for repeated patterns like "asdf", "qwert", "zxcv"
    keyboard_patterns = ['asdf', 'qwert', 'zxcv', 'fdsa', 'jkl', 'hjkl', '12345', '54321']
    for pattern in keyboard_patterns:
        if pattern in text:
            return True
    
    # Check if it's just repeated characters
    if len(text) > 3 and len(set(text)) <= 2:
        return True
    
    return False


def has_typo_indicators(text):
    """Check for common typing errors."""
    typo_indicators = [
        'hellp', 'hepl', 'halp', 'helpp',
        'sadd', 'saaaad', 'saddd', 'depresed', 'depresion', 'deppression',
        'anxity', 'anxcious', 'anxiuos',
        'lonley', 'lonlly', 'lonli', 'lonly',
        'wortless', 'worthles', 'worthess', 'hopless', 'hopeles',
        'crrying', 'cryin', 'cryng', 'suicde', 'sucid',
        'hurrt', 'hurrting', 'hurrrt',
        'pleese', 'pleease', 'pleas',
        'whyy', 'whyyy', 'why meee',
        'help meee', 'help mee', 'helpp me',
        'i dont', 'i dnt', 'i cnt', 'i dont know',
        'nothng', 'nothin', 'nuthing',
    ]
    for typo in typo_indicators:
        if typo in text:
            return True
    return False


def match_patterns(text, patterns):
    """Check if text matches any pattern."""
    for pattern in patterns:
        if pattern == "*":
            continue
        
        # Exact phrase match
        if pattern in text:
            return True
        
        # All words from pattern appear in text (any order)
        pattern_words = pattern.split()
        if len(pattern_words) > 1:
            if all(word in text for word in pattern_words):
                return True
        
        # Fuzzy match for very short patterns
        if len(pattern) > 5 and len(text) > 5:
            # Check if pattern shares 80% of its characters with a substring of text
            pattern_chars = set(pattern.replace(" ", ""))
            text_chars = set(text.replace(" ", ""))
            overlap = pattern_chars & text_chars
            if len(pattern_chars) > 0 and len(overlap) / len(pattern_chars) > 0.8:
                return True
    
    return False


def find_best_match(text):
    """Find the best matching knowledge base entry."""
    best_match = None
    best_score = 0
    
    for entry in KNOWLEDGE_BASE:
        patterns = entry["patterns"]
        
        for pattern in patterns:
            if pattern == "*":
                continue
            
            score = 0
            
            # Exact phrase match = highest score
            if pattern in text:
                score = 100 + len(pattern)  # Longer patterns win ties
            
            # All pattern words present
            pattern_words = pattern.split()
            if len(pattern_words) > 1:
                if all(word in text for word in pattern_words):
                    score = 80 + len(pattern_words)
            
            # Partial word matches
            matched_words = sum(1 for word in pattern_words if word in text)
            if matched_words > 0:
                score = max(score, 50 + matched_words * 10)
            
            # Fuzzy character overlap
            pattern_chars = set(pattern.replace(" ", ""))
            text_chars = set(text.replace(" ", ""))
            overlap = pattern_chars & text_chars
            if len(pattern_chars) > 0:
                overlap_ratio = len(overlap) / len(pattern_chars)
                if overlap_ratio > 0.7:
                    score = max(score, 30 + int(overlap_ratio * 50))
            
            if score > best_score:
                best_score = score
                best_match = entry
    
    return best_match


def is_crisis_message(text):
    """Quick check for crisis keywords to ensure immediate response."""
    crisis_keywords = [
        'suicide', 'kill myself', 'want to die', 'end my life',
        'kms', 'end it', 'self harm', 'cut myself', 'hurt myself',
        'better off dead', 'not want to live', 'want to end',
        'going to kill', 'planning to end', 'die today', 'die now',
        'take my life', 'cease to exist', 'never wake up'
    ]
    for keyword in crisis_keywords:
        if keyword in text:
            return True
    return False


def find_response(user_message):
    """
    Main matching engine. Takes user message, returns best response.
    Handles: crisis, normal patterns, typos, nonsense, vague input.
    """
    # Clean input
    text = preprocess(user_message)
    
    # If empty after cleaning
    if not text or len(text) < 2:
        return {
            "response": "I'm here and I'm listening. Take your time — there's no rush. What's on your mind?",
            "category": "empty_input"
        }
    
    # 1. CRISIS CHECK — highest priority
    if is_crisis_message(text):
        crisis_entry = None
        for entry in KNOWLEDGE_BASE:
            if entry["patterns"] and "i want to die" in entry["patterns"]:
                crisis_entry = entry
                break
        if crisis_entry:
            return {"response": crisis_entry["response"], "category": "crisis"}
    
    # 2. NONSENSE CHECK
    if is_nonsense(text):
        for entry in KNOWLEDGE_BASE:
            if "asdf" in entry["patterns"]:
                return {"response": entry["response"], "category": "nonsense"}
    
    # 3. TYPO CHECK
    if has_typo_indicators(text):
        for entry in KNOWLEDGE_BASE:
            if "helpp" in entry["patterns"]:
                return {"response": entry["response"], "category": "typo"}
    
    # 4. BEST PATTERN MATCH
    best_entry = find_best_match(text)
    if best_entry:
        # Identify category from first pattern
        category = "general"
        if best_entry["patterns"]:
            first_pattern = best_entry["patterns"][0]
            if any(word in first_pattern for word in ['die', 'suicide', 'kill', 'end my']):
                category = "crisis"
            elif any(word in first_pattern for word in ['empty', 'numb', 'hollow']):
                category = "depression"
            elif any(word in first_pattern for word in ['worthless', 'hate myself', 'failure']):
                category = "self_worth"
            elif any(word in first_pattern for word in ['cry', 'crying', 'sad']):
                category = "sadness"
            elif any(word in first_pattern for word in ['bed', 'tired', 'fatigue', 'energy']):
                category = "fatigue"
            elif any(word in first_pattern for word in ['motivation', 'enjoy', 'pleasure']):
                category = "anhedonia"
            elif any(word in first_pattern for word in ['overwhelm', 'cope', 'too much']):
                category = "overwhelm"
            elif any(word in first_pattern for word in ['thank', 'helped', 'better']):
                category = "gratitude"
        
        return {"response": best_entry["response"], "category": category}
    
    # 5. FALLBACK
    for entry in KNOWLEDGE_BASE:
        if entry["patterns"] == ["*"]:
            return {"response": entry["response"], "category": "fallback"}
    
    return {
        "response": "I'm here to listen. Tell me more about how you're feeling. You're not alone.",
        "category": "fallback"
    }


def chat(user_message):
    """Public interface for the chatbot."""
    return find_response(user_message)
