import matplotlib.pyplot as plt
import nltk
from nltk.stem.snowball import SnowballStemmer
import sqlite3
import re

#################################
# Regex for providing labels for training set
#################################


def get_job_title():
    """
    Return's job title, company_name, profile_url for each profile in db
    """
    conn = sqlite3.connect('/Users/Rahul/Desktop/Main/Side_projects/linkedin_recommend/db.sqlite3')
    c = conn.cursor()
    c.execute('SELECT job FROM link_rec_alljobtitle')
    y = c.fetchall()
    job_title = [job[0].lower() for job in y]
    c.execute('SELECT loc FROM link_rec_alllocation')
    y = c.fetchall()
    company_name = [i[0].lower() for i in y]
    c.execute('SELECT url FROM link_rec_allparsedprofile')
    y = c.fetchall()
    profile_url = [i[0] for i in y]
    return job_title, company_name, profile_url

job_title, company_name, profile_url = get_job_title()

stopwords = nltk.corpus.stopwords.words('english')  # load the stop words from nltk
stemmer = SnowballStemmer("english")  # stemming


def tokenize_and_stem(text):
    """
    First tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    """
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def filterPick(list, filter, classification):
    """Used for applying the regex search"""
    y = []
    empty = []
    for job in list:
        x = [(job, classification) for l in job for m in (filter(l),) if m]
        if len(x) == 0:
            empty.append(' '.join(job))
        y.append(x)
    return y, empty


def software():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile('(io|softwar|develop|thiel|innovation|websit|web|forward|deploy|develop|fullstack|python|java|agil|programm|applic|autopilot|fellow)').search
    x = filterPick(new_title_list, searchRegex, 'software')
    return x


def engineer():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(mechan|industri|skule|drill|robot|electr)').search
    x = filterPick(new_title_list, searchRegex, 'engineering')
    return x


def research():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(research|lectur)').search
    x = filterPick(new_title_list, searchRegex, 'research')
    return x


def design():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(design)').search
    x = filterPick(new_title_list, searchRegex, 'design')
    return x


def data():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(data|scien|big data|data vi|data analy|machine learning)').search
    x = filterPick(new_title_list, searchRegex, 'data science')
    return x


def product():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(product)').search
    x = filterPick(new_title_list, searchRegex, 'product manager')
    return x


def finance():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(chair|financi|account payabl|record clerk|busi develop|busi|busi analyst|oper|logist|market|busi intellig|digit market|invest|invest bank|capit|capit market|ventur|merger|acquisit|consult|account|privat|equiti)').search
    x = filterPick(new_title_list, searchRegex, 'business and finance')
    return x


def startup():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(co-found|founder|presid|chief|execut|offic|vice-presid|cofound)').search
    x = filterPick(new_title_list, searchRegex, 'startup founder')
    return x


def admin_it(): # admin/hr/coordination/it
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(administr|coordin|repres|ambassador|teach|talent)').search
    x = filterPick(new_title_list, searchRegex, 'admin/coordination/it')
    return x


def crypto():
    new_title_list = [tokenize_and_stem(i) for i in job_title]
    searchRegex = re.compile(
        '(cryptographi|blockchain|crypto|ethereum)').search
    x = filterPick(new_title_list, searchRegex, 'crypto/blockchain')
    return x


def write_to_file(items):
    for i in items:
        if len(i) != 0:
            with open('job_classified', 'a') as f:
                job = ' '.join(i[0][0])
                classification = i[0][1]
                f.write(job + ', ' + classification + '\n')


# if __name__ == '__main__':
#     software, software_empty = software()
#     finance, finance_empty = finance()
#     product, product_empty = product()
#     startup, startup_empty = startup()
#     data, data_empty = data()
#     design, design_empty = design()
#     research, research_empty = research()
#     engineer, engineer_empty = engineer()
#     admin, admin_empty = admin_it()
#     crypto, crypto_empty = crypto()
#
#     write_to_file(software)
#     write_to_file(finance)
#     write_to_file(product)
#     write_to_file(startup)
#     write_to_file(data)
#     write_to_file(design)
#     write_to_file(research)
#     write_to_file(engineer)
#     write_to_file(admin)
#     write_to_file(crypto)

    # empty_list = []
    # empty_list.extend(software_empty)
    # empty_list.extend(finance_empty)
    # empty_list.extend(product_empty)
    # empty_list.extend(startup_empty)
    # empty_list.extend(data_empty)
    # empty_list.extend(design_empty)
    # empty_list.extend(research_empty)
    # empty_list.extend(engineer_empty)
    # empty_list.extend(admin_empty)
    # empty_list.extend(crypto_empty)
    #
    # empty_list = list(set(empty_list))
    # for i in empty_list:
    #     print(i)
    #
    # with open('job_classified', 'a') as f:
    #     for job in empty_list:
    #         f.write(job + '\n')
    # print('Done')



