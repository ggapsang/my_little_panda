class MyTxt :
    default_values = {
        'split_by' : " "
    }

    def __init__(self, file_name, split_by = None) :
        self.file_name = file_name
        self.split_by = split_by if split_by else MyTxt.default_values['split_by']

    # 텍스트를 특정 구분자 단위로 분리하고(default 구분자는 공백), 각 단어들이 얼마만큼 사용됬는지를 딕셔너리로 반환함
    def get_dict_freq_word(self) :
        file_name = self.file_name
        working_file = open(file_name, 'r')
        split_by = self.split_by


        dict_counting_words = {}
        for line in working_file.readlines() :
            line = line.strip() #불필요한 개행문자의 제거
            lst_words = line.split(split_by)
            for word in lst_words :
                #word = word.strip("=")
                if word not in dict_counting_words :
                    dict_counting_words[word] = 1
                else :
                    dict_counting_words[word] += 1
        
        working_file.close()

        r_dict_counting_words = {v:k for (k, v) in dict_counting_words.items()}
        dict_counting_words = {k:v for (k, v) in sorted(r_dict_counting_words.item())}

        return dict_counting_words

    # 텍스트 파일에 특정 단어가 얼마나 많이 쓰였는지를 확인함
    def get_count_freq_word(self, find_word) :
        file_name = self.file_name
        working_file = open(file_name, 'r')
        split_by = self.split_by

        count_i = 0
        for line in working_file.readlines() :
            line = line.strip()
            lst_words = line.split(split_by)
            for word in lst_words :
                #word = word.strip("=")
                if find_word in word :
                    count_i +=1
                else :
                    continue
        
        working_file.close()

        return count_i

    # split_by로 1차로 구분하고, 2차로 또 다른 구분자로 구분하여 빈도수 분석함
    def get_dict_freq_split_twice(self, split_by_2) :
        file_name = self.file_name
        working_file = open(file_name, 'r')
        split_by = self.split_by

        dict_counting_words = {}
        for line in working_file.readlines() :
            line = line.strip()
            lst_word = line.split(split_by)
            for word in lst_word :
                if split_by_2 in word :
                    lst_words_split_by_2 = word.split(split_by_2)
                    for w in lst_words_split_by_2 :
                        if w not in dict_counting_words :
                            dict_counting_words[w] = 1
                        else :
                            dict_counting_words[w] += 1
                else :
                    if word not in dict_counting_words :
                        dict_counting_words[word] = 1
                    else :
                        dict_counting_words[word] +=1
        
        working_file.close()

        r_dict_counting_words = {v:k for (k, v) in dict_counting_words.items()}
        dict_counting_words = {k:v for (k, v) in sorted(r_dict_counting_words.item())}

        return dict_counting_words
