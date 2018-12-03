class AdvStyleConfig():

    MODE = "train"

    BATCH_SIZE = 64
    EPOCHS = 100
    LATENT_DIM = 256
    LATENT_DIM_DECODER = 256
    NUM_SAMPLES = 700
    MAX_SEQUENCE_LENGTH = 100
    MAX_NUM_WORDS = 20000
    EMBEDDING_DIM = 100    

    ADVERSARIAL = True

    STYLE_TRANSFER = True
    STYLE_NUM = 2
    STYLE_DIM = 256
    
    PREDICTION_BATCH_SIZE = 32
    PREDICT_SAMPLE_SIZE = 5

    ENCODER_INPUT_MAX_LEN = 60
    DECODER_INPUT_MAX_LEN = 60

    def __repr__(self):
        arttribute = vars(self)
        arttribute = {k:v for k,v in arttribute.items() if not k.startswith("__")}
        return str(arttribute) 