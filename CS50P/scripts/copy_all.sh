#!/usr/bin/bash
if [[ "$1" != "" ]];
then
    comment=$1
else
    comment="Update from workspace"
fi
echo "comment == $comment"
cd /workspaces/77242606
my_git=../ethan_cs50/CS50P
cp -fr scripts $my_git/.
cp -fr pset* $my_git/.

pushd $my_git
git add -A
git commit -a -m "${comment}"
git push
popd