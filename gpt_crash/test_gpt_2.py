from g4f.client import Client

client = Client()
response = client.images.generate(
    model="flux",
    prompt="Valentine's Day with Volleyball Theme, boy and girl"
           "",
    response_format="url"
)

print(f"Generated image URL: {response.data[0].url}")