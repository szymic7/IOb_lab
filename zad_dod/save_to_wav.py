import wave

def save_raw_pcm_to_wav(input_path, output_path, channels=1, sample_width_bytes=2, frame_rate=44100):
    with open(input_path, 'rb') as f:
        pcm_data = f.read()

    # Write to WAV file
    with wave.open(output_path, 'wb') as wav_file:
        wav_file.setnchannels(channels)  # 1 for mono, 2 for stereo
        wav_file.setsampwidth(sample_width_bytes)  # 2 bytes = 16-bit audio
        wav_file.setframerate(frame_rate)  # 44100 samples per second
        wav_file.writeframes(pcm_data)


save_raw_pcm_to_wav('appended_data.bin', 'message.wav')
