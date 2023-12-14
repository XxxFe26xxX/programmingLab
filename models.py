

class Model:
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
        
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')
        
class IncrementModel(Model):
    def predict(self, data):
        predictions = []
        temp = 0
        for i in range(len(data)-1):
                delta = abs(data[i+1] - data[i])
                temp = temp + delta
                average_delta = temp / len(data)
            #return average_delta
                predictions.append(average_delta)
        return predictions

data = [50,52,60]

m = IncrementModel()
print(m.predict(data))