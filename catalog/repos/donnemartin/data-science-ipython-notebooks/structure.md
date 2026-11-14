# Project structure: donnemartin/data-science-ipython-notebooks

**Analysed commit:** `5b3c00d462c6e9200315afe46d0093948621eb95`

**Commit reference:** [5b3c00d462c6e9200315afe46d0093948621eb95](https://github.com/donnemartin/data-science-ipython-notebooks/commit/5b3c00d462c6e9200315afe46d0093948621eb95)

**Tree at this commit:** [donnemartin/data-science-ipython-notebooks@5b3c00d462c6](https://github.com/donnemartin/data-science-ipython-notebooks/tree/5b3c00d462c6e9200315afe46d0093948621eb95)

Static snapshot only. Repository code was not executed. Paths below are the files the analyser kept after size, binary, vendored, and secret exclusions.

| Item | Value |
| --- | --- |
| Repository | donnemartin/data-science-ipython-notebooks |
| Description | Data science Python notebooks: Deep learning (TensorFlow, Theano, Caffe, Keras), scikit-learn, Kaggle, big data (Spark, Hadoop MapReduce, HDFS), matplotlib, pandas, NumPy, SciPy, Python essentials, AWS, and various command lines. |
| Stars | 29391 |
| Forks | 7996 |
| Licence | Other |
| Language | Python |
| Default branch | master |
| Analysed commit | `5b3c00d462c6e9200315afe46d0093948621eb95` |
| Retrieved at | 2026-11-14T19:07:15.774525+00:00 |
| Files in this snapshot | 170 |

## Directory tree

```text
analyses/  (2 files)
  __init__.py
  churn_measurements.py
aws/  (2 files)
  __init__.py
  aws.ipynb
commands/  (4 files)
  styles/  (1 files)
    custom.css
  __init__.py
  linux.ipynb
  misc.ipynb
data/  (10 files)
  titanic/  (8 files)
    genderclassmodel.csv
    genderclassmodel.py
    gendermodel.csv
    gendermodel.py
    myfirstforest.py
    results-rf.csv
    test.csv
    train.csv
  ozone.csv
  ozone_copy.csv
deep-learning/  (58 files)
  keras-tutorial/  (26 files)
    data/  (1 files)
      … 1 files under this directory
    deep_learning_models/  (6 files)
      … 6 files under this directory
    solutions/  (2 files)
      … 2 files under this directory
    0. Preamble.ipynb
    1.2 Introduction - Theano.ipynb
    1.3 Introduction - Keras.ipynb
    1.4 (Extra) A Simple Implementation of ANN for MNIST.ipynb
    2.1 Supervised Learning - ConvNets.ipynb
    2.2.1 Supervised Learning - ConvNet HandsOn Part I.ipynb
    2.2.2 Supervised Learning - ConvNet HandsOn Part II.ipynb
    2.3 Supervised Learning - Famous Models with Keras.ipynb
    3.2 RNN and LSTM.ipynb
    3.3 (Extra) LSTM for Sentence Generation.ipynb
    4. Conclusions.ipynb
    LICENSE
    data_helpers.py
    deep-learning-osx.yml
    deep-learning.yml
    outline.md
    w2v.py
  tensor-flow-examples/  (12 files)
    notebooks/  (9 files)
      … 9 files under this directory
    Setup_TensorFlow.md
    input_data.py
    multigpu_basics.py
  tensor-flow-exercises/  (7 files)
    1_notmnist.ipynb
    2_fullyconnected.ipynb
    3_regularization.ipynb
    4_convolutions.ipynb
    6_lstm.ipynb
    Dockerfile
    README.md
  theano-tutorial/  (13 files)
    intro_theano/  (3 files)
      … 3 files under this directory
    rnn_tutorial/  (6 files)
      … 6 files under this directory
    scan_tutorial/  (3 files)
      … 3 files under this directory
    theano_mlp/  (1 files)
      … 1 files under this directory
kaggle/  (1 files)
  __init__.py
mapreduce/  (4 files)
  __init__.py
  mapreduce-python.ipynb
  mr_s3_log_parser.py
  test_mr_s3_log_parser.py
matplotlib/  (11 files)
  tests/  (1 files)
    __init__.py
  04.00-Introduction-To-Matplotlib.ipynb
  04.02-Simple-Scatter-Plots.ipynb
  04.03-Errorbars.ipynb
  04.05-Histograms-and-Binnings.ipynb
  04.08-Multiple-Subplots.ipynb
  04.09-Text-and-Annotation.ipynb
  04.15-Further-Resources.ipynb
  __init__.py
  matplotlib-applied.ipynb
  matplotlib.ipynb
misc/  (2 files)
  Algorithmia.ipynb
  regex.ipynb
numpy/  (13 files)
  tests/  (1 files)
    __init__.py
  02.00-Introduction-to-NumPy.ipynb
  02.01-Understanding-Data-Types.ipynb
  02.02-The-Basics-Of-NumPy-Arrays.ipynb
  02.03-Computation-on-arrays-ufuncs.ipynb
  02.04-Computation-on-arrays-aggregates.ipynb
  02.05-Computation-on-arrays-broadcasting.ipynb
  02.06-Boolean-Arrays-and-Masks.ipynb
  02.07-Fancy-Indexing.ipynb
  02.08-Sorting.ipynb
  02.09-Structured-Data-NumPy.ipynb
  __init__.py
  numpy.ipynb
pandas/  (16 files)
  tests/  (1 files)
    __init__.py
  03.00-Introduction-to-Pandas.ipynb
  03.01-Introducing-Pandas-Objects.ipynb
  03.02-Data-Indexing-and-Selection.ipynb
  03.03-Operations-in-Pandas.ipynb
  03.04-Missing-Values.ipynb
  03.05-Hierarchical-Indexing.ipynb
  03.06-Concat-And-Append.ipynb
  03.07-Merge-and-Join.ipynb
  03.08-Aggregation-and-Grouping.ipynb
  03.09-Pivot-Tables.ipynb
  03.10-Working-With-Strings.ipynb
  03.12-Performance-Eval-and-Query.ipynb
  03.13-Further-Resources.ipynb
  __init__.py
  pandas.ipynb
python-data/  (15 files)
  tests/  (3 files)
    __init__.py
    test_transform_util.py
    test_type_util.py
  __init__.py
  datetime.ipynb
  files.ipynb
  functions.ipynb
  hello_world.txt
  logs.ipynb
  pdb.ipynb
  structs.ipynb
  structs_utils.ipynb
  transform_util.py
  type_util.py
  unit_tests.ipynb
scikit-learn/  (14 files)
  fig_code/  (9 files)
    ML_flow_chart.py
    __init__.py
    data.py
    figures.py
    helpers.py
    linear_regression.py
    scikit-learn.ipynb
    sgd_separator.py
    svm_gui.py
  tests/  (1 files)
    __init__.py
  __init__.py
  scikit-learn-gmm.ipynb
  scikit-learn-linear-reg.ipynb
  scikit-learn-pca.ipynb
scipy/  (10 files)
  tests/  (1 files)
    __init__.py
  2002FemPreg.dct
  __init__.py
  effect_size.ipynb
  first.py
  hypothesis.ipynb
  nsfg.py
  sampling.ipynb
  thinkplot.py
  thinkstats2.py
spark/  (3 files)
  __init__.py
  hdfs.ipynb
  spark.ipynb
.gitattributes
.gitignore
LICENSE
README.md
__init__.py
```

## Entry points

- [deep-learning/keras-tutorial/deep_learning_models/resnet50.py:235](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/deep-learning/keras-tutorial/deep_learning_models/resnet50.py#L235)
- [deep-learning/keras-tutorial/deep_learning_models/vgg16.py:154](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/deep-learning/keras-tutorial/deep_learning_models/vgg16.py#L154)
- [deep-learning/keras-tutorial/deep_learning_models/vgg19.py:156](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/deep-learning/keras-tutorial/deep_learning_models/vgg19.py#L156)
- [deep-learning/keras-tutorial/w2v.py:53](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/deep-learning/keras-tutorial/w2v.py#L53)
- [mapreduce/mr_s3_log_parser.py:136](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/mapreduce/mr_s3_log_parser.py#L136)
- [scikit-learn/fig_code/ML_flow_chart.py:129](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/scikit-learn/fig_code/ML_flow_chart.py#L129)
- [scikit-learn/fig_code/linear_regression.py:35](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/scikit-learn/fig_code/linear_regression.py#L35)
- [scikit-learn/fig_code/sgd_separator.py:38](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/scikit-learn/fig_code/sgd_separator.py#L38)
- [scikit-learn/fig_code/svm_gui.py:340](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/scikit-learn/fig_code/svm_gui.py#L340)
- [scipy/first.py:156](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/scipy/first.py#L156)
- [scipy/nsfg.py:105](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/scipy/nsfg.py#L105)
- [scipy/thinkplot.py:715](https://github.com/donnemartin/data-science-ipython-notebooks/blob/5b3c00d462c6e9200315afe46d0093948621eb95/scipy/thinkplot.py#L715)

## Main components

| Component | Kind | Status | Responsibility |
| --- | --- | --- | --- |
| analyses package | library | Observed | Groups 2 file(s) under analyses package (observed from repository paths and static analysis). Observed top-level functions: calibration, discrimination. |
| aws package | library | Observed | Groups 1 file(s) under aws package (observed from repository paths and static analysis). |
| commands package | library | Observed | Groups 1 file(s) under commands package (observed from repository paths and static analysis). |
| Configuration and deployment | config | Observed | Groups 3 file(s) under configuration and deployment (observed from repository paths and static analysis). |
| Core modules | core | Observed | Groups 1 file(s) under core modules (observed from repository paths and static analysis). |
| Data layer | data | Observed | Groups 3 file(s) under data layer (observed from repository paths and static analysis). |
| deep-learning package | library | Observed | Groups 12 file(s) under deep-learning package (observed from repository paths and static analysis). Observed top-level classes: DataSet, LogisticRegression, LstmLayer, SimpleRNN. Observed top-level functions: _read32, b… |
| Application entry point | entrypoint | Observed | Groups 13 file(s) under application entry point (observed from repository paths and static analysis). Observed top-level classes: Beta, Cdf, ControllBar, Controller, Dirichlet, EstimatedPdf. Observed top-level functions… |
| kaggle package | library | Observed | Groups 1 file(s) under kaggle package (observed from repository paths and static analysis). |
| mapreduce package | library | Observed | Groups 1 file(s) under mapreduce package (observed from repository paths and static analysis). |
| matplotlib package | library | Observed | Groups 1 file(s) under matplotlib package (observed from repository paths and static analysis). |
| numpy package | library | Observed | Groups 1 file(s) under numpy package (observed from repository paths and static analysis). |
| pandas package | library | Observed | Groups 1 file(s) under pandas package (observed from repository paths and static analysis). |
| python-data package | library | Observed | Groups 3 file(s) under python-data package (observed from repository paths and static analysis). Observed top-level classes: TransformUtil, TypeUtil. |
| scikit-learn package | library | Observed | Groups 5 file(s) under scikit-learn package (observed from repository paths and static analysis). Observed top-level functions: linear_data_sample, linear_data_sample_big_errs, plot_example_decision_tree, plot_image_com… |
| scipy package | library | Observed | Groups 1 file(s) under scipy package (observed from repository paths and static analysis). |
| spark package | library | Observed | Groups 1 file(s) under spark package (observed from repository paths and static analysis). |
| Tests | test | Observed | Groups 9 file(s) under tests (observed from repository paths and static analysis). Observed top-level classes: MrTestsUtil, TestMrS3LogParser, TestTransformUtil, TestUtil. |

## Important files

- `deep-learning/keras-tutorial/deep-learning-osx.yml` (config)
- `deep-learning/keras-tutorial/deep-learning.yml` (config)
- `deep-learning/tensor-flow-exercises/Dockerfile` (container)

## Top-level layout

- `deep-learning` — 58 analysed file(s)
- `pandas` — 16 analysed file(s)
- `python-data` — 15 analysed file(s)
- `scikit-learn` — 14 analysed file(s)
- `numpy` — 13 analysed file(s)
- `matplotlib` — 11 analysed file(s)
- `data` — 10 analysed file(s)
- `scipy` — 10 analysed file(s)
- `(root files)` — 5 analysed file(s)
- `commands` — 4 analysed file(s)
- `mapreduce` — 4 analysed file(s)
- `spark` — 3 analysed file(s)
- `analyses` — 2 analysed file(s)
- `aws` — 2 analysed file(s)
- `misc` — 2 analysed file(s)
- `kaggle` — 1 analysed file(s)

## Limitations

- Static analysis only: repository code was not executed, installed, or imported at runtime.
- Components and relationships are inferred from file paths, imports, and AST structure; runtime behaviour, dynamic imports, and reflection may not be visible.
- File data/titanic/gendermodel.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File data/titanic/myfirstforest.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File deep-learning/keras-tutorial/solutions/sol_111.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File deep-learning/keras-tutorial/solutions/sol_112.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File deep-learning/tensor-flow-examples/multigpu_basics.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- File deep-learning/theano-tutorial/rnn_tutorial/lstm_text.py could not be parsed as Python (possible SyntaxError) and was skipped for AST analysis.
- Repository text was treated as untrusted data; no instructions found in repository files were followed, and likely secret values were redacted/excluded.

Commit `5b3c00d462c6e9200315afe46d0093948621eb95` is the revision these paths and observations refer to.
