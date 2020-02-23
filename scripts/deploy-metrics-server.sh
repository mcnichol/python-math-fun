#!/usr/bin/env bash

set -e
METRICS_SERVER_DEPLOY_DIR='../metrics-server/deploy/kubernetes'

if [ -f "$METRICS_SERVER_DEPLOY_DIR/metrics-server-deployment.yaml" ]; then
#Indentation matters in this conditional, below command is split over three lines
sed 's/secure-port=4443$/secure-port=4443\
          - --kubelet-insecure-tls\
          - --kubelet-preferred-address-types=InternalIP/' "$METRICS_SERVER_DEPLOY_DIR/metrics-server-deployment.yaml" > "$METRICS_SERVER_DEPLOY_DIR/modified-metrics-server-deployment.yaml"

   echo "$METRICS_SERVER_DEPLOY_DIR/"
   ls "$METRICS_SERVER_DEPLOY_DIR/"

   mv "$METRICS_SERVER_DEPLOY_DIR/metrics-server-deployment.yaml" "$METRICS_SERVER_DEPLOY_DIR/metrics-server-deployment.bak"
fi

kubectl apply -f ../metrics-server/deploy/kubernetes
