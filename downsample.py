import audioop
import wave

converted_file_path = 'audio_files/new.wav'
file_path = 'audio_files/financial_accounting.wav'

inrate = 44100
outrate = 16000
inchannels = 1
outchannels = 1

w = wave.open(file_path)
n_frames = w.getnframes()
data = w.readframes(n_frames)

converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)

w_rite = wave.open(converted_file_path, 'w')

w_rite.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
w_rite.writeframes(converted[0])
