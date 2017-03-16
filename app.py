from flask import Flask
import sys
from github import Github

url = sys.argv[1]
user = url.split("/")


app = Flask(__name__)

@app.route('/v1/<filename>')
def show_file_contents(filename):
 g = Github("akanshamehta17","P@ssw0rd")
 repo = g.get_user(user[3]).get_repo(user[4])
 try:
   file = repo.get_file_contents(filename)
   if file is not None:
     if(filename.endswith(".yml")): 
        file = repo.get_file_contents(filename)
        return file.decoded_content
     if(filename.endswith(".json")):
        file = repo.get_file_contents(filename)
        return file.decoded_content

 except:
   return "Error: File not found" 

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0')

