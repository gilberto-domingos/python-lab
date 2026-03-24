git() {
    if [[ "$1" == "add" && "$2" == "." ]]; then
        python3 ~/.scripts/random_number.py
    else
        command git "$@"
    fi
}
