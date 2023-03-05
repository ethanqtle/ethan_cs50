#!/usr/bin/bash
cd /workspaces/77242606
my_git=../ethan_cs50/CS50P
cp -fr scripts $my_git/.
cp -fr pset* $my_git/.

pushd $my_git
git add -A
git commit -a -m "Update from workspace"
git push
popd