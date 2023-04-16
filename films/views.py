from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Загрузка данных фильмов
movies = Movie.objects.all()

# Создание векторного представления фильмов
vectorizer = CountVectorizer()
movie_titles = [movie.title for movie in movies]
movie_vectors = vectorizer.fit_transform(movie_titles)

# Вычисление матрицы сходства косинусной между фильмами
similarity_matrix = cosine_similarity(movie_vectors)

# Функция для получения рекомендаций для фильма
def get_recommendations(movie_title):
    movie_index = movie_titles.index(movie_title)
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similar_movies = [movies[score[0]] for score in similarity_scores[1:6]]
    return similar_movies
