from flask import Flask
import sys
from github import Github


url = sys.argv[1] ##Fetching the URL from command line argument 
user = url.split("/") ##Splitting the URL to extract user and repository name

app = Flask(__name__)

@app.route('/v1/<filename>') ##attaching variable <filename> to the url '/v1' for runtime
def show_file_contents(filename):
 g = Github("akanshamehta17","P@ssw0rd") ##connecting to github via PyGithub api
 repo = g.get_user(user[3]).get_repo(user[4]) ##fetching repository in order to access it's objects 
 try: ## handling exception if file not found
   if filename is not None: 
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


