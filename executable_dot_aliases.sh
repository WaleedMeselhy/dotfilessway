#!/bin/bash
alias fixZshHistory="cat -n ~/.zhistory | sort -t ';' -uk2 | sort -nk1 | cut -f2- > ~/.zhistory"
