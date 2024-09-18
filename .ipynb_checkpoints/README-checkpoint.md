Markov Affinity-based Graph Imputation of Cells (MAGIC)
-------------------------------------------------------

### Environment
```
git config --global user.email "eliu11037@gmail.com"
git config --global user.name "Yuyu-Liu11037"
conda create -n MAGIC python=3.10
source activate MAGIC
conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=12.1 -c pytorch -c nvidia
pip install anndata scanpy leidenalg
```

### Data
```
cd data
pip install gdown
gdown https://drive.google.com/uc?id=1raqlykXvm5wHjam1Up0SHYT-7gq7coz4
gdown https://drive.google.com/uc?id=1pilLsl2N1HX_US_Y6X6eAwmXaPso_1Mu
```