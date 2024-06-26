import streamlit as st


def read_data(file_path):
    with open(file_path, 'r') as f:
        data = f.readlines()
    return data


def preprocessing(words):
    return sorted(set([word.strip().lower() for word in words]))


def levenshtein_distance(word_input, target):
    rows = len(word_input) + 1
    columns = len(target) + 1
    
    # initial matrix
    matrix = [[0]*columns for _ in range(rows)]
    for i in range(rows): 
        matrix[i][0] = i
    for j in range(columns):
        matrix[0][j] = j

    for i in range(rows): 
        for j in range(columns):
            if word_input[i-1] == target[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j] + 1,
                                matrix[i][j-1] + 1, 
                                matrix[i-1][j-1] + 1)
    return matrix[-1][-1]


def main():
    vocabs = read_data(
        'F:\\AIO2024\\AIO2024-Project\\module1\\streamlit\\data\\vocab.txt')
    vocabs = preprocessing(vocabs)

    st.title('Word Correction using Levenshtein Distance')
    word = st.text_input('Word: ')

    if st.button('Compute'):
        levenshtein_distance_dict = {}
        for vocab in vocabs: 
            levenshtein_distance_dict[vocab] = levenshtein_distance(word, vocab)
        sorted_distances_dict = dict(sorted(levenshtein_distance_dict.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances_dict.keys())[0]
        st.write('Correct word: ', correct_word)
    
        col1, col2 = st.columns(2)
        with col1: 
            st.write('Vocabulary:', vocabs)
        with col2: 
            st.write('Distance:', sorted_distances_dict)


if __name__ == '__main__':
    main()
