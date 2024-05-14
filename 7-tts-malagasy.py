from transformers import VitsModel, AutoTokenizer
import torch
import scipy


model = VitsModel.from_pretrained("facebook/mms-tts-mlg")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-mlg")

text = "Salama"
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    output = model(**inputs).waveform

# scipy.io.wavfile.write("techno.wav", rate=model.config.sampling_rate, data=output)
