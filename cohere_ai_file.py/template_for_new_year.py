import cohere

co = cohere.Client('MUuqoZhxXI2AwhpYRZppOD8FNPebgSyHbX7YADiZ') 

response = co.generate(
  model='command',
  prompt='create a template for a new year :',
  max_tokens=42,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
