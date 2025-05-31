import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json

# Mock database for vast data (expandable to SQLite, Firebase, etc.)
def load_domains():
    # Simulate a larger dataset of internship domains
    domains_data = {
        "Software Development": [1, 0, 0, 0.5, 0.3],
        "UI/UX Design": [0.2, 1, 0.3, 0, 0.5],
        "Digital Marketing": [0, 0.5, 1, 0.3, 0.8],
        "Data Science": [0.8, 0, 0.2, 1, 0.4],
        "Business Development": [0, 0.2, 0.8, 0, 1],
        "Cybersecurity": [0.7, 0, 0, 0.6, 0.4],
        "AI/ML Engineering": [0.9, 0, 0.1, 0.8, 0.3],
        "Graphic Design": [0.1, 0.9, 0.4, 0, 0.6],
        "Content Writing": [0, 0.3, 0.7, 0, 0.9],
        "Cloud Computing": [0.8, 0, 0, 0.7, 0.2]
    }
    # In real-world, load from a database or JSON file
    return domains_data

# Function to create user profile vector from inputs
def create_user_profile(interests, skills, experience):
    features = [0, 0, 0, 0, 0]  # [coding, design, marketing, data_analysis, communication]
    
    # Interests
    if "coding" in interests.lower(): features[0] += 0.5
    if "design" in interests.lower(): features[1] += 0.5
    if "marketing" in interests.lower(): features[2] += 0.5
    if "data" in interests.lower(): features[3] += 0.5
    if "business" in interests.lower(): features[4] += 0.5
    
    # Skills
    if "python" in skills.lower() or "java" in skills.lower(): features[0] += 0.5
    if "ui/ux" in skills.lower() or "figma" in skills.lower(): features[1] += 0.5
    if "seo" in skills.lower() or "social media" in skills.lower(): features[2] += 0.5
    if "machine learning" in skills.lower() or "statistics" in skills.lower(): features[3] += 0.5
    if "communication" in skills.lower() or "leadership" in skills.lower(): features[4] += 0.5
    
    # Experience
    if "software" in experience.lower() or "app" in experience.lower(): features[0] += 0.5
    if "design" in experience.lower() or "ui" in experience.lower(): features[1] += 0.5
    if "marketing" in experience.lower() or "campaign" in experience.lower(): features[2] += 0.5
    if "data" in experience.lower() or "analysis" in experience.lower(): features[3] += 0.5
    if "business" in experience.lower() or "sales" in experience.lower(): features[4] += 0.5
    
    return features

# Function to recommend internship domains
def recommend_internships(interests, skills, experience):
    user_profile = create_user_profile(interests, skills, experience)
    domains = load_domains()
    
    # Calculate cosine similarity for all domains
    recommendations = {}
    for domain, domain_vector in domains.items():
        similarity = cosine_similarity([user_profile], [domain_vector])[0][0]
        recommendations[domain] = similarity
    
    # Sort and return top 5 for broader coverage
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations[:5]

# Example usage
if __name__ == "__main__":
    user_interests = "coding, data"
    user_skills = "Python, machine learning"
    user_experience = "software project, data analysis"
    recs = recommend_internships(user_interests, user_skills, user_experience)
    print("Recommended Internship Domains:")
    for domain, score in recs:
        print(f"{domain}: {score:.2f}")
