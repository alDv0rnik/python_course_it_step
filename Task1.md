mkdir homework1
cd homework1
git init
vi homeworck.txt
git remote add origin https://github.com/Tairoks/homework1.git
git add
git commit -m "first commit"
git push -u origin master
git branch develop
git checkout develop
git checkout -b develop1
vi homework.txt
git add .
git commit -m "new entry"
git push origin develop1
cd ..

mkdir aaa
cd aaa
git clone https://github.com/Tairoks/homework1.git
cd homework1
git branch -a 
git checkout -b develop2
vi homework.txt
git add .
git commit -m "new commit"
git push origin develop2
git checkout develop
git merge develop2
git merge develop1
vi homework.txt
git add .
git push
