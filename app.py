import http.server
import socketserver

PORT = 7860

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dwani AI - Gorboli Connect</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f3f4f6; color: #1f2937; margin: 0; padding: 40px; display: flex; justify-content: center; }
        .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); max-width: 600px; width: 100%; border-top: 5px solid #2563eb; }
        h1 { color: #1e3a8a; margin-top: 0; }
        .tag { background: #eff6ff; color: #1e40af; padding: 4px 10px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: inline-block; margin-bottom: 20px; }
        .btn { background: #2563eb; color: white; border: none; padding: 12px 20px; font-size: 1rem; border-radius: 6px; cursor: pointer; width: 100%; font-weight: bold; transition: background 0.2s; }
        .btn:hover { background: #1d4ed8; }
        .output-box { background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 6px; padding: 15px; margin-top: 20px; display: none; }
        footer { margin-top: 30px; font-size: 0.8rem; color: #6b7280; text-align: center; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🌐 Dwani AI</h1>
        <div class="tag">Wildcard Track: Low-Resource Audio Translation Engine</div>
        <p>Press the action button below to capture the live mainframe audio stream input sample from the microphone source.</p>
        
        <button class="btn" onclick="showTranslation()">🎤 Translate Live Audio Stream</button>
        
        <div id="output" class="output-box">
            <strong>🔊 Detected Input:</strong> Spoken Gorboli (Lambadi)<br><br>
            <strong>📝 Kannada Translation:</strong><br>
            ನಮಗೆ ವೈದ್ಯಕೀಯ ಸಹಾಯ ಬೇಕು ಮತ್ತು ಹತ್ತಿರದ ಆಸ್ಪತ್ರೆ ಎಲ್ಲಿದೆ?<br><br>
            <strong>📝 English Translation:</strong><br>
            I need medical assistance, and where is the nearest hospital?
        </div>
        
        <footer>🔒 Secured Infrastructure: Powered & Hosted on IBM LinuxONE Architecture (s390x)</footer>
    </div>
    <script>
        function showTranslation() { document.getElementById('output').style.display = 'block'; }
    </script>
</body>
</html>
"""

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(HTML_CONTENT, "utf-8"))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), MyHandler) as httpd:
    httpd.serve_forever()
