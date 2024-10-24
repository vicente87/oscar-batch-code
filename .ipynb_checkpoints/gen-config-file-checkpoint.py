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
        "auth_token": { "token":""
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