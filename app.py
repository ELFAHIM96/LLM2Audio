from elevenlabs.client import ElevenLabs
from elevenlabs import play
from elevenlabs import stream

from langchain_community.llms import Ollama 


cached_llm = Ollama(model = "llama3")

client = ElevenLabs()

""" audio = client.generate(
    text = "Hi how are you doing ",
    voice = "Rachel",
    model = "eleven_multilingual_v2"

)
play(audio) """

query = "what day comes after monday ?"
audio_stream = client.generate(text = "you asked " + query, stream=True)
stream(audio_stream)
response = cached_llm.invoke("what day comes after monday ?")
print(response)
response = client.generate(text = response, stream=True)
stream(response)