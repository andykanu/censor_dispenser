# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#function to remove specific string
def remove_phrase(source_text, phrase_to_redact):
    source_text_new = source_text.replace(phrase_to_redact, "***")
    return source_text_new
#if many strings passed in list, remove each one by calling 'remove phrase' function
def remove_many_phrases(source_text, phrases_to_redact):
    #apply variable to source text 
    edited_phrase = source_text
    #create title case version of the phrases to redact
    lst_title_case = [phrase.title() for phrase in phrases_to_redact]
    # remove phrases as passed through in lower case
    for phrase in phrases_to_redact:
        edited_phrase = remove_phrase(edited_phrase, phrase)
    #remove phrases passed through in title case
    for phrase in lst_title_case:
        edited_phrase = remove_phrase(edited_phrase, phrase) 
    #return edited email   
    return edited_phrase
#declare terms for editing
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

#third function - removing negative words if repeated
def remove_many_negative_phrases(source_text, phrases_to_redact, negative_words):
    #remove phrases as per proprietary terms by calling above function
    string_for_negative = remove_many_phrases(source_text, proprietary_terms)
    
    # count no. of negative words used, and if >2 replace negative word with **
    neg_count = 0
    lst_for_negative_check = string_for_negative.split(' ')
    for i in range(len(lst_for_negative_check)):
        if lst_for_negative_check[i] in negative_words:
            neg_count += 1
            if neg_count > 2:
                break
    string_for_negative = ' '.join(lst_for_negative_check[i+1:])
    pre_string = ' '.join(lst_for_negative_check[:i])
    string_for_negative = remove_many_phrases(string_for_negative, negative_words)
    return pre_string + ' ' + string_for_negative
    
#list of negative words
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#function four - censor surrounding words
def remove_surrounding_phrases(source_text, phrases_to_remove, negative_words):
    #remove phrases in list, replacing with "***"
    interim_text = remove_many_phrases(source_text, phrases_to_remove)
    interim_text = remove_many_phrases(interim_text, negative_words)
    #split source text into list
    interim_list = interim_text.split(' ')
    #check for censored words and censor words before and after
    for i in range(len(interim_list) -1):
        if interim_list[i+1] == "***":
            interim_list[i] = "****"
        if interim_list[i-1] == "***":
            interim_list[i] = "****"
    #join string, censor & return
    final_text = ' '.join(interim_list)
    final_text = remove_phrase(final_text, "****")
    return final_text

print(remove_surrounding_phrases(email_four, proprietary_terms, negative_words))