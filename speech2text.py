from deepspeech import Model
import wave
import numpy as np

# STT Model
model_file_path = 'models/deepspeech-0.9.1-models.pbmm'
scorer_file_path = 'models/deepspeech-0.9.1-models.scorer'

lm_alpha = 0.75
lm_beta = 1.85
beam_width = 500

model = Model(model_file_path)

model.enableExternalScorer(scorer_file_path)
model.setScorerAlphaBeta(lm_alpha, lm_beta)
model.setBeamWidth(beam_width)

# Batch API
filename = 'audio_files/financial_accounting.wav'

w = wave.open(filename, 'r')
rate = w.getframerate()
frames = w.getnframes()
buffer = w.readframes(frames)
print(rate)
print(model.sampleRate())

data16 = np.frombuffer(buffer, dtype=np.int16)

# Run model
text = model.stt(data16)

# Save text