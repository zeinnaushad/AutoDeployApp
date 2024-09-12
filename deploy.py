import subprocess 
 
def deploy_app(): 
    subprocess.run(["git", "pull", "origin", "master"], check=True) 
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True) 
    subprocess.run(["python", "app.py"], check=True) 
 
if __name__ == "__main__": 
    deploy_app() 
