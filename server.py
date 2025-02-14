from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_image():
    try:
        if "file" not in request.files:
            return "No file uploaded. Fuck it, try again. 🖕", 400

        file = request.files["file"]
        if file.filename == "":
            return "Invalid file name. Fuck it, try again. 🖕", 400

        file_path = "uploaded_image.jpg"
        file.save(file_path)
        print(f"✅ Image received and saved as {file_path}")

        return "Image uploaded successfully! 🚀", 200

    except Exception as e:
        return f"Failed to process image. Fuck it, try again. 🖕 Error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
