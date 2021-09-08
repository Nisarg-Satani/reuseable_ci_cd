# Importing required libraries
import git
from git import Repo
from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import os

app = Flask(__name__)
base_dir = os.getcwd()


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
        Project_name = request.form.get("Project_name")
        Authenticate = request.form.get("Authenticate")
        Git_Url = request.form.get("Git_Url")
        Branch_Name = request.form.get("Branch_Name")
        username = request.form.get("username")
        token = request.form.get("token")
        w3review = request.form.get("w3review")
        user_data = {
            "Project_name":Project_name,
            "Authenticate":Authenticate,
            "w3review": w3review,
            "Git_Url":Git_Url,
            "Branch_Name":Branch_Name,
            "username": username,
            "token": token

        }
        print(user_data)
        print(w3review)
        var1=w3review
        if Authenticate == "AzureRepo":
            u=Git_Url.split("@")
            url=u[1]
        elif Authenticate == "GitHub":
          u=Git_Url.split("//")
          url=u[1]
        elif Authenticate == "GitLab":
          u=Git_Url.split("//")
          url=u[1]
        # request_url = f'git clone -b {Branch_Name} @{Git_Url}'
        # request_url = f'git clone -b {Branch_Name}  https://{username}:{token} @{Git_Url}'
       
        request_url = f"https://{username}:{token}@{url}"
        
        parent_dir="F:/var/projects"

        path = os.path.join(parent_dir,Project_name)
        
        os.mkdir(path)
        
        if  os.path.exists(path):
            Repo.clone_from(request_url,path, branch=Branch_Name)
            os.system(f"{request_url}")
            os.chdir('F:/var/projects')
            os.chdir(Project_name)
            os.system(var1)
            # if os.path.isfile('filename.txt'):
            #     print ("File exist")
            # else:
            #     print ("File not exist")
            return jsonify({
                "status": 200,
                "message": f"{url} has been cloned!"
            })
        else:
            return jsonify({
                "status": 502,
                "message": f"{url} already there!"
            })
    return render_template("index.html")


if __name__ == "__main__":
     app.run(debug=True, host="0.0.0.0", port=5000)