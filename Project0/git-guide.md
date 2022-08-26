# Project 0 - Git Guide

**Name:** Justin Do  

**Email:** do.20@wright.edu

## Command line git

- **status**
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- **clone**
  - A Git command line utility which is used to target an existing repository and create a clone, or copy of the target repository.
  - `git clone`
- **add**
  - The first command in a chain of operations that directs Git to "save" a snapshot of the current project state, into the commit history. 
  - When used on its own, git add will promote pending changes from the working directory to the staging area.
  - `git add [file name]`
- **rm**
  - rm - remove files or directories
  - `rm [OPTION]... [FILE]...`
- **commit**
  - The `git commit` command captures a snapshot of the project's currently staged changes. 
  - `git commit [file name]`
- **push**
  - The git push command is used to upload local repository content to a remote repository.
  - Pushing is how you transfer commits from your local repository to a remote repo. 
  - `git push [file name]`
- **fetch**
  - The git fetch command downloads commits, files, and refs from a remote repository into your local repo. 
  - Fetching is what you do when you want to see what everybody else has been working on. 
  - `git fetch`
- **merge**
  - Merging is Git's way of putting a forked history back together again. 
  - The git merge command lets you take the independent lines of development created by git branch and integrate them into a single branch.
  - `git merge [branch name]`
- **pull**
  -The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. 
  - `git pull`
- **branch**
  - A branch represents an independent line of development. Branches serve as an abstraction for the edit/stage/commit process.
  - New commits are recorded in the history for the current branch, which results in a fork in the history of the project.
  - `git branch [name]`
- **checkout**
  - A "checkout" is the act of switching between different versions of a target entity. 
  - The git checkout command operates upon three distinct entities: files, commits, and branches. 
  - `git checkout [branch name]`
- ~~init~~
- ~~remote~~

## git files & folders

- **.git folder**
  - The .git folder contains all information that is necessary for the project and all information relating commits, remote repository address, etc.
  - It also contains a log that stores the commit history. This log can help you to roll back to the desired version of the code.
- **.gitignore file**
  - A .gitignore file is a plain text file where each line contains a pattern for files/directories to ignore. 
  - Generally, this is placed in the root folder of the repository, and that's what I recommend. 
  - However, you can put it in any folder in the repository and you can also have multiple .gitignore files.
- ~~.git/hooks~~

## GitHub

- **Pull requests**
  - Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. 
  - Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch.
- **SSH authentication to repositories**
  - You can access and write data in repositories on GitHub.com using SSH (Secure Shell Protocol). 
  - When you connect via SSH, you authenticate using a private key file on your local machine.
- ~~Actions~~
