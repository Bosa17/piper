#!/bin/sh

echo $1 | ./piper \
  -m de-bosa-de-tts-medium.onnx \
  -c de-bosa-de-tts-medium.onnx.json \
  -f test1.wav
