## Text Summarization using Hugging Face

### Objective

Creating a text summarizer UI API. Text summarization is the process of creating a shorter version of a document or an article that captures all the important information. It can be formulated as a sequence-to-sequence task and can be either extractive or abstractive. Hugging Face provides several model architectures for summarization, including BART, BigBird-Pegasus, Blenderbot, BlenderbotSmall, Encoder decoder, FairSeq Machine-Translation, GPTSAN-japanese, LED, LongT5, M2M100, Marian, mBART, MT5, MVP, NLLB, NLLB-MOE, Pegasus, PEGASUS-X, PLBart, ProphetNet, SwitchTransformers, T5, UMT5, and XLM-ProphetNet. For this project Pegasus model is choosed and its also acts as tokenizer.

### Packages Used

- transformers
- transformers[sentencepiece]
- datasets
- sacrebleu
- rouge_score
- py7zr
- pandas
- nltk
- tqdm
- pyYAML
- matplotlib
- torch
- notebook
- boto3
- mypy-boto3-s3
- python-box==6.0.2
- ensure==1.0.2
- fastapi==0.78.0
- uvicorn==0.18.3
- jinja2==3.1.2

### Tools Used

- GitHub 
- GutHub actions
- Visual Studio Code
- AZURE
- Google Colab

### Data Description

SAMsum Corpus dataset is used in this project. SAMSum Corpus is a human-annotated dialogue dataset for abstractive summarization. It was introduced by Gliwa et al. in 2019.  The dataset contains 16k online chats with corresponding summaries. The data has splitted into 3 sets and each consists of 3 features ('id', 'dialogue', 'summary').
- train --> 14732
- test --> 819
- validation --> 818

### Model Selection

Pegasus model is used to train the data. Pegasus is a transformer-based model for abstractive summarization. It was proposed by Jingqing Zhang, Yao Zhao, Mohammad Saleh, and Peter J. Liu in 2019. The model is pre-trained jointly on two self-supervised objective functions: 
- Masked Language Modeling (MLM)
- Novel summarization-specific pretraining objective, called Gap Sentence Generation (GSG)