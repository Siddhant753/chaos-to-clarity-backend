RULES = {
    'Incident' : ['overheat', 'overstress', 'failure', 'fault', 'crash'],
    'Vendor Issue' : ['vendor', 'shipment', 'package', 'parcel', 'delay', 'late'],
    'QA Issue' : ['qa', 'testing', 'test', 'damage', 'damaged', 'pcb', 'failed'],
    'Electrical' : ['voltage', 'current', 'resistance', 'inductor', 'capacitor', 'battery', 'fuse'],
    'Mechanical' : ['fracture', 'fatigue'],
    'Environmental' : ['humidity', 'moisture', 'dust', 'corrosion', 'contamination'],
    'Uncategorized' : [],
}

SEVERITY_KEYWORDS = {
    'high' : ['overheat', 'overstress', 'failure', 'crash'],
    'medium' : ['failed', 'delay'],
}

def classify_text(text : str):
    text_lower = text.lower()
    tags = []

    # Category
    category = 'Uncategorized'
    confidence = 0.3

    for cat, keywords in RULES.items():
        for word in keywords:
            if word in text_lower:
                category = cat
                tags.append(word)
                confidence = 0.7
                break

    # Severity
    severity = 'low'
    for level, keywords in SEVERITY_KEYWORDS.items():
        if any(k in text_lower for k in keywords):
            severity = level

    return {
        'category' : category,
        'tags' : list(set(tags)),
        'severity' : severity,
        'confidence' : confidence,
    }