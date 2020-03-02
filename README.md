# Deep-Drop
The dropper implementation was proof-of-concept, and a lot of the inital code came from training code during research. This branch aims to simplify the project and expose model predictions through a REST API. (The old branch could get a makeover at some point using this API). 

## Process List Data
The process list parsing was built around a specific inital access payload, as a result the parsing wasn't flexible. The API no longer makes an assumption about the process list structure and only cares about the features - process_count, user_count, and process_user_ratio.

**Example cURL request**

```curl
curl http://localhost/api/v1/predict?process_count=345&user_count=2&process_user_ratio=172.5
{'decision_tree': 0.0}
```

## Predictions
Returning scores for both models was somewhat arbitrary. During training and evaluation you would deploy the model that is the most accurate, and re-evaluate on a periodic basis as more data was collected.

## Training
Training code has not changed.

## TODO