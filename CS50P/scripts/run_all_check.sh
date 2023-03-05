#!/usr/bin/bash
script_dir=`dirname $0`
pushd $script_dir
for py_file in `find . -name '*.py' | sort`
do
  my_dir=`dirname $py_file`
  pushd $my_dir
  echo "check50 cs50/problems/2022/python/`basename $my_dir`"
  check50 cs50/problems/2022/python/`basename $my_dir`
  popd
done
popd