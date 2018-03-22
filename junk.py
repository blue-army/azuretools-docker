import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess


def run_sample():
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='planck', account_key='dXskxcS8enXEWXbk2K4dAfh5ktJkF/LHx9er5I2UdW44jKqT/AYWBqI7M2IzkoDUCvmbzHRWdV3nCXUmUn1WPQ==')

        # Create a container called 'quickstartblobs'.
        container_name ='nutanix-pipeline'
        
        # List the blobs in the container
        print("\nList blobs in the container")
        generator = block_blob_service.list_blobs(container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)
    except Exception as e:
        print(e)

# Main method.
if __name__ == '__main__':
    run_sample()