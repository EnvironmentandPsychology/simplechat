import json
import urllib.request

def lambda_handler(event, context):
    # リクエストボディをパース
    body = json.loads(event.get('body', '{}'))
    message = body.get('message', '')

    # Colab で立ち上げた FastAPI サーバーの公開URL
    url = "https://0ea2-35-185-248-34.ngrok-free.app"

    # urllib で POST
    req = urllib.request.Request(
        url,
        data=json.dumps({"message": message}).encode('utf-8'),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as res:
        api_res = json.loads(res.read().decode('utf-8'))

    assistant_response = api_res.get("response", "")

    # Lambda レスポンス返却
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "success": True,
            "response": assistant_response
        })
    }
