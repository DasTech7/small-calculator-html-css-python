from browser import document, alert, console

calc = document["result"]
inputs = [
  document["first"],
  document["second"],
]
operator = document["operator"]


def summ(e):
  result = ''
  first = ''
  second = ''
  typeOfOper = operator.value

  try:
    first = float(inputs[0].value)
    second = float(inputs[1].value)
  except:
    alert("plz enter any number")
  
  if typeOfOper=="+": result = first+second
  elif typeOfOper=="-": result = first-second
  elif typeOfOper=="x": result = first*second
  elif typeOfOper=="/": result = first/second
  calc.innerText = result

document["calc"].bind(
  'click', 
  summ
)
