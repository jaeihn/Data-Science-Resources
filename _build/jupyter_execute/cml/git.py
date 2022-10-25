#!/usr/bin/env python
# coding: utf-8

# # git

# | Command | Description |
# |:--------|:------------|
# | `git pull` | `fetch`+`merge`; Update local repo with remote repo |
# | `git status` | View staging area | 
# | `git add {filename}` | Add file to staging area |
# | `git add -u` | Add updates and deletion of files |
# | `git add .` | Add updates and new files |
# | `git add -A` | Add everything available to staging area |
# | `git add -p` | Add with interactive prompt for each file (y/n) | 
# | `git diff --staged` | Compare the changes in the staging area |
# | `git diff {older_hash} {newer_hash}`| Compare between two commits |
# | `git diff {older_hash}` | Compare with most recent commit | 
# | `git diff {file1} {file2}` | Compare two files in general | 
# | `git restore --staged {filename}` | Unstage file |
# | `git reset` | Unstage all files (default = --mixed) |
# | `git stash` | Temporarily removes local changes from the working area |
# | `git stash pop` | Retrieve the changes that were stowed away |
# | `git commit -m "{message}"` | Commit current staging area with message |
# | `git commit --amend -m "{message}"` | Rewrite most recent unpushed commit message | 
# | `git log` | View commit history | 
# | `git log --oneline` | View commit history (minimal) | 
# | `git log --graph --all --oneline` | Draw tree graph of commit history | 
# | `git switch -c {branch}` | Create and switch to branch | 
# | `git revert` | Create a new commit that reverts previous commits | 
# | `git reset --soft {hash}` | Uncommit, changes are left staged |
# | `git reset --mixed {hash}` | Uncommit + unstage, changes are in working tree |
# | `git reset --hard {hash}` | Uncommit + unstage + delete, nothing left | 
# | `git reset {hash}` | Move forward to undo a `--hard` reset based on `reflog`; NOT GUARANTEED |
# | `git push -f origin` | Force reset commit to remote repo (deletes any commit history in between) |

# ### `.gitignore`
# 
# Place in root directory of the repo, or set globally for all `.git` repos. 
# 
# #### Common `.gitignore_global` template
# 
# ```{bash}
# **/.DS_Store
# **/.ipynb_checkpoints
# **/.Rhistory
# **/__pycache__
# **/.OTTER_LOG
# ```

# ## Q&A
# 
# - [Staging deleted files](https://stackoverflow.com/questions/12373733/staging-deleted-files)
# - [How to write a commit message and description (the proper way)](https://medium.com/@steveamaza/how-to-write-a-proper-git-commit-message-e028865e5791)
