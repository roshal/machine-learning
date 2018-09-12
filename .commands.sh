:; tail -n +2 .commands.sh; exit
#
git add --all
git commit --allow-empty --allow-empty-message -m ''
git commit --allow-empty --allow-empty-message -m '' --amend
git push origin master
#
pipenv install
pipenv run jupyter notebook
pipenv run python main/main.py
pipenv shell
#
git all && git cam && git pom -f
