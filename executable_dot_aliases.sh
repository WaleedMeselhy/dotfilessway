#!/bin/zsh
alias fixZshHistory="cat -n ~/.zhistory | sort -t ';' -uk2 | sort -nk1 | cut -f2- > ~/.zhistory"

kexec() {
    kubectl exec "$(kubectl get pods | awk '{print $1}' | fzf)" -it -- bash
}
klogs() {
    kubectl logs -f "$(kubectl get pods | awk '{print $1}' | fzf)"
}
kcontext() {
    kubectl config use-context "$(kubectl config get-clusters | tail -n +2 | fzf)"
}
kport-forward() {
    local service
    local port
    declare -A service_info
    typeset -A socket_cat_services=(
        "redis_powerful" "powerful Redis instance"
        "rabbitmq" "messaging broker instance"
        "opensearch" "search engine instance"
    )
    
    service_info[redis]="6379"
    service_info[rabbitmq]="15672"
    service_info[opensearch]="9200"
    
    service="$(printf '%s\n' ${(k)service_info} | fzf)" || return
    port="${service_info[$service]}"
    pod_name="$(kubectl get pods | awk '{print $1}' | fzf)"
    
    preview=$(for k v in ${(kv)socket_cat_services}; do echo " $k) echo \"$v\" ;;"; done | tr '\n' ' ')
    preview="case {1} in $preview esac"
    socket_cat=$(printf '%s\n' ${(k)socket_cat_services} | fzf --preview "$preview" --preview-window=right:30%) || exit 1
    
    case "$socket_cat" in
        "redis_powerful")
            echo "socat TCP-LISTEN:6379,fork TCP:dj-prod-redis-new.p62sxg.ng.0001.euc1.cache.amazonaws.com:6379"  | wl-copy
        ;;
        "rabbitmq")
            echo "rabbitmq:Wih78dbt7JchTC7YDkbvk6HSw3lMH6dGciw" | wl-copy
            echo "socat TCP-LISTEN:15672,fork TCP:b-f72a2325-35c4-4bb2-bcd7-f96229419ba5.mq.eu-central-1.amazonaws.com:443"  | wl-copy
        ;;
        "opensearch")
            echo "38DAnb8bW9a3:8*lBW$4>t!hWqTN)@Z70" | wl-copy
            echo "socat TCP-LISTEN:9200,fork TCP:vpc-core-opensearch-domain-e22bsgkv6gkf5ce3emfvb3kqde.eu-central-1.es.amazonaws.com:443" | wl-copy
        ;;
    esac
    
    kubectl port-forward "$pod_name" "$port:$port"
}
