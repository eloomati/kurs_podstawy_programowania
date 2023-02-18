tools = ['lornetka', 'lupa', 'teleskop', 'sonda']
tools.append('łazik')
print(tools)

tools += ['czujnik']
print(tools)

tools = tools + ['komputer pokładowy']
print(tools)

tools += 'czujnik2'
print(tools)

tools = []
tools.append('lornetka')
tools += ["lupa"]
tools = tools + ["teleskop"]
print(len(tools))
print(tools)
print(tools[-2])

