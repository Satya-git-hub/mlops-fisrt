Wine Quality MLOPS

conda create -n wineq python=3.7 -y 
conda activate wineq
touch requirements.txt
pip install -r requirements.txt 
dataset : https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5

git init
dvc init
dvc add data_given/winequality.csv
git add .
git commit -m "first commit"

git remote add origin https://github.com/Satya-git-hub/mlops-fisrt.git
git branch -M main
git push -u origin main

