from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

client = OpenAI()

def get_embedding(text):
	response = client.embeddings.create(
		input= text,
		model='text-embedding-3-small'
	)
	return response.data[0].embedding


def compare_embedding(text1, text2):
	embedding1 = get_embedding(text1)
	embedding2 = get_embedding(text2)

	embedding1_array = np.array([embedding1])
	embedding2_array = np.array([embedding2])
    
    # コサイン類似度を計算
	similarity = cosine_similarity(embedding1_array, embedding2_array)[0][0]
	return similarity

#text_sample1 = "今日はいい天気ですね。"
#text_sample2 = "今日の天気は晴れで、気持ちがいいです。"

text_sample1 = "今日はいい天気ですね。"
text_sample2 = "そのエビデンスは医学的に間違っています。"

similarity_score = compare_embedding(text_sample1, text_sample2)
print("similarity score is {:.4f}".format(similarity_score))
