import os
import git
from flask import Flask, render_template, current_app
from dataclasses import dataclass
from datetime import datetime

app = Flask(__name__)


@dataclass(order=True)
class InfoIndex:
    name: str
    time: str

def is_git_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False

def get_git_repos(repo_path):
    dirs = os.scandir(repo_path)
    
    repos_info = []
    for dir in dirs:
        dir_path = os.path.join(repo_path, dir.name)
        if (is_git_repo(dir_path)):
            repo = git.Repo(dir_path)
            last_commit = repo.head.commit
            info = InfoIndex(dir.name, 
                             last_commit.committed_datetime.strftime("%d %b, %Y"))
            repos_info.append(info)
    repos_info.sort()
    return repos_info 

@app.route("/")
def index():
    repos = get_git_repos(current_app.repo)

    return render_template("index.html", repos=repos)

@app.route("/")
def repo_index():
    pass

