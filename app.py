# Importing required libraries
from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import os
import shutil

app = Flask(__name__)
# base_dir = '/var/projects'
base_dir = os.getcwd()
print(base_dir)
# exit()

@app.route("/", methods= ['GET'])
def show():
    return render_template("index.html")

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    """
    To submit user input account urls to database
    :return: renders the index.html with parsed data
    """
    if request.method == "POST":
        projectname= request.form.get("projectname")
        Authenticate = request.form.get("Authenticate")
        Git_Url = request.form.get("Git_Url")
        Branch_Name = request.form.get("Branch_Name")
        username = request.form.get("username")
        token = request.form.get("token")
        user_data = {
            "projectname":projectname,
            "Authenticate":Authenticate,
            "Git_Url":Git_Url,
            "Branch_Name":Branch_Name,
            "username": username,
            "token": token
            
        }
        print(user_data)
    
    
       
        
       
       # request_url = f'git clone -b {Branch_Name} @{Git_Url}' /var/projects/projectname
        # request_url = f'git clone -b {Branch_Name}  https://{username}:{token} @{Git_Url}'
        
        if Authenticate == "GitHub" or "GitLab":
            u = Git_Url.split("//")
            url = u[1]
            # 'https://github.com/Nisarg-Satani/ChatBro.git'
            repo_name = u[1].split("/")[-1].split(".")[0]
            print("repo name:", repo_name)

            request_url = f'git clone -b {Branch_Name} https://{username}:{token}@{url}'

            if not os.path.exists(os.path.join(base_dir + f"/{projectname}")):
                print("inside mkdir")
                os.mkdir(f'{projectname}')
            if not os.path.exists(f"{repo_name}"):
                os.system(f"{request_url}")
                shutil.move(f'{repo_name}', f'{projectname}')
                return jsonify({
                    "status": 200,
                    "message": f"{Authenticate} has been cloned!"
                })
            else:
                    return jsonify({
                        "status": 502,
                        "message": f"{url} already there!"
                    })
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)