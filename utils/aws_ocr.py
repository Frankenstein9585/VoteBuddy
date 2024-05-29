import boto3


def aws_textract_local(image_path):
    detected_text = ''
    client = boto3.client('textract')

    with open(image_path, 'rb') as document:
        image_bytes = bytearray(document.read())

    response = client.detect_document_text(Document={'Bytes': image_bytes})

    # for item in response['Blocks']:
    #     print(item)

    # print(response['Blocks'])

    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            detected_text += item['Text'] + '\n'

    return detected_text.casefold()


# # Example usage
# print(aws_textract_local('AU202000348.png'))
