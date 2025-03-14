import boto3

def detect_celebrities(bucket_name, image_name):
    rekognition = boto3.client('rekognition')
    
    response = rekognition.recognize_celebrities(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': image_name,
            }
        }
    )
    
    print("Celebridades detectadas:")
    for celebrity in response['CelebrityFaces']:
        print(f"- Nome: {celebrity['Name']}")
        print(f"  Confiança: {celebrity['MatchConfidence']:.2f}%")
        print(f"  URLs: {', '.join([url['Url'] for url in celebrity['Urls']])}")
        print("")
    
    if not response['CelebrityFaces']:
        print("Nenhuma celebridade foi detectada na imagem.")
    return response

if __name__ == "__main__":
    bucket_name = "bucket01"
    image_name = "detectando-celebridades.jpg"

    detect_celebrities(bucket_name, image_name)
