# Tagging tool (QA) for toloka.yandex.ru on js
Lightweight tool for sentence tagging (i.e. QA markup) on JavaScript


In Toloka you must create 2 input variables:
* context: string - space separated words to show
* question: array_string - array of question for QA

and 1 output variable:
* output: [int] - arrays of taggs represented as tuple [first_word, last_word] 

Toloka settings of input :
{
  "context": {
    "type": "string",
    "hidden": false,
    "required": true
  },
  "question": {
    "type": "array_string",
    "hidden": false,
    "required": true
  }
}

Toloka settings of output :
{
  "output": {
    "type": "array_json",
    "required": true
  }
}
