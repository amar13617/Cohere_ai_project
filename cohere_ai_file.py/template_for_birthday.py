import cohere

co = cohere.Client('AHDicrFO7YMJeBBposjKkGAz7Dxj34WSRcqUQyo6') 

response = co.generate(
  model='command',
  prompt='create a template for a birthday :',
  max_tokens=42,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
