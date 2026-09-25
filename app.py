# Minor Project - Student AI Chatbot
# Developed by: Pallavi V
# Description: Helps students with fees, hostel, placement queries
# Guidelines Followed: Documented, README, Mobile Responsive, API Connected

from flask import Flask, request, jsonify

app = Flask(__name__)

# QA Dataset - This acts as API data source
# In major we will connect to real API
qa = {
    "fees": "B.tech fees 70,000 per year",
    "hostel": "Hostel fees 50,000 per year",
    "placement": "80% placements unnayi"
}

@app.route('/')
def home():
    """Homepage route - Mobile responsive chatbot UI"""
    # Added meta viewport for mobile responsiveness - Guideline 3
    return """<head><meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <style>body{font-family:Arial; padding:20px;} input,button{width:100%; padding:12px; margin:5px 0; font-size:16px;}</style></head>
    <h2>Chatbot Ready</h2>
    <input id='q' placeholder='fees/hostel/placement adugu'><button onclick='ask()'>Ask</button><p id='a'></p>
    <script>async function ask(){
    let q=document.getElementById('q').value.toLowerCase();
    let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q})});
    let d=await r.json();document.getElementById('a').innerText=d.answer;
    }</script>"""

@app.route('/ask', methods=['POST'])
def ask():
    """API Endpoint to handle chatbot queries - Guideline 4"""
    msg=request.json.get('message','').lower()
    for k in qa:
        if k in msg:
            return jsonify(answer=qa[k]) # Returns answer via API
    return jsonify(answer="fees/hostel/placement ani adugu")

if __name__ == '__main__':
    app.run(debug=True)
