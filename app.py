from flask import Flask, request, jsonify
app = Flask(__name__)

qa = {
    "fees": "B.Tech fees 70,000 per year",
    "hostel": "Hostel fees 50,000 per year",
    "placement": "80% placements unnayi"
}

@app.route('/')
def home():
    return """<h2>Chatbot Ready</h2>
    <input id='q'><button onclick='ask()'>Ask</button><p id='a'></p>
    <script>async function ask(){
    let q=document.getElementById('q').value.toLowerCase();
    let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q})});
    let d=await r.json();document.getElementById('a').innerText=d.answer;
    }</script>"""

@app.route('/ask', methods=['POST'])
def ask():
    msg=request.json.get('message','').lower()
    for k in qa:
        if k in msg: return jsonify(answer=qa[k])
    return jsonify(answer="fees/hostel/placement ani adugu")
app.run(debug=True)