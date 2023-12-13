#!/bin/sh

echo $1 | ./piper \
  -m en_us-bosa-medium.onnx \
  -c en_us-bosa-medium.onnx.json \
  -f test1.wav
