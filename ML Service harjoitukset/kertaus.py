# 1) Lue AML työtila-konfigurointi:
with open('../ws_conf.json', 'r') as myfile:
    data = myfile.read()# parse file
    conf = json.loads(data)

# 2) Luo yhteys AML työtilaan:
from azureml.core import Workspace
import json


# 3) Datan haku:
from sklearn.datasets import load_breast_cancer
X,y = load_breast_cancer(return_X_y=True)

# 4) Datan jakaminen:
from sklearn.model_selection import train_test_split


# 5) Luo eksperimentti:
from azureml.core import Experiment

# 6) Mallin koulutus:
from sklearn.linear_model import LogisticRegression

C = 0.2 # regularisointiparametri

with experiment.start_logging() as run:
	model = LogisticRegression(...)
	model.fit(...)


# 7) Mallin rekisteröinti:
run = [r for r in experiment.get_runs()][0]
model = run.register_model(...)

# 8) Ennustelogiikan luonti:


# 9) Python-ympäristön määrittely:
from azureml.core.conda_dependencies import CondaDependencies
from azureml.core.environment import Environment


# 10) Ennustepalvelun luonti:
from azureml.core.model import InferenceConfig, Model
from azureml.core.webservice import AciWebservice, Webservice

inference_config = ...
deployment_config = ...
service = Model.deploy(...)

# 11) Palvelun testaus:
test_samples = json.dumps({"data": data['test']['X'][0,:].tolist()})
service.run(...)

# 12) Palvelun lopetus:
service.delete()
