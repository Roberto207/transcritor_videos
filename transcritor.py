import whisper

def transcrever_audio(arquivo_audio):
    model = whisper.load_model("base")  # tiny, base, small, medium, large
    resultado = model.transcribe(arquivo_audio, language='pt')
    return resultado['text']

if __name__ == "__main__":
    caminho_arquivo = 'C:\\Users\\Windows\\Pictures\\videomulherteste1.mp4' #input("Digite o caminho do arquivo de vídeo ou áudio a ser transcrito: ")
    roteiro = transcrever_audio(caminho_arquivo)

    print("\n--- Roteiro transcrito ---\n")
    print(roteiro)
    #print(roteiro)

