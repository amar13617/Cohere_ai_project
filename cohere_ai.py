import cohere
co = cohere.Client('BZY3Z23n0BvI984Zf43VwLvpWbXXxprrAHYd5skS') # This is your trial API key
response = co.generate(
  model='command',
  prompt='write a poem to generate AI:',
  max_tokens=42,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))