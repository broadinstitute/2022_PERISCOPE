from io import BytesIO
from matplotlib import image as mpimg
import boto3
import pandas as pd

s3_client = boto3.client("s3",config=Config(signature_version=UNSIGNED))
bucket_name = "cellpainting-gallery"

def read_csv_gzip(path):

    data = s3_client.get_object(
        Bucket=bucket_name, Key=path
    )  
    df_p_s = pd.read_csv(data["Body"], compression="gzip")

    return df_p_s


def read_image(path):

    response = s3_client.get_object(Bucket=bucket_name, Key=path)
    format_ext = path.split(".")[-1]
    image = mpimg.imread(BytesIO(response["Body"].read()), format=format_ext)

    return image