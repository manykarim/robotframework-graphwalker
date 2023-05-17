from robot.api import TestSuite, ResultWriter
import json

suite = TestSuite('Walker')

# read the json file model.json
with open('model.json') as f:
    # read the file line by line
    # read each line as a json object
    # append the json object to the list
    model_list = [json.loads(line) for line in f]


    
# read the json file path.json
with open('path.json') as f:
    # read the file line by line
    # read each line as a json object
    # append the json object to the list
    path_list = [json.loads(line) for line in f]

# print the model
print(model_list)

# print the path
print(path_list)

for model in model_list[0]['models']:
    print(model['name'])
    suite.resource.imports.resource(model['name'] + '.resource')
    for vertice in model['vertices']:
        print(vertice['name'])
    for edge in model['edges']:
        print(edge['name'])

test = suite.tests.create('Walker Test')

for path in path_list:
    print(path['modelName'])
    print(path['currentElementName'])
    kw = path['currentElementName']
    kw_args = []

    # Add Keyword with Arguments to Test Case
    for data in path['data']:
        # each data is a dictionary
        # get the key and value of the dictionary
        for key, value in data.items():
            if key != 'JsonContext':
                print(key)
                print(value)
                kw_args.append(f'{key}={value}')

    test.body.create_keyword(kw, kw_args)

result = suite.run(output='output.xml')
ResultWriter(result).write_results(report='report.html', log=None)
ResultWriter('output.xml').write_results()

