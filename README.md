# twitter-faves
An analysis on my preferences on twitter. This is a work in progress. Its 
purpose is to serve as workshop material to present jupyter 
notebooks, python and its data science ecosystem. 
Herein I use mainly `nltk`, `scikit-learn` and `pandas`.

## Notebook index
The notebooks present a very simple pipeline in the following order:
1. [`collecting-data.ipynb`](./collecting-data.ipynb)
2. [`cleaning-data.ipynb`](./cleaning-data.ipynb)
3. [`clustering-tweets.ipynb`](./clustering-tweets.ipynb)


## Running the jupyter notebooks

All dependencies are listed in [`environment.yml`](./environment.yml).
To create an environment with the required dependencies (first install `conda`):

```
cd <cloned repo directory>
conda install -f environment.yml
```

This environment will be created with the name `twitter-faves`. To activate it, 
run:

```
source activate twitter-faves
```

finally, to start a JupyterLab "IDE", run:

```
jupyter lab
```
