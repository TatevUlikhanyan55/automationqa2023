'''1. Configure the author name and email address
to be used with your commits.
git config --global user.name "Sam Smith"
git config --global user.email sam@example.com

2. Create a new local repository
git init

3. Create a working copy of a local repository:
git clone /path/to/repository

4. Add one or more files to staging (index):
git add <filename>
git add *

5. 	Commit changes to head (but not yet to the remote repository):
git commit -m "Commit message"

6. 	Send changes to the master branch of your remote repository:
git push origin master

7. List the files you've changed and those you still need to add or commit:
git status

8. Create a new branch and switch to it:
git checkout -b <branchname>

9. Switch from one branch to another:
git checkout <branchname>

10. List all the branches in your repo, and also tell you what branch you're currently in:
git branch

11. Delete the feature branch:
git branch -d <branchname>

12. Push the branch to your remote repository, so others can use it:
git push origin <branchname>

13. Push all branches to your remote repository:
git push --all origin

14. Fetch and merge changes on the remote server to your working directory:
git pull

15. To merge a different branch into your active branch:
git merge <branchname>

16. View all the merge conflicts:
View the conflicts against the base file:

Preview changes, before merging:

 merge conflicts:
View the conflicts against the base file:

Preview changes, before merging:

git diff
git diff --base <filename>

git diff <sourcebranch> <targetbranch>

'''