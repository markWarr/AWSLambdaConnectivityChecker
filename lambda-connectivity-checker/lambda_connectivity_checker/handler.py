import requests

def lambda_handler(event, context):
  try:
    url = event.get("url")
    print_output = ""    
    response = requests.get(url, timeout=2)
    print(f"typeof RESPONSE: {type(response)}")    
    print(f"RESPONSE: {response}")
    if response.ok:   # alternatively you can use response.status_code == 200
         print_output = "Success - URL is accessible."
    else:
        print_output = f"Failure - URL is accessible but error returned. Response code : {response.status_code}"
    
  except Exception as e:
    print_output = f"Failure - Unknown error occurred: {e}."
  
    return {
        'statusCode': 200,
        'body': print_output
    }