from flask import Flask
from github import Github,GithubException
import sys
import getpass


url = sys.argv[1] ##Fetching the URL from command line argument 
user = url.split("/") ##Splitting the URL to extract user and repository name

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route('/v1/<filename>') ##attaching variable <filename> to the url '/v1' for runtime
def show_file_contents(filename):
  git_id =  raw_input('\n\nEnter your Github Id:')
  git_pwd = getpass.getpass('Enter your Github Password:') 
 
  try: ##validating github credentials
     g = Github(git_id,git_pwd)##connecting to github via PyGithub api
     if g is not None:
       repo = g.get_user(user[3]).get_repo(user[4])##fetching repository in order to access it's objects
       
  except:
      print("Invalid Id/Password. Please try again.")
      sys.tracebacklimit=0
      sys.exit(1)
      

  try: ##handling exception if filename not found
    if filename is not None: 
      if(filename.endswith(".yml")): 
         file = repo.get_file_contents(filename) 
         return file.decoded_content 
      elif(filename.endswith(".json")):
         file = repo.get_file_contents(filename)
         return file.decoded_content

  except:
    return "Error: File not found" 

if __name__ == "__main__":
  app.run(debug=True,host='0.0.0.0')##Running the app


