from flask import Flask, render_template, request, flash, redirect, url_for
from compression import compress_file, decompress_file
from conversion import convert_docx_to_pdf, convert_pdf_to_docx

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(file.filename)
            zip_path = compress_file(file.filename)
            if zip_path:
                flash("Fichier compressé avec succès!", 'success')
            else:
                flash("La compression du fichier a échoué.", 'danger')
    return redirect(url_for('index'))

@app.route('/decompress', methods=['POST'])
def decompress():
    if request.method == 'POST':
        zip_file = request.files['zip_file']
        if zip_file:
            zip_file.save(zip_file.filename)
            extracted_path = decompress_file(zip_file.filename)
            if extracted_path:
                flash("Fichier décompressé avec succès!", 'success')
            else:
                flash("La décompression du fichier a échoué.", 'danger')
    return redirect(url_for('index'))

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        if 'docx_to_pdf' in request.form:
            docx_file = request.files['docx_file']
            if docx_file:
                docx_file.save(docx_file.filename)
                convert_docx_to_pdf(docx_file.filename, 'converted.pdf')
                flash("Conversion de DOCX en PDF réussie!", 'success')

        if 'pdf_to_docx' in request.form:
            pdf_file = request.files['pdf_file']
            if pdf_file:
                pdf_file.save(pdf_file.filename)
                convert_pdf_to_docx(pdf_file.filename, 'converted.docx')
                flash("Conversion de PDF en DOCX réussie!", 'success')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
