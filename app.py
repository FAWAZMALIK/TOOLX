from flask import Flask,redirect, render_template, request,  send_file
from helpers import apology, docxtopdf , pdftodocx ,docxtotext , pdftotext , texttopdf , texttodocx , is_integer , tojpg ,topdf , topng , extext, exframe ,tobw, tosound, converter
import os



# Configure application
app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


TOOL = ["text","numbers","file","photo","video","audio"]


#homepage
@app.route("/", methods=["GET", "POST"])
def index():
    """Show Home Page"""
    if request.method == "POST":
        # Validate input
        val = request.values.get("button")
        if val not in TOOL:
            return apology("Invalid Tool")
        # Redireact to requested page
        if val == "text":
             return redirect("/text")
        if val == "file":
             return redirect("/file")
        if val == "numbers":
             return redirect("/numbers")
        if val == "photo":
             return redirect("/photo")
        if val == "video":
            return redirect("/video")
        if val == "audio":
            return redirect("/audio")
        
        else:
            return redirect("/")

    else:
        return render_template("index.html")


@app.route("/text")
def text():
    """Show Text Page"""
    return render_template("text.html")


@app.route("/numbers")
def numbers():
    """Show Numbers Page"""
    return render_template("numbers.html")


@app.route("/photo", methods=["GET", "POST"])
def photo():
    """Show photo Page"""
    if request.method == "POST":
        image = request.files['image']
        op1 = request.values.get('op1')
        # Validate input
        if not image:
            return render_template('photo.html',notice='No Image Is Selected!')
        if op1 == '0':
            return render_template('photo.html',notice='No Opreation Is Selected!')
        op1 = int(op1)
        # Save Uploaded Files
        filename = image.filename
        image.save('./static/uploads/' + filename)
        pathf = './static/uploads/' + filename
        if op1 == 1:
            try:
                path = tojpg(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                return send_file(path, as_attachment=True) 
            except Exception as e:
                return str(e)
        if op1 == 2:
            try:
                path = topdf(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
                
            try:
                return send_file(path, as_attachment=True) 
            except Exception as e:
                return str(e)
        if op1 == 3:
            try:
                path = topng(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                return send_file(path, as_attachment=True) 
            except Exception as e:
                return str(e)
        if op1 == 4:
            try:
                path = extext(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                return send_file(path, as_attachment=True) 
            except Exception as e:
                return str(e)
            
        
        
        return apology("?????")
        
    else:
        return render_template("photo.html",notice='no')





@app.route("/file", methods=["GET", "POST"])
def filee():
    """Show Text Page"""
    if request.method == "POST":
        file = request.files['file']
        if not file:
            return apology("No File Slected")
        op1 = request.values.get("op1")
        op2 = request.values.get("op2")
            
        


        if op1 == '0':
            return apology("file format is not selected")
        op1 = int(op1)
        op2 = int(op2)

        if op1 == op2:
            return apology("Can Not Convert To Same Format")
        
        filename = file.filename
        file.save('./static/uploads/' + filename)
        pathf = './static/uploads/' + filename
        
        
        
        if op1 == 2 and op2 == 1:
            try:
                path = pdftodocx(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                return send_file(path, as_attachment=True) 
            except Exception as e:
                return str(e)
        
        if op1 == 1 and op2 == 2:
             try:
                path = docxtopdf(pathf)
                os.remove(pathf)
             except:
                return apology('Something went wrong please try again')
             try:
                 return send_file(path, as_attachment=True) 
             except Exception as e:
                 return str(e)
        if op1 == 1 and op2 == 3:
            try:
                path = docxtotext(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                 return send_file(path, as_attachment=True) 
            except Exception as e:
                 return str(e)
        if op1 == 2 and op2 == 3:
            try:
                path = pdftotext(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                 return send_file(path, as_attachment=True) 
            except Exception as e:
                 return str(e)
        if op1 == 3 and op2 == 2:
            try:
                path = texttopdf(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                 return send_file(path, as_attachment=True) 
            except Exception as e:
                 return str(e)
        if op1 == 3 and op2 == 1:
            try:
                path = texttodocx(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                 return send_file(path, as_attachment=True) 
            except Exception as e:
                 return str(e)
        else:
            return apology("Tool is offline")
    
       
    
    return render_template("file.html")





@app.route("/video", methods=["GET", "POST"])
def video():
    """Show video Page"""
    if request.method == "POST":
        video = request.files['video']
        op1 = request.values.get('op1')
        
        if not video:
            return render_template('videos.html',notice='No Video Is Selected!')
        if op1 == '0':
            return render_template('videos.html',notice='No Opreation Is Selected!')
        op1 = int(op1)
        filename = video.filename
        video.save('./static/uploads/' + filename)
        pathf = './static/uploads/' + filename
        if op1 == 1:
            try:
                path = exframe(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                return send_file(path, as_attachment=True) 
            except Exception as e:
                return str(e)
        if op1 == 2:
            try:
                path = tobw(pathf,filename)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                return send_file(path, as_attachment=True) 
            except Exception as e:
                return str(e)
        if op1 == 3:
            try:
                path = tosound(pathf)
                os.remove(pathf)
            except:
                return apology('Something went wrong please try again')
            try:
                return send_file(path, as_attachment=True) 
            except Exception as e:
                return str(e)
    else:
        return render_template('videos.html',notice='no')
    
@app.route("/audio", methods=["GET", "POST"])
def audio():
    """Show audio Page"""
    if request.method == "POST":
        audio = request.files['audio']
        if not audio:
            return apology("No audio Slected")
        op1 = request.values.get("op1")
        op2 = request.values.get("op2")
            
        


        if op1 == '0':
            return apology("audio format is not selected")
        op1 = int(op1)
        op2 = int(op2)

        if op1 == op2:
            return apology("Can Not Convert To Same Format")
        
        audioname = audio.filename
        audio.save('./static/uploads/' + audioname)
        pathf = './static/uploads/' + audioname
        try:
            path = converter(op1,op2,pathf)
            os.remove(pathf)
        except:
                return apology('Something went wrong please try again')
        try:
            return send_file(path, as_attachment=True) 
        except Exception as e:
            return str(e)
    else:
        return render_template('audio.html')