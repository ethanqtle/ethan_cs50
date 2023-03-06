#!/usr/bin/bash
getSlugName(){
    myDir=`pwd`
    slugName=`basename $myDir`
    if [[ $slugName =~ ^test_ ]]
    then
        slugName=${slugName/test_/tests/}
    fi
    echo $slugName
}

slugName=$(getSlugName)

echo "slugName == $slugName"
echo "submit50 cs50/problems/2022/python/$slugName"
submit50 cs50/problems/2022/python/$slugName