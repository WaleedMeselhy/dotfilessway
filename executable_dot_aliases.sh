#!/bin/bash
alias fixZshHistory="cat -n ~/.zhistory | sort -t ';' -uk2 | sort -nk1 | cut -f2- > ~/.zhistory"

kexec() {
  kubectl exec "$(kubectl get pods | awk '{print $1}' | fzf)" -it -- bash
}
klogs() {
  kubectl logs "$(kubectl get pods | awk '{print $1}' | fzf)"
}