import boto3

s3 = boto3.client("s3")

s3.dowload_file(
    Bucket = "meet-there-demo", Key = "document.csv", Filename = "data/"
)


def generate_presigned_url(file_key):
    client = boto3.client('s3')
    presigned_url = client.generate_presigned_url('get_object',
                                                  Params = {'Bucket': "meet-there-demo",
                                                            'Key': file_key})
    return presigned_url
