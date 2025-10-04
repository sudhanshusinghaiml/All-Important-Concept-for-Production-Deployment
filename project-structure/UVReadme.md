# [Settingup Project using UV](https://docs.astral.sh/uv/guides/projects/)

## Create a new UV environment
  - uv venv .venv
	
## Activate the environment
	- (Mac/Linux) source .venv/bin/activate
	- (Windows) .venv\Scripts\activate
	
## Create Project using below commands(if you do not have project code)
	- uv init myproject
	- cd myproject
	- uv add openai
	
## If you already have Python code but no pyproject.toml. We can run it inside your existing project folder — it won’t overwrite your code, just create pyproject.toml
	- uv init

## Converting local repository to git repository
	- git init
	- curl https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore -o .gitignore
	- Create a repository in remote with repo name - "cardatabase-repo". 
	- git remote add origin https://github.com/sudhanshusinghaiml/cardatabase-repo.git
	- git branch -M develop
	- git commit -m "Initial commit"
