class ListNodes :

    @staticmethod
    def list_nodes(app1):
        nodes = app1.getChildren()

        print("Number of nodes:", len(nodes))

        for n in nodes:
            print(n.getScriptName())