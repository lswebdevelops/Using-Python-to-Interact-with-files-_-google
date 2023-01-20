#!/bin/bash

while read line; do
words=($line)
capitalized_words=()
for word in "${words[@]}"; do
capitalized_words+=($(echo "${word^}"))
done
echo "${capitalized_words[@]}"
done
