#!/usr/bin/bash
script_dir=`dirname $0`
script_dir=`realpath $script_dir`
pushd $script_dir/..
for py_file in `find . -name '*.py' | sort`
do
  my_dir=`dirname $py_file`
  pushd $my_dir
  $script_dir/mycheck.sh
  popd
done
popd