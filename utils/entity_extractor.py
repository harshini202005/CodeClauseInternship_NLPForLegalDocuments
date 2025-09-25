import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """
    Extract named entities from text.
    Returns a list of tuples: (entity_text, entity_label)
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
