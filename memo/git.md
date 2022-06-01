# Version Control


## Git
git config --global user.name "<name>"
git config --global user.email "<email address>"
git config --global core.fileMode false

git init
git status
git remote -v；
git remote add upstream git@github.com:xxx/xxx.git
git diff
git fetch --all

git checkout <branch-name>
git checkout -b <branch-name>

git merge [--no-ff] <branch name>
git merge upstream/master
git merge master --allow-unrelated-histories

git pull <remote> <branch>
git push origin --delete <branch-name>
git push <remote> <branch>

git checkout <file>
git checkout .

git tag
git tag <tag name>
git tag -a <tag name> -m "<comment>"
git push origin <tag name>
git tag -d <tag name>
git push origin :refs/tags/<tag name>


#### branch
git branch
git branch -r
git branch -a
git branch -D <branch-name>

新建一个分支，但依然停留在当前分支
git branch <branch-name>
建立追踪关系，在现有分支与指定的远程分支之间
git branch --set-upstream <branch> <remote-branch>
在本地创建和远程分支对应的分支
git checkout -b branch-name origin/branch-name（本地和远程分支的名称最好一致）

#### log
git log
git log --oneline --decorate --graph --all
git log --graph --decorate --oneline --simplify-by-decoration --all
git log --graph --pretty=oneline --abbrev-commit

查看命令历史
git reflog

#### stash
git stash (save <stash name>)
git stash pop
git stash pop/apply/list/clear/show/drop
git stash branch <branch name> <stash name>

#### pull subset
git clone --depth=1 <repository>
git config core.sparseCheckout true

#### submodule
git submodule add <repository>
git submodule init
git submodule update
git submodule foreach <command>
git config -f .gitmodules submodule.xxx.branch stable

#### delete submodule
1. 删除子模块文件夹 $git rm --cached assets $rm -rf assets
2. 删除.gitmodules文件中相关子模块信息
3. 删除.git/config中的相关子模块信息
4. 删除.git文件夹中的相关子模块文件

#### sync with remote
git remote show origin
git remote prune origin

#### recover
git reset --hard HEAD^
git reset --hard origin/master

重置暂存区与工作区，与上一次commit保持一致
git reset --hard <commit id>
不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令 git reset HEAD <file>，第二步用命令 git checkout <file>。

#### delete commit record
git checkout --orphan <branch name>
git add -A
git commit -am "comment"
git branch -D <main>
git branch -m <main>
git push -f origin <main>

git merge --squash <branch name>

####
.gitattributes
git rm --cached -r
git reset --hard

git config --get core.attributesFile
git config --global --get core.attributesFile


## SVN
svn co <url> <path> --username  --password

svn status
svn diff -r <number>:<number>
svn merge <url>@xxx <url>@xxx <path>
svn merge -r <version>:<version>

svn resolve  --accept <option> <path>
svn resolve –-accept working a.txt
svn resolve --accept=theirs-conflict file.c

svn st | awk '{if($1=="?") {print $2}}' | xargs svn add

svn diff <url_merge_from> <url_merge_to> | grep @@
svn diff <url_merge_from> <url_merge_to>
svn diff -r <end_version>:<start_version>
svn log --stop-on-copy <url_merge_from>
svn diff --old=<url_merge_from>@<start_version> --new=<url_merge_from>
svn export --username abc --password 123  -r <svn_version> <svn_url> <project_name>
