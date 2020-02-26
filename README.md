# Math and Python
Working through mathematical concepts with Python

## Setup
```shell script
#Download Repo
$> git clone https://github.com/mcnichol/python-math-fun.git && cd python-math-fun  

# Setup Python virtualenv
$/python-math-fun> python3 -m venv venv
$/python-math-fun> . venv/bin/activate

# Install Project Deps (and optionally dev deps if testing)
$/python-math-fun> pip install -r requirements.txt

# Run vector server locally
$/python-math-fun> python app/vectory-server.py

# Call server locally via curl
$/python-math-fun> curl localhost:8080/
```

## Demo Links to Follow along with

[KPack Demo Repo](https://github.com/mcnichol/python-math-fun)

[Kind Local K8s Quick Start](https://kind.sigs.k8s.io/docs/user/quick-start/)

Install Binary (Mac/Linux)
```
curl -Lo ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.7.0/kind-$(uname)-amd64
chmod +x ./kind
mv ./kind /some-dir-in-your-PATH/kind
```

Or install with Brew  (Mac)
```
brew install kind
```

[Metrics Server](https://github.com/kubernetes-sigs/metrics-server)   
`git clone https://github.com/kubernetes-sigs/metrics-server --depth=1`  

[Kube Ops View](https://github.com/mcnichol/kube-ops-view) *FORKED from hjacobs*   
`git clone https://github.com/mcnichol/kube-ops-view --depth=1`  

[KPack Release](https://github.com/pivotal/kpack/releases)  

