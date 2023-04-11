#pip install --upgrade tensorflow_hub
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import bert.tokenization as tokenization
import pandas as pd

module_url = "https://tfhub.dev/tensorflow/bert_en_uncased_L-24_H-1024_A-16/1"
bert_layer = hub.KerasLayer(module_url, trainable=False)
train=pd.read_csv(r"C:\Users\peter\OneDrive\Documents\GitHub\Privacy-Law-Technology-Project\train.csv")

print(train.head(3))
# vocab_file = bert_layer.resolved_object.vocab_file.asset_path.numpy()
# do_lower_case = bert_layer.resolved_object.do_lower_case.numpy()
# tokenizer = tokenization.FullTokenizer(vocab_file, do_lower_case)

# def bert_encode(texts, tokenizer, max_len=512):
#     all_tokens = []
#     all_masks = []
#     all_segments = []
    
#     for text in texts:
#         text = tokenizer.tokenize(text)
            
#         text = text[:max_len-2]
#         input_sequence = ["[CLS]"] + text + ["[SEP]"]
#         pad_len = max_len - len(input_sequence)
        
#         tokens = tokenizer.convert_tokens_to_ids(input_sequence) + [0] * pad_len
#         pad_masks = [1] * len(input_sequence) + [0] * pad_len
#         segment_ids = [0] * max_len
        
#         all_tokens.append(tokens)
#         all_masks.append(pad_masks)
#         all_segments.append(segment_ids)
    
#     return np.array(all_tokens), np.array(all_masks), np.array(all_segments)

# def build_model(bert_layer, max_len=512):
#     input_word_ids = tf.keras.Input(shape=(max_len,), dtype=tf.int32, name="input_word_ids")
#     input_mask = tf.keras.Input(shape=(max_len,), dtype=tf.int32, name="input_mask")
#     segment_ids = tf.keras.Input(shape=(max_len,), dtype=tf.int32, name="segment_ids")

#     pooled_output, sequence_output = bert_layer([input_word_ids, input_mask, segment_ids])
#     clf_output = sequence_output[:, 0, :]
#     net = tf.keras.layers.Dense(64, activation='relu')(clf_output)
#     net = tf.keras.layers.Dropout(0.2)(net)
#     net = tf.keras.layers.Dense(32, activation='relu')(net)
#     net = tf.keras.layers.Dropout(0.2)(net)
#     out = tf.keras.layers.Dense(5, activation='softmax')(net)
    
#     model = tf.keras.models.Model(inputs=[input_word_ids, input_mask, segment_ids], outputs=out)
#     model.compile(tf.keras.optimizers.Adam(lr=1e-5), loss='categorical_crossentropy', metrics=['accuracy'])
    
#     return model
# print(train.head(3))
# # max_len = 150
# # train_input = bert_encode(train.Review.values, tokenizer, max_len=max_len)
# # #test_input = bert_encode(test.Review.values, tokenizer, max_len=max_len)
# # train_labels = tf.onclick="parent.postMessage({'referent':'.tensorflow.keras'}, '*')">tf.keras.utils.to_categorical(train.label.values, num_classes=8)
