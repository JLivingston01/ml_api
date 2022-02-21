import numpy as np
from sklearn.linear_model import LinearRegression


models = {f'model_{j}': LinearRegression().fit(
    X,
    X@np.random.normal(0,.5,5)
    ) for j,X in zip(range(3),[np.random.normal(0,.5,(100,5)),
                          np.random.normal(0,.5,(100,5)),
                          np.random.normal(0,.5,(100,5))])}


def get_predictions(cards,length,mod_id,models=models):
    
    mod = models[mod_id]
    cards = max([1,cards])
    length = max([1,length])
    
    predictions = [
        mod.predict(np.random.normal(0,.5,(length,5))) for i in range(0,cards)]
    
    
    out = {f"card-{j}":list(i)  for i,j in zip(predictions,range(cards))}
    
    return out
