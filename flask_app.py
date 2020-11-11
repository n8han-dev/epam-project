from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/upload')
def upload_file_butn():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'
	
@app.route('/result')
def show_file():


if __name__ == '__main__':
   app.run()
