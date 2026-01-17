import json
import os

class TreatmentAdvisor:
    """
    Sustainable treatment recommendation system
    Provides eco-friendly alternatives to chemical treatments
    """
    
    def __init__(self):
        self.treatments_db = self._load_treatments_database()
    
    def _load_treatments_database(self):
        """
        Load treatment database from JSON file or create default
        """
        try:
            # Try to load from data directory
            data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'treatments.json')
            if os.path.exists(data_path):
                with open(data_path, 'r') as f:
                    return json.load(f)
        except:
            pass
        
        # Return default treatments database
        return self._get_default_treatments()
    
    def _get_default_treatments(self):
        """
        Default sustainable treatments database
        """
        return {
            "Healthy": [
                {
                    "name": "Preventive Care",
                    "type": "Organic Prevention",
                    "method": "Regular monitoring and proper nutrition",
                    "eco_rating": 5,
                    "cost": "Low",
                    "ingredients": ["Compost", "Organic fertilizer", "Beneficial microorganisms"],
                    "application": "Apply organic compost monthly and monitor plant health weekly",
                    "effectiveness": "95%"
                }
            ],
            "Leaf Blight": [
                {
                    "name": "Neem Oil Treatment",
                    "type": "Organic Fungicide",
                    "method": "Foliar spray application",
                    "eco_rating": 4,
                    "cost": "Low",
                    "ingredients": ["Neem oil", "Water", "Mild soap"],
                    "application": "Mix 2 tbsp neem oil per liter water, spray in evening",
                    "effectiveness": "80%"
                },
                {
                    "name": "Baking Soda Solution",
                    "type": "Natural Fungicide",
                    "method": "Spray treatment",
                    "eco_rating": 5,
                    "cost": "Very Low",
                    "ingredients": ["Baking soda", "Water", "Vegetable oil"],
                    "application": "1 tsp baking soda + 1 tsp oil per liter water",
                    "effectiveness": "70%"
                },
                {
                    "name": "Copper Sulfate (Organic)",
                    "type": "Approved Organic",
                    "method": "Targeted application",
                    "eco_rating": 3,
                    "cost": "Medium",
                    "ingredients": ["Organic copper sulfate"],
                    "application": "Follow organic certification guidelines",
                    "effectiveness": "85%"
                }
            ],
            "Powdery Mildew": [
                {
                    "name": "Milk Spray Treatment",
                    "type": "Natural Antifungal",
                    "method": "Foliar application",
                    "eco_rating": 5,
                    "cost": "Very Low",
                    "ingredients": ["Fresh milk", "Water"],
                    "application": "Mix 1 part milk with 9 parts water, spray weekly",
                    "effectiveness": "75%"
                },
                {
                    "name": "Garlic & Onion Extract",
                    "type": "Natural Fungicide",
                    "method": "Homemade spray",
                    "eco_rating": 5,
                    "cost": "Low",
                    "ingredients": ["Garlic cloves", "Onion", "Water", "Soap"],
                    "application": "Blend ingredients, strain, dilute and spray",
                    "effectiveness": "70%"
                },
                {
                    "name": "Potassium Bicarbonate",
                    "type": "Organic Treatment",
                    "method": "Spray application",
                    "eco_rating": 4,
                    "cost": "Low",
                    "ingredients": ["Potassium bicarbonate", "Water"],
                    "application": "1 tbsp per liter water, spray affected areas",
                    "effectiveness": "80%"
                }
            ],
            "Rust Disease": [
                {
                    "name": "Compost Tea",
                    "type": "Biological Control",
                    "method": "Soil and foliar application",
                    "eco_rating": 5,
                    "cost": "Low",
                    "ingredients": ["Well-aged compost", "Water"],
                    "application": "Steep compost in water for 24-48 hours, strain and spray",
                    "effectiveness": "65%"
                },
                {
                    "name": "Chamomile Tea Spray",
                    "type": "Natural Antifungal",
                    "method": "Foliar spray",
                    "eco_rating": 5,
                    "cost": "Low",
                    "ingredients": ["Dried chamomile flowers", "Hot water"],
                    "application": "Steep chamomile, cool, strain and spray on affected areas",
                    "effectiveness": "60%"
                },
                {
                    "name": "Bordeaux Mixture (Organic)",
                    "type": "Traditional Organic",
                    "method": "Protective spray",
                    "eco_rating": 3,
                    "cost": "Medium",
                    "ingredients": ["Copper sulfate", "Hydrated lime", "Water"],
                    "application": "Follow organic preparation guidelines carefully",
                    "effectiveness": "85%"
                }
            ],
            "Bacterial Spot": [
                {
                    "name": "Hydrogen Peroxide Treatment",
                    "type": "Natural Disinfectant",
                    "method": "Diluted spray",
                    "eco_rating": 4,
                    "cost": "Low",
                    "ingredients": ["3% Hydrogen peroxide", "Water"],
                    "application": "Mix 1 part H2O2 with 10 parts water, spray lightly",
                    "effectiveness": "70%"
                },
                {
                    "name": "Apple Cider Vinegar Solution",
                    "type": "Natural Acidic Treatment",
                    "method": "Foliar spray",
                    "eco_rating": 5,
                    "cost": "Low",
                    "ingredients": ["Apple cider vinegar", "Water"],
                    "application": "2 tbsp vinegar per liter water, spray in morning",
                    "effectiveness": "65%"
                },
                {
                    "name": "Beneficial Bacteria Inoculation",
                    "type": "Biological Control",
                    "method": "Soil treatment",
                    "eco_rating": 5,
                    "cost": "Medium",
                    "ingredients": ["Bacillus subtilis", "Pseudomonas fluorescens"],
                    "application": "Apply beneficial bacteria to soil and root zone",
                    "effectiveness": "80%"
                }
            ],
            "Mosaic Virus": [
                {
                    "name": "Plant Removal & Sanitation",
                    "type": "Preventive Control",
                    "method": "Physical removal",
                    "eco_rating": 5,
                    "cost": "Low",
                    "ingredients": ["Disinfectant", "Clean tools"],
                    "application": "Remove infected plants, disinfect tools between plants",
                    "effectiveness": "90%"
                },
                {
                    "name": "Reflective Mulch",
                    "type": "Vector Control",
                    "method": "Physical barrier",
                    "eco_rating": 4,
                    "cost": "Medium",
                    "ingredients": ["Aluminum foil mulch", "Silver plastic mulch"],
                    "application": "Install reflective mulch to deter aphid vectors",
                    "effectiveness": "60%"
                },
                {
                    "name": "Companion Planting",
                    "type": "Natural Deterrent",
                    "method": "Integrated planting",
                    "eco_rating": 5,
                    "cost": "Low",
                    "ingredients": ["Marigolds", "Basil", "Nasturtiums"],
                    "application": "Plant deterrent species around susceptible crops",
                    "effectiveness": "50%"
                }
            ]
        }
    
    def get_recommendations(self, disease_name):
        """
        Get sustainable treatment recommendations for detected disease
        """
        treatments = self.treatments_db.get(disease_name, [])
        
        if not treatments:
            # Return generic eco-friendly advice for unknown diseases
            return [{
                "name": "Organic Consultation",
                "type": "Professional Advice",
                "method": "Expert consultation",
                "eco_rating": 5,
                "cost": "Medium",
                "ingredients": ["Professional assessment"],
                "application": "Consult with organic farming specialist",
                "effectiveness": "Variable"
            }]
        
        # Sort by eco-rating (highest first) and effectiveness
        treatments.sort(key=lambda x: (x['eco_rating'], int(x['effectiveness'].rstrip('%'))), reverse=True)
        
        return treatments
    
    def get_prevention_tips(self, disease_name):
        """
        Get prevention tips for specific diseases
        """
        prevention_tips = {
            "Leaf Blight": [
                "Ensure good air circulation between plants",
                "Avoid overhead watering",
                "Remove plant debris regularly",
                "Rotate crops annually",
                "Use disease-resistant varieties"
            ],
            "Powdery Mildew": [
                "Maintain proper plant spacing",
                "Reduce humidity around plants",
                "Avoid overhead irrigation",
                "Prune for better air flow",
                "Apply preventive organic sprays"
            ],
            "Rust Disease": [
                "Water at soil level, not on leaves",
                "Remove infected plant material",
                "Improve soil drainage",
                "Use resistant plant varieties",
                "Apply mulch to prevent soil splash"
            ],
            "Bacterial Spot": [
                "Use drip irrigation instead of sprinklers",
                "Disinfect tools between plants",
                "Avoid working with wet plants",
                "Remove and destroy infected plants",
                "Practice crop rotation"
            ],
            "Mosaic Virus": [
                "Control aphid and thrips populations",
                "Remove weeds that harbor viruses",
                "Use virus-free planting material",
                "Install physical barriers",
                "Practice good sanitation"
            ]
        }
        
        return prevention_tips.get(disease_name, [
            "Maintain healthy soil with organic matter",
            "Practice integrated pest management",
            "Monitor plants regularly for early detection",
            "Use certified disease-free seeds",
            "Maintain proper plant nutrition"
        ])
    
    def get_sustainability_score(self, treatments):
        """
        Calculate overall sustainability score for treatment plan
        """
        if not treatments:
            return 0
        
        total_score = sum(treatment['eco_rating'] for treatment in treatments)
        avg_score = total_score / len(treatments)
        
        return round(avg_score, 1)
    
    def generate_treatment_plan(self, disease_name, severity="medium"):
        """
        Generate comprehensive treatment plan based on disease and severity
        """
        treatments = self.get_recommendations(disease_name)
        prevention_tips = self.get_prevention_tips(disease_name)
        
        # Select treatments based on severity
        if severity.lower() == "high":
            selected_treatments = treatments[:2]  # Use top 2 treatments
        elif severity.lower() == "low":
            selected_treatments = treatments[:1]  # Use only the most eco-friendly
        else:
            selected_treatments = treatments[:2]  # Default to top 2
        
        plan = {
            "disease": disease_name,
            "severity": severity,
            "immediate_actions": selected_treatments,
            "prevention_tips": prevention_tips,
            "sustainability_score": self.get_sustainability_score(selected_treatments),
            "estimated_cost": self._estimate_total_cost(selected_treatments),
            "timeline": self._generate_timeline(selected_treatments)
        }
        
        return plan
    
    def _estimate_total_cost(self, treatments):
        """
        Estimate total cost for treatment plan
        """
        cost_mapping = {"Very Low": 5, "Low": 15, "Medium": 35, "High": 75}
        total_cost = sum(cost_mapping.get(treatment['cost'], 25) for treatment in treatments)
        
        if total_cost < 20:
            return "Very Low ($5-20)"
        elif total_cost < 50:
            return "Low ($20-50)"
        elif total_cost < 100:
            return "Medium ($50-100)"
        else:
            return "High ($100+)"
    
    def _generate_timeline(self, treatments):
        """
        Generate treatment timeline
        """
        return {
            "immediate": "Apply first treatment within 24 hours",
            "short_term": "Monitor progress for 3-7 days",
            "follow_up": "Apply second treatment if needed after 1 week",
            "prevention": "Implement prevention measures ongoing"
        }