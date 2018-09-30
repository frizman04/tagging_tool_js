#!/usr/bin/python

import argparse
import json
import pandas as pd


def main(args):
    file_name = args.input
    file_out = args.output

    df = pd.read_table(file_name)
    df = df.drop(labels=['GOLDEN:output','HINT:text'],axis=1)
    df = df.dropna()

    data = []
    for context in df['INPUT:context'].unique() :
        data_item = dict()
        data_item['context'] = context
        data_item['qas'] = []

        for question in df[df['INPUT:context'] == context]['INPUT:question'].unique() :
            quest_item = dict()
            quest_item['question'] = question
            quest_item['answers'] = []
            
            for answers in df[(df['INPUT:context'] == context) & (df['INPUT:question'] == question)]['OUTPUT:output'] :
                answers_item = dict()
                index_arr = answers.replace('"','').replace('\\','').replace('[','').replace(']','').split(',')
                index_arr = [int(indx) for indx in index_arr]
                answer_start = index_arr[0]
                answers_item['answer_start'] = answer_start
                answers_item['text'] = " ".join(context.split(' ')[index_arr[0]:index_arr[1]+1])
                
                quest_item['answers'].append(answers_item)
            data_item['qas'].append(quest_item)
        data.append(data_item)


    json_txt = json.dumps(data,ensure_ascii=False)
    with open(file_out,'w',encoding='utf-8') as f :
        f.write(json_txt)
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file tsv")
    parser.add_argument("-o", "--output", help="output file in squad format")
    args = parser.parse_args()

    main(args)
