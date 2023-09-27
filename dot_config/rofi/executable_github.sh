#!/bin/zsh
repo="/home/waleed/work/one"
previous_command_loc_file=/tmp/github_prs
chdir $repo
if [ "$ROFI_RETV" != "0" ]; then
    selected="$*"
    if [ "$selected" = "Authors:" ]; then
        echo "authors" >"${previous_command_loc_file}"
        gh pr list --json number,title,headRefName,author \
            --template '{{range .}}{{tablerow (.author.login | color "yellow") }}{{end}}' |
            sort | uniq
    elif [ -f "${previous_command_loc_file}" ]; then
        previous_command=$(cat "${previous_command_loc_file}")
        if [ "$previous_command" = "authors" ]; then
            echo "author" >"${previous_command_loc_file}"
            gh pr list --author "$selected" --json number,title,headRefName,author \
                --template '{{range .}}{{tablerow (printf "#%v" .number | autocolor "green") .title }}{{end}}'
        elif [ "$previous_command" = "author" ]; then
            pr_number=$(echo $selected | awk '{print $1}')
            pr_number="${pr_number:1}"
            xdg-open https://github.com/MoneyHash/one/pull/$pr_number </dev/null >/dev/null 2>&1 &
            rm -f $previous_command_loc_file
        fi
    fi
fi
if [ "$ROFI_RETV" = "0" ]; then
    echo Authors:
fi
