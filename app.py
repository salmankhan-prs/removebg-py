from flask  import Flask , render_template, send_file,request
from rembg import remove
from PIL import Image
from io import BytesIO


app =Flask(__name__)

@app.route('/',methods=['GET','POST'])
def upload_file():
    if request.method =="POST":
        if 'file' not in request.files:
            return 'no file uploaded',400
        file =request.files['file']
        if file.filename =='':
          return 'no file selected ',400
        if file:
            input_image =Image.open(file.stream)
            output_image = remove(input_image,post_process_mask=True)
            img_io =BytesIO()
            output_image.save(img_io,'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=file.filename+'_rmbg.png')
    return render_template('index.html')



if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True,port=5100)