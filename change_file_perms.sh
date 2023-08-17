def change_new_file_perms():
    while True; do
        inotifywait -e create -m /home/mwdevops/json/full |
        while read path action file; do
            chmod +w "$path/$file"
        done 
    done