from stanford_tokenizer import *
from redundancy import *
from coverage import ext_fragments
from uniformity import uniformity
import json
import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from tfidf import stopwords_output


def intrinsic_characteristic(source_doc, ref_summ, stopw):
    result_dict = {}
    # Tokens and Sents
    source_tokens = clean_and_tokenize(source_doc)
    summ_tokens = clean_and_tokenize(ref_summ)
    source_sents = sent_tokenizer(source_doc)
    summ_sents = sent_tokenizer(ref_summ)
    result_dict['source_tokens'] = len(source_tokens)
    result_dict['source_sents'] = len(source_sents)
    result_dict['summ_tokens'] = len(summ_tokens)
    result_dict['summ_sents'] = len(summ_sents)

    # Compression Ratio
    result_dict['compress_tokens'] = len(source_tokens)/len(summ_tokens)
    result_dict['compress_sents'] = len(source_sents)/len(summ_sents)

    # Redundancy
    result_dict['redundancy'] = redundancy(summ_sents)

    # Coverage and Density
    cov_and_den = ext_fragments(source_doc, ref_summ)
    result_dict['coverage'] = cov_and_den['coverage']
    result_dict['density'] = cov_and_den['density']

    # Uniformity
    try:
        result_dict['uniformity'] = uniformity(source_doc, ref_summ,'tenth',stopw)
    except:
        result_dict['uniformity'] = 'Error'
    return result_dict


if __name__ == "__main__":
    # SumSurvey test set
    test_source_path = 'SumSurvey/test.source'
    test_target_path = 'SumSurvey/test.target'
    f1 = open(test_source_path, 'r')
    test_source = f1.readlines()
    f1.close()
    f2 = open(test_target_path, 'r')
    test_target = f2.readlines()
    f2.close()

    dataset_size = len(test_source)

    compress_sents_all = 0
    compress_tokens_all = 0
    coverage_all = 0
    density_all = 0
    redundancy_all = 0
    err_redundancy = 0
    uniformity_all = 0
    err_uniformity = 0

    for i in range(dataset_size):
        print('processing the ' + str(i) + 'th item...')
        src = test_source[i]
        summ = test_target[i]

        import spacy
        nlp = spacy.load('en_core_web_sm')
        stopwords = set(list(nlp.Defaults.stop_words) + ['et', 'al'])  # which is far too common in a paper

        test = intrinsic_characteristic(src, summ, stopwords)

        # pprint.pprint(test)

        compress_sents_all = compress_sents_all + test['compress_sents']
        compress_tokens_all = compress_tokens_all + test['compress_tokens']
        coverage_all = coverage_all + test['coverage']
        density_all = density_all + test['density']
        if test['redundancy'] == 'Error':
            err_redundancy = err_redundancy + 1
        else:
            redundancy_all = redundancy_all + test['redundancy']
        if test['uniformity'] == 'Error':
            err_uniformity = err_uniformity + 1
        else:
            uniformity_all = uniformity_all + test['uniformity']

    print('compress_sents: ' + str(compress_sents_all / dataset_size))
    print('compress_tokens: ' + str(compress_tokens_all / dataset_size))
    print('coverage: ' + str(coverage_all / dataset_size))
    print('density: ' + str(density_all / dataset_size))
    print('redundancy: ' + str(redundancy_all / (dataset_size-err_redundancy)))
    print('uniformity: ' + str(uniformity_all / (dataset_size-err_uniformity)))
