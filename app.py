from flask import Flask, request, jsonify, render_template
from recommendation_engine import recommend_internships

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    interests = data.get('interests', '')
    skills = data.get('skills', '')
    experience = data.get('experience', '')
    
    # Basic validation
    if not all([interests, skills, experience]):
        return jsonify({"error": "All fields are required"}), 400
    
    recommendations = recommend_internships(interests, skills, experience)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
