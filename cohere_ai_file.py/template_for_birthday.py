import cohere

co = cohere.Client('BZY3Z23n0BvI984Zf43VwLvpWbXXxprrAHYd5skS') 

response = co.generate(
  model='command',
  prompt='create a template for a birthday :',
  max_tokens=42,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