# def get_job_title():
#     conn = sqlite3.connect('/Users/Rahul/Desktop/Main/Side_projects/linkedin_recommend/db.sqlite3')
#     c = conn.cursor()
#     c.execute('SELECT job FROM link_rec_alljobtitle')
#     y = c.fetchall()
#     job_title = [job[0].lower() for job in y]
#     c.execute('SELECT loc FROM link_rec_alllocation')
#     y = c.fetchall()
#     company_name = [i[0].lower() for i in y]
#     c.execute('SELECT url FROM link_rec_allparsedprofile')
#     y = c.fetchall()
#     profile_url = [i[0] for i in y]
#     return job_title, company_name, profile_url
#
# job_title, company_name, profile_url = get_job_title()
#
# stopwords = nltk.corpus.stopwords.words('english')  # load the stop words from nltk
# stemmer = SnowballStemmer("english")  # stemming
#
#
# def tokenize_and_stem(text):
#     # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
#     tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
#     filtered_tokens = []
#     # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
#     for token in tokens:
#         if re.search('[a-zA-Z]', token):
#             filtered_tokens.append(token)
#     stems = [stemmer.stem(t) for t in filtered_tokens]
#     return stems
#
#
# def stem_for_regex(items):
#     x = []
#     for i in items:
#         x.append(tokenize_and_stem(i))
#     return [y for i in x for y in i]
#
#
# def filterPick(list, filter, classification):
#     """Used for applying the regex search"""
#     y = []
#     empty = []
#     for job in list:
#         x = [(job, classification) for l in job for m in (filter(l),) if m]
#         if len(x) == 0:
#             empty.append(' '.join(job))
#         y.append(x)
#     return y, empty
#
#
# def software():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile('(io|softwar|develop|thiel|innovation|websit|web|forward|deploy|develop|fullstack|python|java|agil|programm|applic|autopilot|fellow)').search
#     x = filterPick(new_title_list, searchRegex, 'software')
#     return x
#
#
# def engineer():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(mechan|industri|skule|drill|robot|electr)').search
#     x = filterPick(new_title_list, searchRegex, 'engineering')
#     return x
#
#
# def research():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(research|lectur)').search
#     x = filterPick(new_title_list, searchRegex, 'research')
#     return x
#
#
# def design():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(design)').search
#     x = filterPick(new_title_list, searchRegex, 'design')
#     return x
#
#
# def data():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(data|scien|big data|data vi|data analy|machine learning)').search
#     x = filterPick(new_title_list, searchRegex, 'data science')
#     return x
#
#
# def product():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(product)').search
#     x = filterPick(new_title_list, searchRegex, 'product manager')
#     return x
#
#
# def finance():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(chair|financi|account payabl|record clerk|busi develop|busi|busi analyst|oper|logist|market|busi intellig|digit market|invest|invest bank|capit|capit market|ventur|merger|acquisit|consult|account|privat|equiti)').search
#     x = filterPick(new_title_list, searchRegex, 'business and finance')
#     return x
#
#
# def startup():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(co-found|founder|presid|chief|execut|offic|vice-presid|cofound)').search
#     x = filterPick(new_title_list, searchRegex, 'startup founder')
#     return x
#
#
# def admin_it(): # admin/hr/coordination/it
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(administr|coordin|repres|ambassador|teach|talent)').search
#     x = filterPick(new_title_list, searchRegex, 'admin/coordination/it')
#     return x
#
#
# def crypto():
#     new_title_list = [tokenize_and_stem(i) for i in job_title]
#     searchRegex = re.compile(
#         '(cryptographi|blockchain|crypto|ethereum)').search
#     x = filterPick(new_title_list, searchRegex, 'crypto/blockchain')
#     return x
#
#
# def write_to_file(items):
#     for i in items:
#         if len(i) != 0:
#             with open('job_classified', 'a') as f:
#                 job = ' '.join(i[0][0])
#                 classification = i[0][1]
#                 f.write(job + ', ' + classification + '\n')
#
#
# def count(data):
#     """
#     Return's a dict with key (item) and number of times it appears in list
#     """
#     assert type(data) == list
#     main_di = {}
#     for i in data:
#         if i in main_di:
#             main_di[i] += 1
#         else:
#             main_di[i] = 1
#     return main_di
#
#
# # lines = open('job_classified').readlines()
# # lines = [line.replace('\n', '') for line in lines]
# # classification = []
# # for i in lines:
# #     c = i.split(',')[-1]
# #     classification.append(c)
#
#
# def barGraph(data_count):
#
#     names, count_in = [], []
#     data_count = sorted(data_count.items(), key=operator.itemgetter(1), reverse=True)
#     for i in data_count:
#         names.append(i[0])
#         count_in.append(i[-1])
#
#     plt.rcdefaults()
#     fig, ax = plt.subplots()
#     y_pos = np.arange(len(names))
#     ax.barh(y_pos, count_in, align='center',
#             color='green', ecolor='black')
#     ax.set_yticks(y_pos)
#     ax.set_yticklabels(names)
#     ax.invert_yaxis()  # labels read top-to-bottom
#     ax.set_xlabel('Categories')
#     ax.set_title('# of job titles in each category')
#     plt.show()
#
# # data_count = count(classification)
# # barGraph(data_count)
#
#
# software, software_empty = software()
# finance, finance_empty = finance()
# product, product_empty = product()
# startup, startup_empty = startup()
# data, data_empty = data()
# design, design_empty = design()
# research, research_empty = research()
# engineer, engineer_empty = engineer()
# admin, admin_empty= admin_it()
# crypto, crypto_empty = crypto()

# write_to_file(software)
# write_to_file(finance)
# write_to_file(product)
# write_to_file(startup)
# write_to_file(data)
# write_to_file(design)
# write_to_file(research)
# write_to_file(engineer)
# write_to_file(admin)
# write_to_file(crypto)
#
#
# empty_list = []
# empty_list.extend(software_empty)
# empty_list.extend(finance_empty)
# empty_list.extend(product_empty)
# empty_list.extend(startup_empty)
# empty_list.extend(data_empty)
# empty_list.extend(design_empty)
# empty_list.extend(research_empty)
# empty_list.extend(engineer_empty)
# empty_list.extend(admin_empty)
# empty_list.extend(crypto_empty)
#
# empty_list = list(set(empty_list))
# # for i in empty_list:
# #     print(i)
#
# with open('job_classified', 'a') as f:
#     for job in empty_list:
#         f.write(job + '\n')
#
# print('Done')