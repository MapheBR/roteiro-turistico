class Node:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, content, root=None):
        if self.root is None:
            self.root = Node(content)
            return

        if root is None:
            root = self.root

        if content.lower() > root.content.lower():
            if root.right is None:
                root.right = Node(content)
            else:
                self.add(content, root.right)
        else:
            if root.left is None:
                root.left = Node(content)
            else:
                self.add(content, root.left)

    def remove(self, content, root=None, parent=None):
        if self.root is None:
            return False

        if root is None:
            root = self.root

        if content.lower() < root.content.lower():
            if root.left:
                return self.remove(content, root.left, root)
        elif content.lower() > root.content.lower():
            if root.right:
                return self.remove(content, root.right, root)
        else:
            if root.left is None and root.right is None:
                if parent is None:
                    self.root = None
                elif parent.left == root:
                    parent.left = None
                else:
                    parent.right = None
                return True

            elif root.left is None:
                if parent is None:
                    self.root = root.right
                elif parent.left == root:
                    parent.left = root.right
                else:
                    parent.right = root.right
                return True

            elif root.right is None:
                if parent is None:
                    self.root = root.left
                elif parent.left == root:
                    parent.left = root.left
                else:
                    parent.right = root.left
                return True

            else:
                successor_parent = root
                successor = root.right

                while successor.left is not None:
                    successor_parent = successor
                    successor = successor.left

                root.content = successor.content

                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
                return True

        return False

    def printTreeInOrd(self, root=None):
        if root is None:
            root = self.root

        if root:
            if root.left:
                self.printTreeInOrd(root.left)
            print(f" - {root.content}")
            if root.right:
                self.printTreeInOrd(root.right)

    def printPreOrder(self, root=None):
        if root is None:
            root = self.root

        if root:
            print(f" - {root.content}")
            if root.left:
                self.printPreOrder(root.left)
            if root.right:
                self.printPreOrder(root.right)

    def printPostOrder(self, root=None):
        if root is None:
            root = self.root

        if root:
            if root.left:
                self.printPostOrder(root.left)
            if root.right:
                self.printPostOrder(root.right)
            print(f" - {root.content}")

    def search(self, content, root=None):
        if root is None:
            root = self.root

        if root is None:
            return None

        if content.lower() == root.content.lower():
            return root
        elif content.lower() < root.content.lower():
            return self.search(content, root.left) if root.left else None
        else:
            return self.search(content, root.right) if root.right else None

    # ===== MÉTODO GET_HEIGHT CORRIGIDO =====
    def get_height(self, root=None):
        # Se não passou root, usa a raiz
        if root is None:
            root = self.root

        # Se o nó é vazio, altura é 0
        if root is None:
            return 0

        # Calcula altura da esquerda
        esquerda = 0
        if root.left is not None:
            esquerda = self.get_height(root.left)

        # Calcula altura da direita
        direita = 0
        if root.right is not None:
            direita = self.get_height(root.right)

        # Retorna a maior + 1
        if esquerda > direita:
            return esquerda + 1
        else:
            return direita + 1


def menu():
    roteiro = Tree()

    destinos_iniciais = [
        "Cristo Redentor (Rio de Janeiro)",
        "Pelourinho (Salvador)",
        "Teatro Amazonas (Manaus)",
        "Parque Ibirapuera (São Paulo)",
        "Catedral de Brasília (Brasília)",
        "Bonito (Mato Grosso do Sul)",
        "Fernando de Noronha (Pernambuco)"
    ]

    print("\nCarregando destinos turísticos iniciais...")
    for destino in destinos_iniciais:
        roteiro.add(destino)
    print(f"{len(destinos_iniciais)} destinos carregados com sucesso!")

    while True:
        print("\n" + "="*50)
        print("          ROTEIRO TURÍSTICO - ÁRVORE BINÁRIA")
        print("="*50)
        print("1. Exibir roteiro em ordem alfabética")
        print("2. Exibir roteiro em pré-ordem")
        print("3. Exibir roteiro em pós-ordem")
        print("4. Adicionar novo destino")
        print("5. Remover um destino")
        print("6. Buscar um destino")
        print("7. Mostrar altura da árvore")
        print("8. Sair")
        print("-"*50)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n--- Roteiro em Ordem Alfabética (In-Ordem) ---")
            if roteiro.root is None:
                print("O roteiro está vazio.")
            else:
                roteiro.printTreeInOrd()
            input("\nPressione Enter para continuar...")

        elif opcao == '2':
            print("\n--- Roteiro em Pré-Ordem (Raiz -> Esquerda -> Direita) ---")
            if roteiro.root is None:
                print("O roteiro está vazio.")
            else:
                roteiro.printPreOrder()
            input("\nPressione Enter para continuar...")

        elif opcao == '3':
            print("\n--- Roteiro em Pós-Ordem (Esquerda -> Direita -> Raiz) ---")
            if roteiro.root is None:
                print("O roteiro está vazio.")
            else:
                roteiro.printPostOrder()
            input("\nPressione Enter para continuar...")

        elif opcao == '4':
            novo_destino = input("Digite o nome do novo destino turístico: ").strip()
            if novo_destino:
                if roteiro.search(novo_destino):
                    print(f"O destino '{novo_destino}' já está cadastrado!")
                else:
                    roteiro.add(novo_destino)
                    print(f"Destino '{novo_destino}' adicionado com sucesso!")
            else:
                print("Nome inválido. Tente novamente.")
            input("\nPressione Enter para continuar...")

        elif opcao == '5':
            destino_remover = input("Digite o nome do destino a ser removido: ").strip()
            if destino_remover:
                if roteiro.remove(destino_remover):
                    print(f"Destino '{destino_remover}' removido com sucesso!")
                else:
                    print(f"Destino '{destino_remover}' não encontrado no roteiro.")
            else:
                print("Nome inválido. Tente novamente.")
            input("\nPressione Enter para continuar...")

        elif opcao == '6':
            destino_buscar = input("Digite o nome do destino a ser buscado: ").strip()
            if destino_buscar:
                resultado = roteiro.search(destino_buscar)
                if resultado:
                    print(f"Destino encontrado: {resultado.content}")
                else:
                    print(f"Destino '{destino_buscar}' não encontrado.")
            else:
                print("Nome inválido. Tente novamente.")
            input("\nPressione Enter para continuar...")

        elif opcao == '7':
            altura = roteiro.get_height()
            print(f"Altura da árvore: {altura}")
            if altura >= 0:
                print(f"   (Número de níveis: {altura + 1})")
            input("\nPressione Enter para continuar...")

        elif opcao == '8':
            print("\nSaindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Escolha um número de 1 a 8.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    menu()