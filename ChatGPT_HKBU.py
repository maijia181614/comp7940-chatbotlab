import configparser
import requests
import os


class HKBU_ChatGPT():

    def submit(self, message):
        conversation = [{"role": "user", "content": message}]
        url = (os.environ["chatgpt_basic_url"]) + "/deployments/" + (
        os.environ["chatgpt_model_name"]) + "/chat/completions/?api-version=" + (
              os.environ["chatgpt_api_version"])
        headers = {'Content-Type': 'application/json', 'api-key': (os.environ["chatgpt_access_token"])}
        payload = {'messages': conversation}
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return 'Error:', response


if __name__ == '__main__':
    ChatGPT_test = HKBU_ChatGPT()

    while True:
        user_input = input("Typing anything to ChatGPT:\t")
        response = ChatGPT_test.submit(user_input)
        print(response)

