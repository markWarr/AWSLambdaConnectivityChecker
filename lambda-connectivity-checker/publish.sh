set -e

find . -name \*.pyc -delete

rm -rf ./dist

mkdir -p ./dist

shopt -s extglob
cp -r ./!(dist) ./dist/

cp -r $(poetry env info -p)/lib/python*/site-packages/* ./dist/


cd ./dist
rm -f ../lambda.zip
zip -r9 ../lambda.zip ./ -x '*.pyc'

cd -
rm -rf dist
