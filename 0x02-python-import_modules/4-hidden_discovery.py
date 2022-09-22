
#!/usr/bin/python3
if __name__ == "__import__":
    import hidden_4
    for name in dir(hidden_4.pyc):
        if name[0] != '_' and name[1] != '_':
            print(name)
