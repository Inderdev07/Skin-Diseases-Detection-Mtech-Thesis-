"""
Disease Information Database Module
=====================================
Comprehensive medical information about skin diseases.
Place this file in the utils/ directory.

Usage:
    from utils.disease_info import get_disease_info, DISEASE_DATABASE
"""

DISEASE_DATABASE = {
    'melanoma': {'name': 'Melanoma', 'severity': 'CRITICAL', 'description': 'Most serious skin cancer', 'symptoms': ['Asymmetrical moles', 'Irregular borders', 'Multiple colors', 'Diameter >6mm', 'Changes in appearance'], 'causes': ['Sun exposure', 'Sunburns', 'Fair skin', 'Family history', 'Atypical moles'], 'prevention': ['Sunscreen SPF 30+', 'Avoid 10AM-4PM sun', 'Protective clothing', 'Regular skin checks', 'Avoid tanning beds'], 'treatment': ['Surgical excision', 'Mohs surgery', 'Immunotherapy', 'Targeted therapy', 'Chemotherapy'], 'prognosis': '5-year survival >90% if detected early'},
    'nevus': {'name': 'Nevus (Common Mole)', 'severity': 'LOW', 'description': 'Benign mole - common and harmless', 'symptoms': ['Brown/tan spot', 'Uniform color', 'Symmetrical', 'Well-defined borders', '<6mm size'], 'causes': ['Genetic factors', 'Normal development', 'Sun exposure', 'Age'], 'prevention': ['Sun protection', 'Regular monitoring', 'Avoid UV', 'Track changes'], 'treatment': ['Monitoring (preferred)', 'Cosmetic removal', 'Laser removal', 'Cryotherapy'], 'prognosis': 'Benign with excellent prognosis'},
    'basal_cell_carcinoma': {'name': 'Basal Cell Carcinoma', 'severity': 'HIGH', 'description': 'Most common skin cancer, slow-growing', 'symptoms': ['Pearly nodule', 'Bleeding center', 'Scaly lesion', 'Pink/red color', 'Rolled borders'], 'causes': ['Chronic sun exposure', 'Sunburns', 'Fair skin', 'Aging', 'Chemical exposure'], 'prevention': ['Sunscreen use', 'Protective clothing', 'Avoid peak sun', 'Regular checks'], 'treatment': ['Surgical excision', 'Mohs surgery', 'Curettage', 'Topical imiquimod', 'Laser therapy'], 'prognosis': 'Excellent with early treatment, rarely metastasizes'},
    'actinic_keratosis': {'name': 'Actinic Keratosis', 'severity': 'MEDIUM', 'description': 'Precancerous lesion from sun damage', 'symptoms': ['Rough patches', 'Red/pink/brown', 'Tender spots', '<1cm size', 'Wart-like'], 'causes': ['Cumulative sun exposure', 'UVB radiation', 'Advanced age', 'Fair skin'], 'prevention': ['Strict sun protection', 'Daily sunscreen', 'Protective clothing', 'Avoid peak hours'], 'treatment': ['Topical 5-FU', 'Topical imiquimod', 'Cryotherapy', 'Chemical peels', 'Laser ablation'], 'prognosis': 'Good with treatment, prevents SCC progression'},
    'benign_keratosis': {'name': 'Benign Keratosis', 'severity': 'LOW', 'description': 'Non-cancerous growth, common with age', 'symptoms': ['Waxy appearance', 'Brown/black/tan', 'Well-defined', 'Raised', 'Itchy sometimes'], 'causes': ['Age-related', 'Genetic', 'Dead skin accumulation'], 'prevention': ['Sun protection', 'Regular monitoring', 'Moisturizing'], 'treatment': ['Observation (common)', 'Cosmetic removal', 'Cryotherapy', 'Laser therapy'], 'prognosis': 'Benign, no malignant potential'},
    'dermatofibroma': {'name': 'Dermatofibroma', 'severity': 'LOW', 'description': 'Benign nodule, common in women', 'symptoms': ['Firm nodule', 'Pink/red/brown', '<1cm', 'Central dimple', 'Slow growth'], 'causes': ['Trauma/injury response', 'Insect bites', 'Unknown exact cause'], 'prevention': ['Avoid skin trauma', 'Prevent insect bites', 'Sun protection'], 'treatment': ['Observation (common)', 'Surgical excision', 'Steroid injections', 'Laser therapy'], 'prognosis': 'Benign, may persist or resolve gradually'},
    'vascular_lesions': {'name': 'Vascular Lesions', 'severity': 'LOW', 'description': 'Blood vessel abnormalities', 'symptoms': ['Red/purple marks', 'Blanches with pressure', 'May be flat/raised', 'Various sizes'], 'causes': ['Congenital', 'Trauma', 'Sun exposure', 'Genetic factors'], 'prevention': ['Sun protection', 'Avoid trauma', 'Avoid irritants'], 'treatment': ['Laser therapy', 'IPL treatment', 'Surgical excision', 'Sclerotherapy'], 'prognosis': 'Good with treatment options, no malignant potential'},
    'squamous_cell_carcinoma': {'name': 'Squamous Cell Carcinoma', 'severity': 'HIGH', 'description': 'Second most common skin cancer', 'symptoms': ['Scaly nodule', 'Pink/red base', 'Rapid growth', 'Bleeding/ulceration', 'Tender'], 'causes': ['Cumulative sun exposure', 'UVB radiation', 'Immunosuppression', 'Chronic inflammation'], 'prevention': ['Aggressive sun protection', 'Sunscreen daily', 'Protective clothing', 'Treat AK'], 'treatment': ['Surgical excision', 'Mohs surgery', 'Topical 5-FU', 'Radiation', 'Chemotherapy'], 'prognosis': 'Good if detected early, risk increases with size/depth'},
    'psoriasis': {'name': 'Psoriasis', 'severity': 'MEDIUM', 'description': 'Chronic autoimmune condition', 'symptoms': ['Red patches', 'Silvery scale', 'Itching/burning', 'Nail pitting', 'Joint pain'], 'causes': ['Genetic predisposition', 'Immune dysfunction', 'Stress', 'Infections'], 'prevention': ['Stress management', 'Treat infections', 'Avoid triggers', 'Healthy lifestyle'], 'treatment': ['Topical steroids', 'Vitamin D analogues', 'Phototherapy', 'Biologic drugs'], 'prognosis': 'Chronic but manageable with treatment'},
    'eczema': {'name': 'Eczema (Atopic Dermatitis)', 'severity': 'MEDIUM', 'description': 'Chronic inflammatory condition', 'symptoms': ['Intense itching', 'Red inflammation', 'Dry skin', 'Raised bumps', 'Cracked skin'], 'causes': ['Genetic factors', 'Immune dysfunction', 'Environmental factors', 'Stress'], 'prevention': ['Skin hydration', 'Gentle cleansing', 'Avoid irritants', 'Stress management'], 'treatment': ['Moisturizers', 'Topical steroids', 'Antihistamines', 'Phototherapy', 'Biologic therapy'], 'prognosis': 'Chronic but manageable, many children outgrow it'}
}

def get_disease_info(disease_name):
    """Get disease information by name"""
    disease_name = disease_name.lower().replace(' ', '_')
    return DISEASE_DATABASE.get(disease_name)

def get_all_diseases():
    """Get list of all disease keys"""
    return list(DISEASE_DATABASE.keys())

def get_disease_names():
    """Get list of all disease display names"""
    return [d['name'] for d in DISEASE_DATABASE.values()]
