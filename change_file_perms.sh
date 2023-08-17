def change_new_file_perms():
    while True; do
        inotifywait -e create -e moved_to -e moved_from -m /home/mwdevops/json/full |
        while read path action file; do
            if [ "$action" == "CREATE" ] || [ "$action" == "MOVED_TO" ]; then
            chmod +w "$path/$file"
            fi
        done 
    done