import re
import requests 

urls_string = """https://machinelearningmastery.com/the-transformer-model/
https://gekko.readthedocs.io/en/latest/
https://arxiv.org/pdf/1412.3555v1.pdf
https://kindsonthegenius.com/blog/understanding-clustering-k-means-in-machine-learning-unsupervised-learning/
http://www.fit.vutbr.cz/research/groups/speech/publi/2010/mikolov_interspeech2010_IS100722.pdf
https://www.youtube.com/watch?v=QuELiw8tbx8&list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6&t=1190s&ab_channel=StanfordUniversitySchoolofEngineering
https://towardsdatascience.com/multilayer-perceptron-explained-with-a-real-life-example-and-python-code-sentiment-analysis-cb408ee93141
https://www.youtube.com/watch?v=fZXgIgDXtvc&ab_channel=JeffreyChasnov
https://medium.com/ai%C2%B3-theory-practice-business/what-is-pre-training-in-nlp-introducing-5-key-technologies-455c54933054
https://medium.com/geekculture/how-to-deal-with-missing-values-in-machine-learning-98e47f025b9c
https://medium.com/pipeline-a-data-engineering-resource/creating-the-dashboard-that-got-me-a-data-analyst-job-offer-de3f0d6b1771
https://sysflow.readthedocs.io/en/latest/
https://towardsdatascience.com/outlier-detection-with-isolation-forest-3d190448d45e
https://towardsdatascience.com/ridge-lasso-and-elasticnet-regression-b1f9c00ea3a3
https://medium.com/pipeline-a-data-engineering-resource/3-data-science-projects-that-got-me-12-interviews-and-1-that-got-me-in-trouble-f376682b4e21
https://www.researchgate.net/publication/339505894_Predicting_Days_on_Market_to_Optimize_Real_Estate_Sales_Strategy
https://developers.google.com/calendar/api/quickstart/python
https://towardsdatascience.com/acing-machine-learning-interviews-aa73d6d7b07b
https://medium.com/wwblog/reducible-vs-irreducible-error-e469036969fa
https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/
https://jaan.io/what-is-variational-autoencoder-vae-tutorial/
https://hbr.org/2018/07/collaborative-intelligence-humans-and-ai-are-joining-forces
https://paperswithcode.com/paper/neighborhood-enlargement-in-graph-neural
https://towardsdatascience.com/graph-neural-networks-in-python-c310c7c18c83
https://meatba11.medium.com/keras-loading-and-processing-images-in-batches-1cff1b0f4aa4
https://vijayabhaskar96.medium.com/tutorial-on-keras-flow-from-dataframe-1fd4493d237c
https://vijayabhaskar96.medium.com/tutorial-image-classification-with-keras-flow-from-directory-and-generators-95f75ebe5720
https://towardsdatascience.com/auto-encoder-what-is-it-and-what-is-it-used-for-part-1-3e5c6f017726
https://www.youtube.com/watch?v=6gLeplbqtqg&ab_channel=freeCodeCamp.org
https://towardsdatascience.com/hands-on-introduction-to-reinforcement-learning-in-python-da07f7aaca88"""

def text_to_urls(urls_str, version:str):
    urls_list = urls_str.splitlines()
    urls_list_ed = [url for url in urls_list if re.match(r'^https?://', url)]
    urls_list_diff = list(set(urls_list) - set(urls_list_ed))
    if version.lower() == "original":
        return urls_list
    elif version.lower() == "edited":
        return urls_list_ed
    elif version.lower() == "invalid":
        return urls_list_diff

def validate_urls(urls_list):
    
    urls_list = [url for url in urls_list if re.match(r'^https?://', url)]
    urls_list = [url for url in urls_list if not re.search(r"youtube", url)]
    urls_status = {url:requests.get(url).status_code for url in urls_list}
    valid_urls = {url:status_code for (url, status_code) in urls_status.items() if status_code == 200}
    inv_urls = {url:status_code for (url, status_code) in urls_status.items() if status_code != 200}
    all_urls = {'valid':valid_urls, 'invalid':inv_urls}
    return all_urls

# urls_list = text_to_urls(urls_string, "edited")
# valid_urls_list = validate_urls(url_list= urls_list)
# print(valid_urls_list["invalid"])

