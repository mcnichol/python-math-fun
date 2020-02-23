#!/usr/bin/env bash

set -e
K8S_DEPLOY_DIR='../kube-ops-view/deploy/'

if [ -f "$K8S_DEPLOY_DIR/deployment.yaml" ]; then
    sed 's/- --redis-url.*$//' "$K8S_DEPLOY_DIR/deployment.yaml" > "$K8S_DEPLOY_DIR/modified-deployment.yaml"
    mv "$K8S_DEPLOY_DIR/deployment.yaml" "$K8S_DEPLOY_DIR/deployment.bak"
fi

kubectl apply -f ../kube-ops-view/deploy/
