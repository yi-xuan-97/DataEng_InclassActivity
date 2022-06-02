from google.cloud import storage
import zlib
import json
from base64 import b64encode, b64decode
import base64

def list_buckets():
    """Lists all buckets."""

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

def compress():
    with open('testsample.json') as bc:
        data = json.load(bc)

    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)

    f = open('outfile.txt', 'w')
    f.write(compressed_data)
    f.close()


list_buckets()
compress()
#upload_blob("in-class-week9","/home/yixuanfeng/examples/clients/cloud/python/sample.json","week9")
