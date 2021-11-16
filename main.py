from flask import render_template, request
from app import app
import json

@app.route('/', methods=['GET', 'POST'])
def hello():
    
   
    print (str(request.method))
    
    if request.method == 'POST':    
       
            print("entrou")
            result = request.values
            
            print(result["email"])
     
    return render_template('test.html')   

app.run(debug=True)