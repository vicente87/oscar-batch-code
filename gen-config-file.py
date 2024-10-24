import json

# Define the configuration data
config_data = {
    "MinIO": {
        "url": "minio.gracious-varahamihira6.im.grycap.net",
        "access_key": "63710d5ce8f5cd44b91f5152e80ab3f1a144c0760b1773af2dfa6160ad8a368c@egi.eu",
        "secret_key": "UfNn5T98drtJVg"
    },
    "bucket": {
        "name": "fish-detector",
        "folder_prefix": "input/"
    },
    "output": {
        "file": "index.txt"
    },
    "oscar_cluster": {
        "url": "inference-walton.cloud.imagine-ai.eu",
        "auth_basic": {
            "username": "",
            "password": ""
        },
        "auth_token": { "token":"eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQVVlPaXJBM1ktZF9kR3BkajRpSkRIdzR6SGE4SVktYmhaZGFFajByamJVIn0.eyJleHAiOjE3Mjk2NzAzMTMsImlhdCI6MTcyOTY2NjcxMywiYXV0aF90aW1lIjoxNzI5NjY2NjU4LCJqdGkiOiJmZGQ0ODllNy0xYWE5LTQ1ZWEtYTBjNy05MjdlMmViZDgwMzUiLCJpc3MiOiJodHRwczovL2FhaS5lZ2kuZXUvYXV0aC9yZWFsbXMvZWdpIiwic3ViIjoiNjM3MTBkNWNlOGY1Y2Q0NGI5MWY1MTUyZTgwYWIzZjFhMTQ0YzA3NjBiMTc3M2FmMmRmYTYxNjBhZDhhMzY4Y0BlZ2kuZXUiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0b2tlbi1wb3J0YWwiLCJub25jZSI6IjRjNTg5YWQyMWQwYmQ1YTM5NzVlODIyMWFkYWQwY2Y1Iiwic2Vzc2lvbl9zdGF0ZSI6IjIyNzdjZDRlLWYxM2EtNDFjMi1iOWZjLTM1NTA5OTQyMWQzZCIsInNjb3BlIjoib3BlbmlkIGVkdXBlcnNvbl9lbnRpdGxlbWVudCB2b3BlcnNvbl9pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiMjI3N2NkNGUtZjEzYS00MWMyLWI5ZmMtMzU1MDk5NDIxZDNkIiwidm9wZXJzb25faWQiOiI2MzcxMGQ1Y2U4ZjVjZDQ0YjkxZjUxNTJlODBhYjNmMWExNDRjMDc2MGIxNzczYWYyZGZhNjE2MGFkOGEzNjhjQGVnaS5ldSIsImF1dGhlbnRpY2F0aW5nX2F1dGhvcml0eSI6Imh0dHBzOi8vd3d3LnJlZGlyaXMuZXMvc2lyL3VwdmlkcCJ9.Vu0SU-aD47ASAjgeKXEZjvFWfo4T7-ii7iqONl7BVW9juvoN5TRSEHg4FTmDcvravYT_0D6Y7gyhrVBNib0EpF7KIhllokwQHgz7DelTTV5DS4c88jP_ynappzjw5CvzIbV56bM3sChCtVFou2E8CbP1nu4-FL5nCNX7AeKT-hGwttFZh1f0JZEK9jtytm0EBancBiP4kKEM3aW2N44HlxzrvstkH1_SV0nOm8IT_BhM-niw6NpnSQ3f5t_YOuLAH5r4I_lZLKxIn9RoNxc6WziEqhBUozL6xIILF1_ICOY6-gjh0i1oAR2vJnrIi1ShS84H3EBo8DhgHMiJe7L2fA"
        }
    },
    "service": {
        "name": "fish-detector"
    }
}

# Create the Configuration File.
with open('config-walton.json', 'w') as config_file:
    json.dump(config_data, config_file, indent=4)

print("Configuration file 'config.json' created.")