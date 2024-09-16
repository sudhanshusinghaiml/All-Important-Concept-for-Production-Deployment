# After creating repo in git remote we need to merge it with local repo
echo "# deeplearning-misc-functions" >> README.md
git init
git add README.md
git commit -m "initial commit"
git branch -M develop
git remote add origin https://github.com/sudhanshusinghaiml/deeplearning-misc-functions.git
git push -u origin develop

# After renaming branches in remote github.com.
git branch -m main develop
git fetch origin
git branch -u origin/develop develop
git remote set-head origin -a

# ---------------------------------------------------------------------------------------------------------------
# If you have already commited the large files but you are unable to pusblish to repo
# use the below commands to rewrite the branch history

git filter-branch --tree-filter 'rm -f yolov7/yolov7.pt' HEAD
git filter-branch --tree-filter 'rm -f deeplearning-computer-vision/MS3-CNN-Architecture-Transfer-Learning/monkeyImages.npy' HEAD
git filter-branch --tree-filter 'rm -f deeplearning-computer-vision-project/Weights_coco.pb' HEAD

# To remove from cache
git rm --cached yolov7/yolov7.pt
git rm --cached deeplearning-computer-vision/MS3-CNN-Architecture-Transfer-Learning/monkeyImages.npy
git rm --cached deeplearning-computer-vision-project/Weights_coco.pb

git push origin develop

# ---------------------------------------------------------------------------------------------------------------
## A file is not present in the repository. But it was present earlier. 
# Can we see who changed/removed this file last time 

# will give file path as output
git log --diff-filter D --pretty="format:" --name-only | grep object_name

# will give commit details as output
git log -n 2 -- file_path_from_prev_command_output

# will give commit id as output
git log -n 2 --format=%H -- file_path_from_prev_command_output

# use the commit id in which the file was not deleted
git show commit_id_output_from_previous_command	

# This command will replace the content of file with the content that was on the deleted files from the commit
git checkout commit_id_output_from_previous_command -- file_path  
# ---------------------------------------------------------------------------------------------------------------

# To add a reposiotry as submodules in git repository

git clone https://github.com/sudhanshusinghaiml/Twitter-Sentiment-Analysis-for-Airlines.git 

git rm -f --cached Twitter-Sentiment-Analysis-for-Airlines

git submodule add https://github.com/sudhanshusinghaiml/Twitter-Sentiment-Analysis-for-Airlines.git Twitter-Sentiment-Analysis-for-Airlines

git status

git add .

git commit -m "Added Submodules XXXX"

# ---------------------------------------------------------------------------------------------------------------
# If you've performed a git reset --hard and want to undo it, you can use the reflog to find the SHA-1 hash of 
# the commit you were on before the reset and then reset back to that commit.

# This will display a list of recent actions with their corresponding commit hashes.
git reflog

# To move your branch pointer back to that commit 
git reset --hard <commit-hash>

# ---------------------------------------------------------------------------------------------------------------

# To unstage all changes in the previous commits
git reset HEAD~


# If you want to completely undo the changes from the previous commit
# Completely undo the last commit: 
# If you want to completely discard the last commit—changes and all—use the git reset command with the --hard flag
git reset --hard HEAD~

# Undo the last commit but keep the changes: 
# If you want to undo the commit but keep the changes in your working directory, use the git reset command with the --soft flag, followed by HEAD~
git reset --soft HEAD~


'''
	Please be cautious when using git reset --hard, as it can permanently discard changes that have not been committed. 
	Make sure you donot have any important changes in your working directory before executing this command
'''
# ---------------------------------------------------------------------------------------------------------------
#  To undo last 2 commits in your local repository without deleting the files
git reset --soft HEAD~2

'''
This command will move the HEAD pointer of your current branch back one commit (HEAD~1 refers to the commit 
before the current HEAD). The --soft option ensures that the changes from the undone commit are staged but 
not discarded, allowing you to make further modifications or commit them again
'''

# ---------------------------------------------------------------------------------------------------------------

# Stash Local Changes (Safe Option)
### If you want to keep the local changes temporarily and apply them later after pulling:
git stash --include-untracked

### Pull the changes:
git pull origin develop


# We can apply the stashed changes back if needed
git stash pop

# --------------------------------------------------------------------------------------------------------------

If you want to permanently delete a stashed entry in Git (without applying it), follow these steps:

### 1. List all stashed entries
   # First, check all the stashed entries you have:
   git stash list

   # This will give you a list of all stashes, each with an index like `stash@{0}`, `stash@{1}`, etc.

### 2. Delete a specific stash
   # If you want to delete a specific stash, use the following command, replacing `stash@{0}` with the stash you want to delete:
   # This will permanently delete the specified stash.
   git stash drop stash@{0}


### 3. **Delete all stashes**
   # If you want to remove all stashes in one go:
   git stash clear

   # This will permanently delete all stashed entries from your repository.

# After this, the stashes will be permanently removed from Git.

# -----------------------------------------------------------------------------------------------------------